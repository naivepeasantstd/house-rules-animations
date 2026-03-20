# core/systems/transforms.rpy — Animation demo: zoom pipeline + beats used by zoom_cinematic + diana_sprites.
# Full-game transforms live in thisboringlife; this copy is trimmed to what the standalone demo loads.

init -1 python:
    def whisper_tag(tag, argument, contents):
        rv = []
        rv.append((renpy.TEXT_TAG, "size=-4"))
        rv.append((renpy.TEXT_TAG, "i"))
        rv.append((renpy.TEXT_TAG, "color=#aaa"))
        rv += contents
        rv.append((renpy.TEXT_TAG, "/color"))
        rv.append((renpy.TEXT_TAG, "/i"))
        rv.append((renpy.TEXT_TAG, "/size"))
        return rv

    config.custom_text_tags["whisper"] = whisper_tag


transform sprite_idle_breath:
    subpixel True
    yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_dialogue_right:
    subpixel True
    xoffset 0 yoffset 0 alpha 1.0
    xalign 0.75 yalign 0.0 zoom 1.0

transform anim_dialogue_center:
    subpixel True
    xoffset 0 yoffset 0 alpha 1.0
    xalign 0.5 yalign 0.0 zoom 1.0

transform anim_dialogue_left:
    subpixel True
    xoffset 0 yoffset 0 alpha 1.0
    xalign 0.25 yalign 0.0 zoom 1.0

transform anim_enter_right(t=0.4, dist=80):
    subpixel True
    xalign 0.75 yalign 0.0 zoom 1.0
    alpha 0.0 xoffset dist
    easein t alpha 1.0 xoffset 0


transform anim_hop:
    subpixel True
    easein 0.12 yoffset 18
    easeout 0.12 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_hop_down:
    subpixel True
    easein 0.28 yoffset 20
    easeout 0.28 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_wiggle:
    subpixel True
    easein 0.08 xoffset 12
    easeout 0.08 xoffset -12
    easein 0.08 xoffset 12
    easeout 0.08 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat



transform anim_excited:
    subpixel True
    easein 0.10 yoffset 18
    easeout 0.10 yoffset 0
    easein 0.10 yoffset 12
    easeout 0.10 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_nervous:
    subpixel True
    linear 0.04 xoffset 3
    linear 0.04 xoffset -3
    linear 0.04 xoffset 4
    linear 0.04 xoffset -2
    linear 0.04 xoffset 3
    linear 0.04 xoffset -3
    linear 0.04 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_flinch:
    subpixel True
    easein 0.08 xoffset -25 yoffset 8
    easeout 0.20 xoffset 0 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sigh:
    subpixel True
    ease 0.3 yoffset 10
    ease 0.4 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_nod:
    subpixel True
    easein 0.12 yoffset 10
    easeout 0.18 yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_pulse:
    subpixel True
    easein 0.12 zoom 1.06
    easeout 0.20 zoom 1.0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat


transform anim_sprite_zoom_hold(z=1.14, t=0.55, stay=0.0):
    subpixel True
    zoom 1.0
    ease t zoom z
    pause stay

transform anim_sprite_zoom_hold_lb(z=1.14, t=0.55, stay=0.0, t_unzoom=-1.0):
    subpixel True
    zoom 1.0
    ease t zoom z
    pause stay
    ease (t_unzoom if t_unzoom >= 0 else t) zoom 1.0

