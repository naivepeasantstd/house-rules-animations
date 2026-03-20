# Optional: game/images/ASSET_ROOT.txt — one line, absolute path to a VN **game** folder
# (directory that contains `images/`). If missing, only this project's gamedir is used.

init -151 python:
    import os

    store._main_game_assets_root = ""
    _hint = os.path.join(config.gamedir, "images", "ASSET_ROOT.txt")
    if os.path.isfile(_hint):
        try:
            with open(_hint, "r", encoding="utf-8") as _f:
                _line = (_f.readline() or "").strip().strip('"')
            if _line and os.path.isdir(_line):
                store._main_game_assets_root = os.path.normpath(_line)
        except Exception:
            pass
