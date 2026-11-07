--[[
WFATest - wow-forever-agent test snapshots.

WHAT IT DOES
  Reads the player's own stats, buffs, talents, Legacy perks, gear, spellbook and spell tooltips
  and stores them in SavedVariables (WFATestDB). scripts/read_addon_data.py in the repo reads
  that file after a /reload or logout. Works on any class.
  /wfa probe asks the client which reads it allows, out of combat and in combat, so we learn
  what CAN be logged instead of guessing. The session log (/wfa auto) stores one small record
  on plain game events (entered combat, left combat, XP, level up, zone, death) while you play.
  That is all.

RULES THIS FILE FOLLOWS (see docs/addon-feasibility.md)
  1. Read-only. No casting, targeting, chat, or input of any kind.
  2. WoW Forever inherits retail's "secret value" restrictions. A secret may be held but not
     compared, used in arithmetic, indexed, or saved (it is written to disk as nil).
     Every value from the game goes through W.safe() BEFORE anything else touches it.
     A secret is recorded as the marker string "SECRET". We never try to recover the number.
  3. Every game call goes through W.read(), which uses pcall and tolerates a missing function,
     because the beta API will change between builds.
  4. No combat log events. They are not available to addons on this client. Per-heal data comes
     from the game's own /combatlog file, parsed outside the game. The session log uses only
     plain state events (PLAYER_REGEN_*, PLAYER_XP_UPDATE, ...) and stores values; it never
     computes on them. Other players are never recorded.
  5. No frames, no hooks into Blizzard UI, so nothing here can taint the default interface.
]]

local ADDON, W = ...
W.version = "0.3.0"
W.schema = 1

local MAX_SNAPSHOTS = 400
local MAX_EVENTS = 4000       -- session log records
local MAX_SPELLS = 300        -- per spellbook scan
local SCHOOLS = { [2] = "holy", [3] = "fire", [4] = "nature", [5] = "frost", [6] = "shadow", [7] = "arcane" }
local STAT_NAMES = { "strength", "agility", "stamina", "intellect", "spirit" }
-- Class trait tree ids, from the datamined TraitTree table (build 1.60.1.69893).
local CLASS_TREE = { DRUID = 1089, HUNTER = 1091, PALADIN = 1100, PRIEST = 1114, ROGUE = 1111,
                     SHAMAN = 1082, MAGE = 1112, WARLOCK = 1116, WARRIOR = 1117 }
local LEGACY_TREES = { professions = 1187, adventure = 1188, resourcefulness = 1189 }

local function say(msg)
    print("|cff66ccffWFA|r " .. tostring(msg))
end

---------------------------------------------------------------------------
-- Secret-safe primitives
---------------------------------------------------------------------------

local function isSecret(v)
    if type(issecretvalue) == "function" then
        local ok, res = pcall(issecretvalue, v)
        if ok and res then return true end
    end
    return false
end

-- Turn ONE game value into something that is safe to store.
function W.safe(v)
    if isSecret(v) then return "SECRET" end
    local t = type(v)
    if t == "nil" then return "NIL" end
    if t == "number" or t == "string" or t == "boolean" then return v end
    return "UNSUPPORTED:" .. t
end

-- One level of a returned table (cooldown info, aura data), each field made safe on its own.
function W.safeDeep(v)
    if isSecret(v) then return "SECRET" end
    if type(v) ~= "table" then return W.safe(v) end
    local out, n = {}, 0
    local ok = pcall(function()
        for k, val in pairs(v) do
            if (type(k) == "string" or type(k) == "number") and n < 40 then
                n = n + 1
                out[k] = W.safe(val)
            end
        end
    end)
    if not ok then return "SECRET_TABLE" end
    return out
end

-- Call a game function defensively. Returns a list of safe values, or a marker table.
local function readWith(conv, fn, ...)
    if type(fn) ~= "function" then return { missing = true } end
    local function pack(ok, ...)
        return ok, select("#", ...), { ... }
    end
    local ok, n, vals = pack(pcall(fn, ...))
    if not ok then
        local e = vals[1]
        return { err = isSecret(e) and "SECRET" or tostring(e) }
    end
    local out = { n = n }
    for i = 1, n do out[i] = conv(vals[i]) end
    return out