transform anim_sprite_zoom_then_breath(z=1.14, t=0.55, stay=0.0):
    subpixel True
    zoom 1.0
    ease t zoom z
    pause stay
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_breath_lb(z=1.14, t=0.55, stay=0.0, t_unzoom=-1.0):
    subpixel True
    zoom 1.0
    ease t zoom z
    pause stay
    ease (t_unzoom if t_unzoom >= 0 else t) zoom 1.0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_wiggle(z=1.14, t_zoom=0.55, stay=0.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    easein 0.08 xoffset 12
    easeout 0.08 xoffset -12
    easein 0.08 xoffset 12
    easeout 0.08 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_wiggle_lb(z=1.14, t_zoom=0.55, stay=0.0, t_unzoom=-1.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    ease (t_unzoom if t_unzoom >= 0 else t_zoom) zoom 1.0
    easein 0.08 xoffset 12
    easeout 0.08 xoffset -12
    easein 0.08 xoffset 12
    easeout 0.08 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_shake(z=1.14, t_zoom=0.55, px=10, step=0.055, stay=0.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    easein step xoffset px
    easein step xoffset -px
    easein step xoffset px
    easein step xoffset -px
    easeout step xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_shake_lb(z=1.14, t_zoom=0.55, px=10, step=0.055, stay=0.0, t_unzoom=-1.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    ease (t_unzoom if t_unzoom >= 0 else t_zoom) zoom 1.0
    easein step xoffset px
    easein step xoffset -px
    easein step xoffset px
    easein step xoffset -px
    easeout step xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_punch(z=1.14, t_zoom=0.55, dip=22, t_in=0.06, t_out=0.18, stay=0.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    easein t_in yoffset dip
    easeout t_out yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_then_punch_lb(z=1.14, t_zoom=0.55, dip=22, t_in=0.06, t_out=0.18, stay=0.0, t_unzoom=-1.0):
    subpixel True
    zoom 1.0
    ease t_zoom zoom z
    pause stay
    ease (t_unzoom if t_unzoom >= 0 else t_zoom) zoom 1.0
    easein t_in yoffset dip
    easeout t_out yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat


transform anim_sprite_zoom_y_hold(z=1.14, fy=0.28, t=0.55, stay=0.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t zoom z
        block:
            pause (fy_after * t)
            ease ((1.0 - fy_after) * t) yanchor fy
    pause stay

transform anim_sprite_zoom_y_hold_lb(z=1.14, fy=0.28, t=0.55, stay=0.0, t_unzoom=-1.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t zoom z
        block:
            pause (fy_after * t)
            ease ((1.0 - fy_after) * t) yanchor fy
    pause stay
    ease ((t_unzoom if t_unzoom >= 0 else t) * 0.4) yanchor 0
    ease ((t_unzoom if t_unzoom >= 0 else t) * 0.6) zoom 1.0

transform anim_sprite_zoom_y_then_breath(z=1.14, fy=0.28, t=0.55, stay=0.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t zoom z
        block:
            pause (fy_after * t)
            ease ((1.0 - fy_after) * t) yanchor fy
    pause stay
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_breath_lb(z=1.14, fy=0.28, t=0.55, stay=0.0, t_unzoom=-1.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t zoom z
        block:
            pause (fy_after * t)
            ease ((1.0 - fy_after) * t) yanchor fy
    pause stay
    ease ((t_unzoom if t_unzoom >= 0 else t) * 0.4) yanchor 0
    ease ((t_unzoom if t_unzoom >= 0 else t) * 0.6) zoom 1.0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_wiggle(z=1.14, fy=0.28, t_zoom=0.55, stay=0.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    easein 0.08 xoffset 12
    easeout 0.08 xoffset -12
    easein 0.08 xoffset 12
    easeout 0.08 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_wiggle_lb(z=1.14, fy=0.28, t_zoom=0.55, stay=0.0, t_unzoom=-1.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.4) yanchor 0
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.6) zoom 1.0
    easein 0.08 xoffset 12
    easeout 0.08 xoffset -12
    easein 0.08 xoffset 12
    easeout 0.08 xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_shake(z=1.14, fy=0.28, t_zoom=0.55, px=10, step=0.055, stay=0.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    easein step xoffset px
    easein step xoffset -px
    easein step xoffset px
    easein step xoffset -px
    easeout step xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_shake_lb(z=1.14, fy=0.28, t_zoom=0.55, px=10, step=0.055, stay=0.0, t_unzoom=-1.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.4) yanchor 0
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.6) zoom 1.0
    easein step xoffset px
    easein step xoffset -px
    easein step xoffset px
    easein step xoffset -px
    easeout step xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_punch(z=1.14, fy=0.28, t_zoom=0.55, dip=22, t_in=0.06, t_out=0.18, stay=0.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    easein t_in yoffset dip
    easeout t_out yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_sprite_zoom_y_then_punch_lb(z=1.14, fy=0.28, t_zoom=0.55, dip=22, t_in=0.06, t_out=0.18, stay=0.0, t_unzoom=-1.0, fy_after=0.1):
    subpixel True
    zoom 1.0
    xanchor 0.5
    yanchor 0
    parallel:
        ease t_zoom zoom z
        block:
            pause (fy_after * t_zoom)
            ease ((1.0 - fy_after) * t_zoom) yanchor fy
    pause stay
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.4) yanchor 0
    ease ((t_unzoom if t_unzoom >= 0 else t_zoom) * 0.6) zoom 1.0
    easein t_in yoffset dip
    easeout t_out yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat


transform anim_bg_depth_breath_lb_center(z=1.14, t_in=0.55, stay=0.0, t_unzoom=-1.0, blur_k=24.0):
    subpixel True
    xalign 0.5 yalign 0.5
    xanchor 0.5
    yanchor 0.5
    zoom 1.0
    blur 0.0
    parallel:
        ease t_in zoom z
        ease t_in blur ((z - 1.0) * blur_k)
    pause stay
    parallel:
        ease (t_unzoom if t_unzoom >= 0 else t_in) blur 0.0
        ease (t_unzoom if t_unzoom >= 0 else t_in) zoom 1.0


transform anim_shake_sprite(px=10, step=0.055):
    subpixel True
    easein step xoffset px
    easein step xoffset -px
    easein step xoffset px
    easein step xoffset -px
    easeout step xoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat

transform anim_punch_sprite(dip=22, t_in=0.06, t_out=0.18):
    subpixel True
    easein t_in yoffset dip
    easeout t_out yoffset 0
    block:
        ease 1.8 yoffset 5
        ease 1.8 yoffset 0
        repeat


# Composed zoom beat — needs all anim_sprite_zoom_* transforms above.

init 1 python:
    def anim_sprite_zoom_beat(
        position,
        focal_x=0.5,
        focal_y=None,
        zoom=1.14,
        t_zoom=0.55,
        zoom_duration=None,
        motion="wiggle",
        breath=True,
        use_anchor=True,
        shake_px=10,
        shake_step=0.055,
        punch_dip=22,
        punch_t_in=0.06,
        punch_t_out=0.18,
        stay=0.0,
        hold_seconds=None,
        loop_back=False,
        revert=None,
        t_unzoom=None,
        revert_duration=None,
        fy_after=0.1,
    ):
        if zoom_duration is not None:
            t_zoom = float(zoom_duration)
        if hold_seconds is not None:
            stay = float(hold_seconds)
        if revert is not None:
            loop_back = bool(revert)
        if revert_duration is not None:
            t_unzoom = float(revert_duration)
        st = renpy.store
        m = (motion or "none").lower().strip()
        yf = focal_y
        tu = -1.0 if t_unzoom is None else float(t_unzoom)
        fa = max(0.0, min(0.999, float(fy_after)))
        if yf is not None:
            if m == "wiggle":
                beat = (
                    st.anim_sprite_zoom_y_then_wiggle_lb(zoom, yf, t_zoom, stay, tu, fa)
                    if loop_back
                    else st.anim_sprite_zoom_y_then_wiggle(zoom, yf, t_zoom, stay, fa)
                )
            elif m == "shake":
                beat = (
                    st.anim_sprite_zoom_y_then_shake_lb(zoom, yf, t_zoom, shake_px, shake_step, stay, tu, fa)
                    if loop_back
                    else st.anim_sprite_zoom_y_then_shake(zoom, yf, t_zoom, shake_px, shake_step, stay, fa)
                )
            elif m == "punch":
                beat = (
                    st.anim_sprite_zoom_y_then_punch_lb(zoom, yf, t_zoom, punch_dip, punch_t_in, punch_t_out, stay, tu, fa)
                    if loop_back
                    else st.anim_sprite_zoom_y_then_punch(zoom, yf, t_zoom, punch_dip, punch_t_in, punch_t_out, stay, fa)
                )
            elif breath:
                beat = (
                    st.anim_sprite_zoom_y_then_breath_lb(zoom, yf, t_zoom, stay, tu, fa)
                    if loop_back
                    else st.anim_sprite_zoom_y_then_breath(zoom, yf, t_zoom, stay, fa)
                )
            else:
                beat = (
                    st.anim_sprite_zoom_y_hold_lb(zoom, yf, t_zoom, stay, tu, fa)
                    if loop_back
                    else st.anim_sprite_zoom_y_hold(zoom, yf, t_zoom, stay, fa)
                )
        else:
            if m == "wiggle":
                beat = (
                    st.anim_sprite_zoom_then_wiggle_lb(zoom, t_zoom, stay, tu)
                    if loop_back
                    else st.anim_sprite_zoom_then_wiggle(zoom, t_zoom, stay)
                )
            elif m == "shake":
                beat = (
                    st.anim_sprite_zoom_then_shake_lb(zoom, t_zoom, shake_px, shake_step, stay, tu)
                    if loop_back
                    else st.anim_sprite_zoom_then_shake(zoom, t_zoom, shake_px, shake_step, stay)
                )
            elif m == "punch":
                beat = (
                    st.anim_sprite_zoom_then_punch_lb(zoom, t_zoom, punch_dip, punch_t_in, punch_t_out, stay, tu)
                    if loop_back
                    else st.anim_sprite_zoom_then_punch(zoom, t_zoom, punch_dip, punch_t_in, punch_t_out, stay)
                )
            elif breath:
                beat = (
                    st.anim_sprite_zoom_then_breath_lb(zoom, t_zoom, stay, tu)
                    if loop_back
                    else st.anim_sprite_zoom_then_breath(zoom, t_zoom, stay)
                )
            else:
                beat = (
                    st.anim_sprite_zoom_hold_lb(zoom, t_zoom, stay, tu)
                    if loop_back
                    else st.anim_sprite_zoom_hold(zoom, t_zoom, stay)
                )
        return [position, beat]
