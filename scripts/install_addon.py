#!/usr/bin/env python3
"""
install_addon.py — Copy addon/WFATest into the WoW Forever AddOns folder.

  python scripts/install_addon.py            install or update
  python scripts/install_addon.py --where    only print the paths it would use
  python scripts/install_addon.py --wow "D:\\Games\\World of Warcraft"

Interface/AddOns is the folder Blizzard provides for user addons. This script writes
nothing else inside the game directory. Stdlib only.
"""
import argparse, pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "addon" / "WFATest"
FLAVORS = ["_classic_beta_", "_forever_", "_classic_forever_"]   # beta slug first; launch name unknown
CANDIDATES = [r"C:\Program Files (x86)\World of Warcraft", r"C:\Program Files\World of Warcraft",
              r"D:\World of Warcraft", r"E:\World of Warcraft", r"D:\Games\World of Warcraft",
              r"E:\Games\World of Warcraft", "/Applications/World of Warcraft"]


def find_flavor(wow_arg):
    roots = [pathlib.Path(wow_arg)] if wow_arg else [pathlib.Path(c) for c in CANDIDATES]
    for r in roots:
        for f in FLAVORS:
            if (r / f).is_dir():
                return r / f
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wow", help="World of Warcraft install folder (the one containing _classic_beta_)")
    ap.add_argument("--where", action="store_true")
    a = ap.parse_args()
    flavor = find_flavor(a.wow)
    if not flavor:
        sys.exit("Could not find a Forever install. Pass --wow \"<World of Warcraft folder>\".")
    dest = flavor / "Interface" / "AddOns" / "WFATest"
    print(f"source : {SRC}\ntarget : {dest}")
    if a.where:
        return
    try:
        dest.mkdir(parents=True, exist_ok=True)
        for f in SRC.iterdir():
            if f.is_file():
                shutil.copy2(f, dest / f.name)
                print(f"  copied {f.name}")
    except PermissionError:
        sys.exit("Permission denied. The game is under Program Files, so run this once from an "
                 "administrator terminal, or copy the addon/WFATest folder into the target by hand.")
    print("Installed. In game: check the AddOns list at character select. If it shows 'Out of date', "
          "tick 'Load out of date AddOns', then tell the agent the interface number from /wfa status.")


if __name__ == "__main__":
    main()
