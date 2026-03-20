# sophie_sprites.rpy — Demo: jog outfit + show_sophie(...) for zoom_cinematic two-shots.
# Sophie assets are native-res only (no _2x/_4x upscale path). Register the resolved file
# as a plain image — skip npc_displayable / npc_texture_scale so she matches her real pixels.

init -1 python:
    def _sophie_reg(tag, path):
        p = store.resolve_npc_path(path)
        renpy.image(tag, (p.replace("\\", "/") if isinstance(p, str) else p))

    _sd = "images/npc/sophie/"
    _sophie_reg("sophie_jog_base_layer", _sd + "sophie_jog_base.webp")
    for _attr, _fn in (
        ("smirk", "sophie_jog_smirk.webp"),
        ("teasing", "sophie_jog_teasing.webp"),
        ("angry", "sophie_jog_angry.webp"),
        ("annoyed", "sophie_jog_annoyed.webp"),
        ("nervous", "sophie_jog_nervous.webp"),
        ("surprised_blush", "sophie_jog_surprised-blush.webp"),
    ):
        _sophie_reg("sophie_jog_" + _attr + "_layer", _sd + _fn)


layeredimage sophie:
    group clothing:
        attribute jog default:
            "sophie_jog_base_layer"
    group expression:
        attribute neutral default:
            Null()
        attribute smirk:
            "sophie_jog_smirk_layer"
        attribute teasing:
            "sophie_jog_teasing_layer"
        attribute angry:
            "sophie_jog_angry_layer"
        attribute annoyed:
            "sophie_jog_annoyed_layer"
        attribute nervous:
            "sophie_jog_nervous_layer"
        attribute surprised_blush:
            "sophie_jog_surprised_blush_layer"


init python:
    _SOPHIE_JOG_EXPR_MAP = {
        "smirk": "smirk",
        "teasing": "teasing",
        "annoyed": "annoyed",
        "angry": "angry",
        "nervous": "nervous",
        "surprised": "surprised_blush",
        "surprised_blush": "surprised_blush",
    }

    def show_sophie(
        expression="",
        position="right",
        clothing="jog",
        at_list=None,
        zorder=11,
        append_breath=True,
    ):
        tags = ["sophie", clothing]

        if expression:
            expr = _SOPHIE_JOG_EXPR_MAP.get(expression, expression)
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

    def hide_sophie():
        renpy.hide("sophie")