end

function W.read(fn, ...) return readWith(W.safe, fn, ...) end
function W.readDeep(fn, ...) return readWith(W.safeDeep, fn, ...) end

-- First return value only, already made safe.
function W.read1(fn, ...)
    local r = W.read(fn, ...)
    if r.missing then return "MISSING" end
    if r.err then return "ERROR:" .. r.err end
    return r[1] == nil and "NIL" or r[1]
end

-- Read a field from a table that may itself be secret (indexing a secret table errors).
local function field(t, k)
    local ok, v = pcall(function() return t[k] end)
    if not ok then return "SECRET_TABLE" end
    return W.safe(v)
end

-- Resolve "C_Foo.Bar" without erroring when the namespace is absent.
local function fn(path)
    local ns, name = path:match("^([%w_]+)%.([%w_]+)$")
    if ns then
        local t = _G[ns]
        return type(t) == "table" and t[name] or nil
    end
    return _G[path]
end

---------------------------------------------------------------------------
-- What gets captured
---------------------------------------------------------------------------

function W.environment()
    local env = {}
    local b = W.read(GetBuildInfo)
    env.version, env.build, env.buildDate, env.interface = b[1], b[2], b[3], b[4]
    env.projectId = W.safe(WOW_PROJECT_ID)
    env.inCombat = W.read1(InCombatLockdown)
    env.hasIsSecretValue = type(issecretvalue) == "function"
    env.hasSecretRestrictions = W.read1(fn("C_Secrets.HasSecretRestrictions"))
    env.unitStatsSecret = W.read1(fn("C_Secrets.ShouldUnitStatsBeSecret"))
    env.aurasSecret = W.read1(fn("C_Secrets.ShouldAurasBeSecret"))
    env.restrictions = {}
    local active = fn("C_RestrictedActions.IsAddOnRestrictionActive")
    local enum = Enum and Enum.AddOnRestrictionType
    if type(enum) == "table" then
        for name, value in pairs(enum) do
            env.restrictions[name] = W.read1(active, value)
        end
    else
        env.restrictions.enumMissing = true
    end
    local inInstance = W.read(IsInInstance)
    env.inInstance, env.instanceType = inInstance[1], inInstance[2]
    env.zone = W.read1(GetRealZoneText)
    return env
end

function W.stats()
    local s = {}
    s.level = W.read1(UnitLevel, "player")
    s.class = W.read(UnitClass, "player")[2]
    s.race = W.read(UnitRace, "player")[2]
    s.healthMax = W.read1(UnitHealthMax, "player")
    s.powerMax = W.read1(UnitPowerMax, "player")
    s.bonusHealing = W.read1(GetSpellBonusHealing)
    s.bonusDamage, s.spellCrit = {}, {}
    for id, name in pairs(SCHOOLS) do
        s.bonusDamage[name] = W.read1(GetSpellBonusDamage, id)
        s.spellCrit[name] = W.read1(GetSpellCritChance, id)
    end
    local ap = W.read(UnitAttackPower, "player")
    s.attackPower = { base = ap[1], pos = ap[2], neg = ap[3], missing = ap.missing, err = ap.err }
    s.meleeCrit = W.read1(GetCritChance)
    s.spellHaste = W.read1(UnitSpellHaste, "player")
    s.haste = W.read1(GetHaste)
    s.hitModifier = W.read1(GetHitModifier)
    s.spellHitModifier = W.read1(GetSpellHitModifier)
    local regen = W.read(GetManaRegen)
    s.manaRegen = { notCasting = regen[1], casting = regen[2], missing = regen.missing, err = regen.err }
    s.primary = {}
    for i, name in ipairs(STAT_NAMES) do
        local r = W.read(UnitStat, "player", i)
        s.primary[name] = { base = r[1], effective = r[2], pos = r[3], neg = r[4], missing = r.missing, err = r.err }
    end
    return s
end

