# BG helpers — multi-root resolve (gamedir + optional _main_game_assets_root).

define bg_resolution_max = 6

init python:
    import os

    def _fn_for_renpy(path):
        if not path or not isinstance(path, str):
            return path
        return path.replace("\\", "/")

    def _asset_roots():
        roots = [config.gamedir]
        mg = getattr(store, "_main_game_assets_root", "") or ""
        if mg and os.path.isdir(mg):
            roots.append(mg)
        return roots

    def resolve_bg_path(path, max_factor=None):
        if max_factor is None:
            max_factor = getattr(store, "bg_resolution_max", 6)
        base, ext = os.path.splitext(path)

        for root in _asset_roots():
            for factor in (6, 4, 2):
                if factor <= max_factor:
                    candidate = base + "_" + str(factor) + "x" + ext
                    full = os.path.join(root, candidate)
                    if os.path.exists(full):
                        return _fn_for_renpy(os.path.normpath(full))

        if "_day" not in base and "_evening" not in base and "_night" not in base:
            for time_suffix in ("_day", "_evening", "_night"):
                for root in _asset_roots():
                    for factor in (6, 4, 2):
                        if factor <= max_factor:
                            candidate = base + time_suffix + "_" + str(factor) + "x" + ext
                            full = os.path.join(root, candidate)
                            if os.path.exists(full):
                                return _fn_for_renpy(os.path.normpath(full))

        for root in _asset_roots():
            full = os.path.join(root, path)
            if os.path.exists(full):
                return _fn_for_renpy(os.path.normpath(full))
        return _fn_for_renpy(path)

    def apply_bg_blur(displayable):
        return Transform(displayable, blur=0)

    def bg_displayable(path):
        resolved = resolve_bg_path(path)
        return Transform(resolved, fit="cover", xysize=(1920, 1080), blur=0)

    def stnd_music_play():
        pass

    def _reset_bg_blur_after_load():
        if hasattr(store, "bg_blur_amount"):
            store.bg_blur_amount = 0

    config.after_load_callbacks.append(_reset_bg_blur_after_load)
