# demo_zoom_cinematic.rpy — Animation showcase: breathing, zoom beats, body language (House Rules tech demo)
# Main menu → start, or renpy.call("zoom_cinematic")

label zoom_cinematic:
    $ _diana_cg_only = False

    scene black
    show expression bg_displayable("images/bg/home/living_room/living_room.webp") as bg_main zorder 0
    with Dissolve(0.6)

    $ diana_outfit = "blueblouse"

    # ═══ Prologue ═══
    $ show_diana("teasewink", position="center", outfit="casual", at_list=[anim_dialogue_center, sprite_idle_breath])
    diana "Welcome to the build diary.{w} I'm the tour guide.{w} Try not to look like you're hiding another tab."
    diana "Naive Peasant geeks out on motion:{w} breathing loops,{w} camera beats,{w} little moves that sell guilt."
    diana "I'll drop the Ren'Py names.{w} You laugh where it's filthy.{w} Fair?"

    # ═══ Breathing — sprite stack ═══
    $ hide_diana()
    with None
    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, sprite_idle_breath])
    diana "This rise and fall is {i}sprite_idle_breath{/i}.{w} Keeps me from looking like a JPG with a grudge."
    diana "You stack it {i}after{/i} {i}anim_dialogue_center{/i} — position first, breath second.{w} That's the recipe."
    diana "Some zoom rigs already loop breath inside them.{w} Then you pass {i}append_breath=False{/i} on {i}show_diana{/i}."
    diana "Otherwise I sound like I ran upstairs.{w} For {i}every{/i} line.{w} Your father never complained about stamina — don't start."

    # ═══ Act A — blue blouse: zoom vocabulary ═══
    $ show_diana("neutral", position="center", outfit="casual", at_list=[anim_dialogue_center, sprite_idle_breath])
    diana "Blue blouse,{w} serious voice.{w} Pretend I'm still the adult in the room."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") at anim_bg_depth_breath_lb_center(1.58, 1.0, 1.5, 1.5, blur_k=28.0) as bg_main zorder 0
    $ show_diana("neutral", position="center", outfit="casual", at_list=anim_sprite_zoom_beat(
        anim_dialogue_center,
        focal_y=None,
        zoom=1.58,
        t_zoom=1.0,
        motion="none",
        revert=True,
        hold_seconds=1.5,
        revert_duration=1.5,
    ), append_breath=False)
    diana "Uniform zoom — {i}focal_y{/i} off.{w} Background and I scale together.{w} Very 'sit down, we need to talk'."
    diana "No clever anchor.{w} Just intimacy with extra legroom."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") at anim_bg_depth_breath_lb_center(1.58, 1.0, 1.5, 1.5, blur_k=28.0) as bg_main zorder 0
    $ show_diana("smile", position="center", outfit="casual", at_list=anim_sprite_zoom_beat(
        anim_dialogue_center,
        focal_y=0.35,
        zoom=1.58,
        t_zoom=1.0,
        motion="none",
        revert=True,
        hold_seconds=1.5,
        revert_duration=1.5,
        fy_after=0.1,
    ), append_breath=False)
    diana "Focal zoom — {i}focal_y{/i} on.{w} The frame re-anchors so one band of the picture stays 'the point'."
    diana "Docs say faces.{w} Physics says other things drift into prime real estate.{w} Eyes up,{w} sweetheart.{w} I'm still your father's wife in this household."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") at anim_bg_depth_breath_lb_center(1.58, 1.0, 1.5, 1.5, blur_k=28.0) as bg_main zorder 0
    $ show_diana("teasewink", position="center", outfit="casual", at_list=anim_sprite_zoom_beat(
        anim_dialogue_center,
        focal_y=0.35,
        zoom=1.58,
        t_zoom=1.0,
        motion="wiggle",
        revert=True,
        hold_seconds=1.5,
        revert_duration=1.5,
        fy_after=0.1,
    ), append_breath=False)
    diana "Now the same beat plus a wiggle.{w} Cute motion,{w} sharp teeth.{w} The smile that says you're not off the hook."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") at anim_bg_depth_breath_lb_center(1.58, 1.0, 1.5, 1.5, blur_k=28.0) as bg_main zorder 0
    $ show_diana("surprised", position="center", outfit="casual", at_list=anim_sprite_zoom_beat(
        anim_dialogue_center,
        focal_y=0.35,
        zoom=1.58,
        t_zoom=1.0,
        motion="shake",
        revert=True,
        hold_seconds=1.5,
        revert_duration=1.5,
        fy_after=0.1,
    ), append_breath=False)
    diana "Shake — panic,{w} bad push notification,{w} or your stepsister remembering she despises you.{w} Same jitter."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") at anim_bg_depth_breath_lb_center(1.58, 1.0, 1.5, 1.5, blur_k=28.0) as bg_main zorder 0
    $ show_diana("pout", position="center", outfit="casual", at_list=anim_sprite_zoom_beat(
        anim_dialogue_center,
        focal_y=0.35,
        zoom=1.58,
        t_zoom=1.0,
        motion="punch",
        revert=True,
        hold_seconds=1.5,
        revert_duration=1.5,
        fy_after=0.1,
    ), append_breath=False)
    diana "Punch zoom — one rude dip.{w} Juvenile,{w} horny energy,{w} over in a heartbeat."
    diana "Like that compliment you shouldn't have said out loud.{w} I heard it anyway."

    show expression bg_displayable("images/bg/home/living_room/living_room.webp") as bg_main zorder 0
    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, sprite_idle_breath])
    diana "All of that was {i}anim_sprite_zoom_beat{/i}:{w} zoom in,{w} hold,{w} optional wiggle or shake or punch,{w} zoom out,{w} idle breath if you want it."
    diana "The rest of {i}transforms.rpy{/i} is pieces.{w} That function stacks them so writers don't cry."
    diana "I read your repo before I read your mail.{w} House rules."

    $ hide_diana()
    with Dissolve(0.35)

    # ═══ Act B — pink casual: body beats ═══
    $ diana_outfit = "casual"

    $ show_diana("teasewink", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_hop])
    diana "{i}anim_hop{/i} — quick bounce.{w} For 'I'm delighted' without meaning it.{w} Or meaning it too much."

    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_hop_down])
    diana "{i}anim_hop_down{/i} — same idea,{w} slower,{w} deeper.{w} When the sprite sits low and we still want heat without clipping my hem."

    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_wiggle])
    diana "{i}anim_wiggle{/i} — side-to-side tease.{w} Sophie weaponizes it.{w} You pretend you don't notice."

    $ show_diana("nervous", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_nervous])
    diana "{i}anim_nervous{/i} — tiny vibration loop.{w} Court dates,{w} chemistry,{w} same hand on the knee under the table."

    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_excited])
    diana "{i}anim_excited{/i} — double bounce.{w} Good news that could ruin you.{w} Smile like you asked for it."

    $ show_diana("sad", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_sigh])
    diana "{i}anim_sigh{/i} — lets gravity win for a second.{w} The sound of 'we shouldn't'{w} with nobody leaving."

    $ show_diana("surprised", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_flinch])
    diana "{i}anim_flinch{/i} — pulls back sharp.{w} Wrong name,{w} right guilt.{w} Act innocent."

    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_pulse])
    diana "{i}anim_pulse{/i} — one zoom hiccup.{w} Emphasis without jumping you.{w} ...Unless the next label says otherwise."

    $ show_diana("teasewink", position="center", outfit="casual", at_list=[anim_dialogue_center, anim_nod])
    diana "{i}anim_nod{/i} — agrees with whatever keeps the peace.{w} Nod if you follow Naive Peasant.{w} I'll count."

    # ═══ Act C — two-shot ═══
    show expression bg_displayable("images/bg/home/living_room/living_room.webp") as bg_main zorder 0
    $ show_diana("smile", position="right", outfit="casual", at_list=[anim_dialogue_right, sprite_idle_breath], zorder=10)
    $ show_sophie("teasing", position="left", at_list=[anim_dialogue_left, sprite_idle_breath], zorder=11)
    diana "Two women,{w} one doorway,{w} ratings board twitching.{w} Welcome to moving day."
    diana "I'm scaled,{w} sharp,{w} a little guilty on purpose.{w} Sophie's native-res — honest pixels.{w} Don't roast her file size.{w} She's family."

    $ show_sophie("annoyed", position="left", at_list=[anim_dialogue_left, sprite_idle_breath], zorder=11)
    sophie "I'm not blurry.{w} You're just over-compressed and coping."
    sophie "I hauled a box.{w} Put {i}that{/i} in the changelog."

    $ show_diana("teasewink", position="right", outfit="casual", at_list=[anim_dialogue_right, sprite_idle_breath], zorder=10)
    $ show_sophie("smirk", position="left", at_list=[anim_dialogue_left, anim_hop], append_breath=False, zorder=11)
    sophie "Say thank you loud,{w} [mc_name].{w} I want the hallway to know you're domestically trained."

    $ show_sophie("teasing", position="left", at_list=[anim_dialogue_left, sprite_idle_breath], zorder=11)
    $ show_diana("pout", position="right", outfit="casual", at_list=[anim_dialogue_right, anim_wiggle], append_breath=False, zorder=10)
    diana "Different loops,{w} same shot.{w} That's how we avoid a slapfest and still feel like one could start."

    $ hide_sophie()
    with None
    $ show_diana("smile", position="center", outfit="casual", at_list=[anim_dialogue_center, sprite_idle_breath])
    diana "More toys live in {i}transforms.rpy{/i}.{w} Parallax,{w} couch slides,{w} night grades.{w} Go bruise your eyes."
    diana "House Rules isn't out yet.{w} Stay tuned.{w} When it drops, you'll swear the easing curves flirted first."
    diana "Demo over.{w} Alt-tab before someone mislabels your hobbies.{w} Shoo."

    $ hide_diana()
    with Dissolve(0.4)

    scene black
    with Dissolve(0.5)

    return