function W.auras()
    local get = fn("C_UnitAuras.GetAuraDataByIndex")
    if type(get) ~= "function" then return { missing = true } end
    local list = {}
    for i = 1, 40 do
        local ok, data = pcall(get, "player", i, "HELPFUL")
        if not ok then
            list[#list + 1] = { err = tostring(data) }
            break
        end
        -- Secrecy check FIRST: comparing a secret (even to nil) raises an error.
        if isSecret(data) then
            list[#list + 1] = { secret = true }
        elseif data == nil then
            break
        else
            list[#list + 1] = {
                name = field(data, "name"), spellId = field(data, "spellId"),
                stacks = field(data, "applications"), duration = field(data, "duration"),
                expires = field(data, "expirationTime"), fromPlayer = field(data, "isFromPlayerOrPlayerPet"),
            }
        end
    end
    return list
end

local function spellText(spellID)
    local out = { name = W.read1(fn("C_Spell.GetSpellName"), spellID),
                  description = W.read1(fn("C_Spell.GetSpellDescription"), spellID) }
    local tip = fn("C_TooltipInfo.GetSpellByID")
    if type(tip) == "function" then
        local ok, data = pcall(tip, spellID)
        if ok and type(data) == "table" and not isSecret(data) then
            out.lines = {}
            local okLines, rawLines = pcall(function() return data.lines end)
            if okLines and type(rawLines) == "table" and not isSecret(rawLines) then
                for i, line in ipairs(rawLines) do
                    out.lines[i] = { left = field(line, "leftText"), right = field(line, "rightText") }
                end
            else
                out.linesUnavailable = true
            end
        elseif not ok then
            out.tooltipErr = tostring(data)
        end
    else
        out.tooltipMissing = true
    end
    return out
end

-- Walk one trait tree: node -> entries -> definition -> spell, with purchased ranks.
function W.traitTree(treeID)
    local out = { treeID = treeID, nodes = {} }
    local cfg = W.read1(fn("C_Traits.GetConfigIDByTreeID"), treeID)
    out.configID = cfg
    if type(cfg) ~= "number" then return out end
    local getNodes, getNode = fn("C_Traits.GetTreeNodes"), fn("C_Traits.GetNodeInfo")
    local getEntry, getDef = fn("C_Traits.GetEntryInfo"), fn("C_Traits.GetDefinitionInfo")
    local ok, nodeIDs = pcall(getNodes, treeID)
    if not ok or type(nodeIDs) ~= "table" then
        out.err = tostring(nodeIDs)
        return out
    end
    for _, nodeID in ipairs(nodeIDs) do
        local okN, node = pcall(getNode, cfg, nodeID)
        if okN and type(node) == "table" and not isSecret(node) then
            local rec = { nodeID = nodeID, ranks = field(node, "activeRank"), current = field(node, "currentRank"),
                          maxRanks = field(node, "maxRanks"), posX = field(node, "posX"), posY = field(node, "posY"),
                          entries = {} }
            local okE, entryIDs = pcall(function() return node.entryIDs end)
            if okE and type(entryIDs) == "table" then
                for _, entryID in ipairs(entryIDs) do
                    local e = { entryID = entryID }
                    local ok1, entry = pcall(getEntry, cfg, entryID)
                    if ok1 and type(entry) == "table" then
                        e.maxRanks = field(entry, "maxRanks")
                        local okD, defID = pcall(function() return entry.definitionID end)
                        if okD and type(defID) == "number" then
                            local ok2, def = pcall(getDef, defID)
                            if ok2 and type(def) == "table" then
                                e.definitionID = defID
                                e.spellID = field(def, "spellID")
                                e.overrideName = field(def, "overrideName")
                                if type(e.spellID) == "number" then
                                    e.name = W.read1(fn("C_Spell.GetSpellName"), e.spellID)
                                    -- Description is rendered at the player's CURRENT rank: this is
                                    -- the text to compare against the datamined per-rank values.
                                    e.description = W.read1(fn("C_Spell.GetSpellDescription"), e.spellID)
                                end
                            end
                        end
                    end
                    rec.entries[#rec.entries + 1] = e
                end
            end
            out.nodes[#out.nodes + 1] = rec
        end
    end
    return out
end

-- Equipped item links, slots 1-19. A link is plain text; stats are read from it outside the game.
function W.gear()
    local g = {}
    for slot = 1, 19 do
        local link = W.read1(GetInventoryItemLink, "player", slot)
        if type(link) == "string" and link:find("|H", 1, true) then g["slot" .. slot] = link end
    end
    return g
end

-- Every spell in the player's spellbook with its live tooltip. Class-agnostic.
function W.spellbook()
    local out = { spells = {} }
    local getLine, getItem = fn("C_SpellBook.GetSpellBookSkillLineInfo"), fn("C_SpellBook.GetSpellBookItemInfo")
    local nLines = W.read1(fn("C_SpellBook.GetNumSpellBookSkillLines"))
    out.skillLines = nLines
    if type(nLines) ~= "number" or type(getLine) ~= "function" or type(getItem) ~= "function" then
        out.missing = true
        return out
    end
    local bank = Enum and Enum.SpellBookSpellBank and Enum.SpellBookSpellBank.Player or 0
    for i = 1, nLines do
        local okL, line = pcall(getLine, i)
        if okL and type(line) == "table" and not isSecret(line) then
            local lineName, offset, count = field(line, "name"), field(line, "itemIndexOffset"), field(line, "numSpellBookItems")
            if type(offset) == "number" and type(count) == "number" then
                for slot = offset + 1, offset + count do
                    if #out.spells >= MAX_SPELLS then break end
                    local okI, item = pcall(getItem, slot, bank)
                    if okI and type(item) == "table" and not isSecret(item) then
                        local spellID = field(item, "spellID")
                        if type(spellID) == "number" then
                            local rec = spellText(spellID)
                            rec.spellID, rec.line = spellID, lineName
                            rec.itemType, rec.passive = field(item, "itemType"), field(item, "isPassive")
                            rec.subName = field(item, "subName")
                            out.spells[#out.spells + 1] = rec
                        end
                    end
                end
            end
        end
    end
    return out
end

-- PROBE: ask the client what it lets an addon read right now. Each call is stored as its safe
-- values or as SECRET / MISSING / an error string. Run out of combat and again in combat, the
-- two lists are what can and cannot be logged. Nothing here is compared or computed on.
local PROBES = {
    { "UnitHealth", "player" }, { "UnitHealthMax", "player" }, { "UnitPower", "player" }, { "UnitPowerMax", "player" },
    { "UnitPowerType", "player" }, { "UnitXP", "player" }, { "UnitXPMax", "player" }, { "GetXPExhaustion" }, { "GetMoney" },
    { "UnitExists", "target" }, { "UnitName", "target" }, { "UnitLevel", "target" }, { "UnitClassification", "target" },
    { "UnitCreatureType", "target" }, { "UnitHealth", "target" }, { "UnitHealthMax", "target" },
    { "UnitThreatSituation", "player", "target" }, { "UnitDetailedThreatSituation", "player", "target" },
    { "GetSpellBonusHealing" }, { "GetSpellBonusDamage", 3 }, { "GetSpellCritChance", 3 }, { "GetCritChance" },
    { "GetRangedCritChance" }, { "GetHaste" }, { "UnitSpellHaste", "player" }, { "GetHitModifier" }, { "GetSpellHitModifier" },
    { "UnitAttackPower", "player" }, { "UnitRangedAttackPower", "player" }, { "UnitDamage", "player" },
    { "UnitAttackSpeed", "player" }, { "UnitRangedDamage", "player" }, { "UnitArmor", "player" }, { "UnitStat", "player", 4 },
    { "GetDodgeChance" }, { "GetParryChance" }, { "GetBlockChance" }, { "GetManaRegen" }, { "GetPowerRegen" },
    { "GetComboPoints", "player", "target" }, { "GetShapeshiftForm" }, { "GetTotemInfo", 1 },
    { "UnitCastingInfo", "player" }, { "UnitChannelInfo", "player" },
    { "C_Spell.GetSpellCooldown", 61304 }, { "C_Spell.GetSpellCharges", 61304 },
    { "C_UnitAuras.GetAuraDataByIndex", "player", 1, "HELPFUL" }, { "C_UnitAuras.GetAuraDataByIndex", "player", 1, "HARMFUL" },
    { "C_UnitAuras.GetAuraDataByIndex", "target", 1, "HARMFUL" }, { "C_UnitAuras.GetAuraDataByIndex", "pet", 1, "HELPFUL" },
    { "UnitHealth", "pet" }, { "UnitPower", "pet" },
    { "GetInventoryItemLink", "player", 16 }, { "GetInventoryItemDurability", 16 },
    { "GetUnitSpeed", "player" }, { "IsResting" }, { "GetNumGroupMembers" },
}
local PROBE_NAMESPACES = { "C_Secrets", "C_RestrictedActions", "C_DamageMeter", "C_CombatLog", "C_CombatText",
                           "C_UnitAuras", "C_Spell", "C_SpellBook", "C_Traits", "C_TooltipInfo", "C_Item",
                           "C_PaperDollInfo", "C_StatTracking", "C_EncounterJournal" }

function W.probe(label)
    local rec = { label = label, time = time(), date = date("%Y-%m-%d %H:%M:%S"), env = W.environment(), results = {} }
    rec.class = W.read(UnitClass, "player")[2]
    for _, p in ipairs(PROBES) do
        local key = p[1] .. "(" .. table.concat(p, ",", 2) .. ")"
        rec.results[key] = W.readDeep(fn(p[1]), unpack(p, 2))
    end
    if label == "ooc" then
        -- Function NAMES only: which API namespaces this build has. Tells us what to probe next.
        rec.namespaces = {}
        for _, ns in ipairs(PROBE_NAMESPACES) do
            local t = _G[ns]
            if type(t) == "table" then
                local names = {}
                pcall(function()
                    for k, v in pairs(t) do
                        if type(k) == "string" and type(v) == "function" then names[#names + 1] = k end
                    end
                end)
                table.sort(names)
                rec.namespaces[ns] = table.concat(names, " ")
            else
                rec.namespaces[ns] = "MISSING"
            end
        end
    end
    return rec
end

---------------------------------------------------------------------------
-- Storage
---------------------------------------------------------------------------

local function db()
    if type(WFATestDB) ~= "table" or WFATestDB.schema ~= W.schema then
        WFATestDB = { schema = W.schema, snapshots = {}, talents = {}, tooltips = {} }
    end
    local d = WFATestDB
    d.addonVersion = W.version          -- the version that last wrote the file, not the one that created it
    -- Lists added in 0.3.0; a file made by an older version gains them here.
    d.probes, d.session, d.spellbooks = d.probes or {}, d.session or {}, d.spellbooks or {}
    if d.auto == nil then d.auto = true end
    return d
end

local function push(list, item, cap)
    list[#list + 1] = item
    cap = cap or MAX_SNAPSHOTS
    while #list > cap do table.remove(list, 1) end
end

function W.snapshot(label, quiet, withGear)
    local snap = { label = label or "unlabelled", time = time(), date = date("%Y-%m-%d %H:%M:%S"),
                   env = W.environment(), stats = W.stats(), auras = W.auras() }
    if withGear then snap.gear = W.gear() end
    push(db().snapshots, snap)
    if not quiet then
        say(("snapshot '%s' stored (#%d). Healing bonus: %s. /reload to write it to disk.")
            :format(snap.label, #db().snapshots, tostring(snap.stats.bonusHealing)))
    end
    return snap
end

---------------------------------------------------------------------------
-- Session log: one small record per plain game event while /wfa auto is on
---------------------------------------------------------------------------

-- The current target, only if it is NOT a player. Other players are never recorded.
local function targetInfo()
    if W.read1(UnitExists, "target") ~= true then return nil end
    if W.read1(UnitIsPlayer, "target") ~= false then return { player = true } end
    return { name = W.read1(UnitName, "target"), level = W.read1(UnitLevel, "target"),
             rank = W.read1(UnitClassification, "target"), kind = W.read1(UnitCreatureType, "target"),
             hpMax = W.read1(UnitHealthMax, "target") }
end

function W.light(event, extra)
    local d = db()
    if not d.auto then return end
    local r = { e = event, t = time(),
                lvl = W.read1(UnitLevel, "player"), xp = W.read1(UnitXP, "player"), xpMax = W.read1(UnitXPMax, "player"),
                rested = W.read1(GetXPExhaustion), hp = W.read1(UnitHealth, "player"), hpMax = W.read1(UnitHealthMax, "player"),
                mp = W.read1(UnitPower, "player"), mpMax = W.read1(UnitPowerMax, "player"), money = W.read1(GetMoney),
                zone = W.read1(GetRealZoneText), sub = W.read1(GetSubZoneText), combat = W.read1(InCombatLockdown) }
    if extra then for k, v in pairs(extra) do r[k] = v end end
    push(d.session, r, MAX_EVENTS)
end

---------------------------------------------------------------------------
-- Slash commands
---------------------------------------------------------------------------

local watcher

local function cmdWatch(rest)
    local seconds, label = rest:match("^(%d+)%s*(.*)$")
    seconds = tonumber(seconds)
    if not seconds or seconds < 1 or seconds > 120 then
        say("usage: /wfa watch <1-120 seconds> [label]   e.g. /wfa watch 25 bloodfury")
        return
    end
    if watcher then watcher:Cancel() end
    label = (label and label ~= "") and label or "watch"
    local tick = 0
    say(("watching for %d sec as '%s'. Use your ability now. Stay out of combat."):format(seconds, label))
    W.snapshot(label .. ":0", true)
    watcher = C_Timer.NewTicker(1, function()
        tick = tick + 1
        W.snapshot(label .. ":" .. tick, true)
        if tick >= seconds then
            say(("watch '%s' finished, %d samples. /reload to write them to disk."):format(label, seconds + 1))
            watcher = nil
        end
    end, seconds)
end

local function cmdTalents(quiet)
    local class = W.read(UnitClass, "player")[2]
    local rec = { time = time(), date = date("%Y-%m-%d %H:%M:%S"), env = W.environment(), class = class, trees = {} }
    if type(class) == "string" and CLASS_TREE[class] then
        rec.trees.class = W.traitTree(CLASS_TREE[class])
    end
    for name, id in pairs(LEGACY_TREES) do
        rec.trees["legacy_" .. name] = W.traitTree(id)
    end
    push(db().talents, rec)
    local n = rec.trees.class and #rec.trees.class.nodes or 0
    if not quiet then
        say(("talent and Legacy trees stored (%d class nodes). /reload to write to disk."):format(n))
    end
end

local function cmdSpells(quiet)
    if InCombatLockdown and InCombatLockdown() then
        say("spellbook scan runs out of combat only.")
        return
    end
    local rec = W.spellbook()
    rec.time, rec.date, rec.env = time(), date("%Y-%m-%d %H:%M:%S"), W.environment()
    rec.class, rec.level = W.read(UnitClass, "player")[2], W.read1(UnitLevel, "player")
    push(db().spellbooks, rec, 12)
    if rec.missing then
        say("spellbook API not found on this build; recorded that. Use /wfa tip <spellID> instead.")
    elseif not quiet then
        say(("spellbook stored: %d spells with live tooltips. /reload to write to disk."):format(#rec.spells))
    end
end

local pending = {}      -- one-shot jobs for the next time combat starts

local function cmdProbe()
    if InCombatLockdown and InCombatLockdown() then
        push(db().probes, W.probe("combat"), 40)
        say("in-combat probe stored. Run /wfa probe again out of combat for the other half.")
        return
    end
    push(db().probes, W.probe("ooc"), 40)
    pending.probe = true
    say("out-of-combat probe stored. NOW: target a mob and fight it; I probe again at the start of")
    say("the fight and 3 sec in. Casting something during the fight makes the probe more useful. Then /reload.")
end

local function cmdAuto(rest)
    local d = db()
    rest = (rest or ""):lower()
    if rest == "on" then
        d.auto = true
        W.light("auto_on")
    elseif rest == "off" then
        W.light("auto_off")
        d.auto = false
    end
    say(("session log is %s, %d records stored (max %d). /wfa auto on | off")
        :format(d.auto and "ON" or "OFF", #d.session, MAX_EVENTS))
end

local function cmdTip(rest)
    local id = tonumber(rest)
    if not id then
        say("usage: /wfa tip <spellID>   e.g. /wfa tip 408521  (Riptide)")
        return
    end
    local rec = spellText(id)
    rec.spellID, rec.time, rec.env = id, time(), W.environment()
    push(db().tooltips, rec)
    say(("tooltip for %s (%d) stored."):format(tostring(rec.name), id))
end

local function cmdStatus()
    local env = W.environment()
    say(("v%s | client %s (%s) interface %s"):format(W.version, tostring(env.version), tostring(env.build), tostring(env.interface)))
    say(("secret system present: %s | restrictions active now: %s | stats secret now: %s")
        :format(tostring(env.hasIsSecretValue), tostring(env.hasSecretRestrictions), tostring(env.unitStatsSecret)))
    say(("healing bonus reads as: %s | stored: %d snapshots, %d talent dumps, %d tooltips")
        :format(tostring(W.read1(GetSpellBonusHealing)), #db().snapshots, #db().talents, #db().tooltips))
    say(("session log %s: %d records | %d probes | %d spellbook scans")
        :format(db().auto and "ON" or "OFF", #db().session, #db().probes, #db().spellbooks))
end

-- One command for the whole first-session test card. Still read-only: it only calls the
-- readers above, in order, and tells the player which single button to press.
local GO_TIPS = { 408521, 408510, 16190 }   -- Riptide, Water Shield, Mana Tide Totem (Shaman only)

local function cmdGo()
    if InCombatLockdown and InCombatLockdown() then
        say("you are in combat. Finish the fight, then type /wfa go again.")
        return
    end
    cmdStatus()
    local base = W.snapshot("baseline", true, true)
    -- W.safe() has already turned a secret into the string "SECRET", so a number here is a
    -- plain number and may be compared. A 10% buff on almost nothing cannot be measured.
    local heal = base.stats.bonusHealing
    if type(heal) == "number" and heal < 30 then
        say(("WARNING: healing bonus is only %d. A 10%% buff needs about 30 or more to show. "):format(heal)
            .. "The run still records everything else; redo this part with more spell power.")
    end
    cmdTalents()
    local _, class = UnitClass("player")
    if class == "SHAMAN" then
        for _, id in ipairs(GO_TIPS) do cmdTip(tostring(id)) end
    end
    cmdSpells()
    push(db().probes, W.probe("ooc"), 40)
    pending.probe = true
    local _, race = UnitRace("player")
    local label = (race == "Orc") and "bloodfury" or "buff"
    cmdWatch("25 " .. label)
    pending.snap = true
    say("==================================================")
    if race == "Orc" then
        say("NOW: wait 3 seconds, then press BLOOD FURY. Stand still for 25 sec.")
    else
        say("NOW: wait 3 seconds, then use any spell power trinket or buff. Stand still for 25 sec.")
    end
    say("THEN: attack one mob (I take the in-combat snapshot and probe myself), then type /reload.")
    say("==================================================")
end

local function cmdHelp()
    say("commands:")
    say("  /wfa go                  THE EASY ONE: runs the whole test card; you press one ability, hit one mob, /reload")
    say("  /wfa status              what the client reports right now")
    say("  /wfa snap [label]        one snapshot of stats and buffs")
    say("  /wfa watch <sec> [label] one snapshot per second (use a cooldown during it)")
    say("  /wfa talents             class tree and Legacy trees with your ranks and live tooltips")
    say("  /wfa tip <spellID>       store one spell's live tooltip")
    say("  /wfa spells              every spell in your spellbook with its live tooltip (any class)")
    say("  /wfa probe               what can the game tell an addon? out of combat now, in combat on your next fight")
    say("  /wfa auto on|off         session log: small records on combat start/end, XP, level, zone, death")
    say("  /wfa clear               delete everything stored")
    say("Data is written to disk on /reload or logout.")
end

SLASH_WFATEST1 = "/wfa"
SlashCmdList["WFATEST"] = function(msg)
    msg = (msg or ""):gsub("^%s+", ""):gsub("%s+$", "")
    local cmd, rest = msg:match("^(%S*)%s*(.-)$")
    cmd = (cmd or ""):lower()
    if cmd == "go" then
        cmdGo()
    elseif cmd == "snap" then
        W.snapshot(rest ~= "" and rest or nil, false, true)
    elseif cmd == "spells" then
        cmdSpells()
    elseif cmd == "probe" then
        cmdProbe()
    elseif cmd == "auto" then
        cmdAuto(rest)
    elseif cmd == "watch" then
        cmdWatch(rest)
    elseif cmd == "talents" then
        cmdTalents()
    elseif cmd == "tip" then
        cmdTip(rest)
    elseif cmd == "status" then
        cmdStatus()
    elseif cmd == "clear" then
        WFATestDB = nil
        db()
        say("stored data cleared.")
    else
        cmdHelp()
    end
end

-- Plain state events only. None of these is a combat log event, and the handler stores values
-- through W.safe() without comparing or computing on them.
local SESSION_EVENTS = { "PLAYER_ENTERING_WORLD", "PLAYER_REGEN_DISABLED", "PLAYER_REGEN_ENABLED", "PLAYER_XP_UPDATE",
                         "PLAYER_LEVEL_UP", "PLAYER_DEAD", "ZONE_CHANGED_NEW_AREA", "PLAYER_EQUIPMENT_CHANGED",
                         "TRAIT_CONFIG_UPDATED" }
local debounce = {}

-- Run job once, `delay` sec after the LAST call with this key, and only out of combat.
local function later(key, delay, job)
    debounce[key] = (debounce[key] or 0) + 1
    local ticket = debounce[key]
    C_Timer.After(delay, function()
        if debounce[key] ~= ticket then return end
        if InCombatLockdown and InCombatLockdown() then return end
        if db().auto then job() end
    end)
end

local loader = CreateFrame("Frame")
loader:RegisterEvent("ADDON_LOADED")
loader:SetScript("OnEvent", function(self, event, a1, a2)
    if event == "ADDON_LOADED" then
        if a1 ~= ADDON then return end
        db()
        self:UnregisterEvent("ADDON_LOADED")
        for _, e in ipairs(SESSION_EVENTS) do pcall(self.RegisterEvent, self, e) end
        say(("loaded. /wfa go runs the whole test, /wfa lists commands. Session log is %s.")
            :format(db().auto and "ON (/wfa auto off to stop)" or "OFF (/wfa auto on to start)"))
    elseif event == "PLAYER_REGEN_DISABLED" then
        -- The plain "entered combat" event. One-shot jobs first, then the session record.
        if pending.snap then
            pending.snap = nil
            W.snapshot("incombat", true)
            say("in-combat snapshot stored. Finish the fight, then type /reload.")
        end
        if pending.probe then
            pending.probe = nil
            push(db().probes, W.probe("combat+0"), 40)
            C_Timer.After(3, function()
                push(db().probes, W.probe("combat+3"), 40)
                say("in-combat probes stored. Finish the fight, then type /reload.")
            end)
        end
        W.light("combat_start", { target = targetInfo() })
    elseif event == "PLAYER_REGEN_ENABLED" then
        W.light("combat_end")
        -- Restrictions may lift a moment after combat ends; a second record shows the real values.
        C_Timer.After(2, function()
            if not (InCombatLockdown and InCombatLockdown()) then W.light("after_combat") end
        end)
    elseif event == "PLAYER_ENTERING_WORLD" then
        local first = (W.safe(a1) == true) or (W.safe(a2) == true)   -- initial login or /reload, not a loading screen
        if first then
            W.light("login", { name = W.read1(UnitName, "player"), class = W.read(UnitClass, "player")[2],
                               race = W.read(UnitRace, "player")[2] })
            later("enter", 5, function() W.snapshot("auto:login", true, true) end)
        else
            W.light("enter_world")
        end
    elseif event == "PLAYER_XP_UPDATE" then
        W.light("xp")
    elseif event == "PLAYER_LEVEL_UP" then
        W.light("level_up", { newLevel = W.safe(a1) })
        later("levelup", 3, function()
            W.snapshot("auto:levelup", true, true)
            cmdSpells(true)
        end)
    elseif event == "PLAYER_DEAD" then
        W.light("dead")
    elseif event == "ZONE_CHANGED_NEW_AREA" then
        W.light("zone")
    elseif event == "PLAYER_EQUIPMENT_CHANGED" then
        later("gear", 3, function() W.snapshot("auto:gear", true, true) end)
    elseif event == "TRAIT_CONFIG_UPDATED" then
        later("talents", 3, function() cmdTalents(true) end)
    end
end)
