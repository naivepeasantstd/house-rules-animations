# diana_sprites.rpy — Demo-only: pink + blue casual (zoom_cinematic). No legacy/couch/robe.

init -1 python:
    def _diana_reg(tag, path):
        renpy.image(tag, store.npc_displayable(path))

    _pink = "images/npc/diana/pink/"
    _diana_reg("diana_pink_base", _pink + "pink_base.webp")
    for _attr, _fn in (
        ("smile", "pink_smile.webp"),
        ("teasewink", "pink_teasing.webp"),
        ("surprised", "pink_surprised.webp"),
        ("pout", "pink_pout.webp"),
        ("nervous", "pink_nervous.webp"),
        ("sad", "pink_sad.webp"),
    ):
        _diana_reg("diana_pink_" + _attr, _pink + _fn)

    _blue = "images/npc/diana/blue/"
    _diana_reg("diana_blue_base", _blue + "blue_base.webp")
    for _attr, _fn in (
        ("smile", "blue_smile.webp"),
        ("teasewink", "blue_smirk.webp"),
        ("surprised", "blue_surprised.webp"),
        ("pout", "blue_pout.webp"),
        ("nervous", "blue_nervous.webp"),
        ("sad", "blue_sad.webp"),
    ):
        _diana_reg("diana_blue_" + _attr, _blue + _fn)


layeredimage diana_casual:
    always:
        "diana_pink_base"
    group expression:
        attribute neutral default:
            Null()
        attribute surprised:
            "diana_pink_surprised"
        attribute nervous:
            "diana_pink_nervous"
        attribute pout:
            "diana_pink_pout"
        attribute teasewink:
            "diana_pink_teasewink"
        attribute sad:
            "diana_pink_sad"
        attribute smile:
            "diana_pink_smile"


layeredimage diana_casual_blueblouse:
    always:
        "diana_blue_base"
    group expression:
        attribute neutral default:
            Null()
        attribute surprised:
            "diana_blue_surprised"
        attribute nervous:
            "diana_blue_nervous"
        attribute pout:
            "diana_blue_pout"
        attribute teasewink:
            "diana_blue_teasewink"
        attribute sad:
            "diana_blue_sad"
        attribute smile:
            "diana_blue_smile"


init python:
    import os

    def _fn_for_renpy(path):
        if not path or not isinstance(path, str):
            return path
        return path.replace("\\", "/")

    def diana_sprite_path(sprite_name):
        res_max = int(getattr(store, "npc_resolution_max", 2))
        root = "images/npc/diana/" + sprite_name
        roots = [config.gamedir]
        mg = getattr(store, "_main_game_assets_root", "") or ""
        if mg and os.path.isdir(mg):
            roots.append(mg)
        for base in roots:
            for ext in (".png", ".webp"):
                for factor in (4, 2):
                    if factor <= res_max:
                        cand = root + "_" + str(factor) + "x" + ext
                        full = os.path.join(base, cand)
                        if os.path.exists(full):
                            return _fn_for_renpy(os.path.normpath(full))
                cand = root + ext
                full = os.path.join(base, cand)
                if os.path.exists(full):
                    return _fn_for_renpy(os.path.normpath(full))
        return None

    def get_diana_idle_sprite(location_override=None):
        return None

    def get_diana_dialogue_sprite(expression=""):
        return None

    _DIANA_EXPR_MAP = {
        "happy": "smile",
        "surprised": "surprised",
        "blushing": "nervous",
        "blush": "nervous",
        "flirty": "teasewink",
    }

    _DIANA_CASUAL_EXPR_MAP = {
        "happy": "smile",
        "surprised": "surprised",
        "surprise": "surprised",
        "blushing": "nervous",
        "blush": "nervous",
        "flirty": "teasewink",
    }

    def diana_layered_base_for_outfit(outfit):
        if outfit == "blueblouse":
            return "diana_casual_blueblouse"
        if outfit == "casual" and getattr(store, "diana_outfit", "casual") == "blueblouse":
            return "diana_casual_blueblouse"
        if outfit == "base":
            return "diana_casual_blueblouse" if getattr(store, "diana_outfit", "casual") == "blueblouse" else "diana_casual"
        return "diana_casual"

    def _diana_casual_layer_showing():
        """renpy.showing('diana_casual_blueblouse') is False when sprite is shown as 'base expression' pairs."""
        if renpy.showing("diana_casual") or renpy.showing("diana_casual_blueblouse"):
            return True
        for _base in ("diana_casual", "diana_casual_blueblouse"):
            for _a in ("neutral", "surprised", "nervous", "pout", "teasewink", "sad", "smile"):
                if renpy.showing(_base + " " + _a):
                    return True
        return False

    def _diana_speak_callback(event, interact=True, **kwargs):
        if event == "begin":
            if getattr(store, "_diana_cg_only", False):
                return
            if not _diana_casual_layer_showing():
                sprite = diana_layered_base_for_outfit("base")
                renpy.show(sprite, at_list=[anim_enter_right, sprite_idle_breath], zorder=10)

    def show_diana(expression="", position="right", outfit="base", at_list=None, zorder=10, append_breath=True):
        base_tag = diana_layered_base_for_outfit(outfit)
        tags = [base_tag]
        expr_map = _DIANA_CASUAL_EXPR_MAP if base_tag.startswith("diana_casual") else _DIANA_EXPR_MAP

        if expression:
            expr = expr_map.get(expression, expression)
            tags.append(expr)

        if at_list is None or not at_list:
            at_list = [anim_dialogue_right, sprite_idle_breath]
            if position == "center":
                at_list = [anim_dialogue_center, sprite_idle_breath]
            elif position == "left":
                at_list = [anim_dialogue_left, sprite_idle_breath]
        elif append_breath:
            breath = getattr(store, "sprite_idle_breath", None)
            if breath is not None:
                at_list = list(at_list) + [breath]
        else:
            at_list = list(at_list)

        renpy.show(" ".join(tags), at_list=at_list, zorder=zorder)

    def hide_diana():
        renpy.hide("diana")
        renpy.hide("diana_casual")
        renpy.hide("diana_casual_blueblouse")
