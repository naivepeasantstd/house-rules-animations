# White splash — Naive Peasant Studios (before main menu)

image splash_white = Solid("#ffffff")
image naive_peasant_logo = "gui/naive_peasant_logo.png"

transform splash_logo_placed:
    subpixel True
    xalign 0.5
    yalign 0.40
    zoom 0.72

screen naive_peasant_splash_title():
    zorder 100
    vbox:
        xalign 0.5
        yalign 0.80
        spacing 6
        text _("Naive Peasant Studios"):
            xalign 0.5
            size 44
            color "#141414"
            bold True
        text _("Animation tooling · House Rules"):
            xalign 0.5
            size 22
            color "#5a5a5a"


label splashscreen:
    scene splash_white
    show naive_peasant_logo at splash_logo_placed
    with Dissolve(0.45)
    pause 0.35
    show screen naive_peasant_splash_title
    with Dissolve(0.35)
    pause 2.75
    hide screen naive_peasant_splash_title
    hide naive_peasant_logo
    with Dissolve(0.35)
    return
