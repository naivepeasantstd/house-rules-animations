# 00NpcAssets.rpy — Same as main game; resolve checks demo gamedir then _main_game_assets_root.

define npc_resolution_max = 2
define npc_texture_scale = 0.5

init -2 python:
    import os

    def _fn_for_renpy(path):
        """Ren'Py expects forward slashes; Windows normpath uses backslash."""
        if not path or not isinstance(path, str):
            return path
        return path.replace("\\", "/")

    def _asset_roots():
        roots = [config.gamedir]
        mg = getattr(store, "_main_game_assets_root", "") or ""
        if mg and os.path.isdir(mg):
            roots.append(mg)
        return roots

    def resolve_npc_path(path, max_factor=None):
        """Return path to highest-resolution variant (absolute when found under main game)."""
        if max_factor is None:
            max_factor = int(getattr(store, "npc_resolution_max", 2))
        base, ext = os.path.splitext(path)
        for root in _asset_roots():
            for factor in (4, 2):
                if factor <= max_factor:
                    candidate = base + "_" + str(factor) + "x" + ext
                    full = os.path.join(root, candidate)
                    if os.path.exists(full):
                        return _fn_for_renpy(os.path.normpath(full))
        for root in _asset_roots():
            full = os.path.join(root, path)
            if os.path.exists(full):
                return _fn_for_renpy(os.path.normpath(full))
        return _fn_for_renpy(path)

    def npc_texture_zoom_for_resolved(resolved_path):
        scale = float(getattr(store, "npc_texture_scale", 0.5))
        if "_4x" in resolved_path:
            return scale * scale
        return scale

    def npc_texture_zoom_for_path(path):
        return npc_texture_zoom_for_resolved(resolve_npc_path(path))

    def npc_displayable(path):
        resolved = resolve_npc_path(path)
        z = npc_texture_zoom_for_resolved(resolved)
        return Transform(resolved, zoom=z)

    def npc_fullbleed_displayable(path):
        return Transform(
            resolve_npc_path(path),
            fit="cover",
            xysize=(1920, 1080),
            subpixel=True,
        )

    store.resolve_npc_path = resolve_npc_path
    store.npc_texture_zoom_for_resolved = npc_texture_zoom_for_resolved
    store.npc_texture_zoom_for_path = npc_texture_zoom_for_path
    store.npc_displayable = npc_displayable
    store.npc_fullbleed_displayable = npc_fullbleed_displayable
