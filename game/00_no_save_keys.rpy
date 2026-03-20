# Quick save/load hotkeys off (main UI already hides Save/Load).

init 999 python:
    for _k in ("quick_save", "quick_load"):
        if _k in config.keymap:
            config.keymap[_k] = list()
