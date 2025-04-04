image splash = "images/logo Meow_Meow_Meadows_Transparent.png"

label splashscreen:
    scene bg white
    with Pause(1)

    show splash with dissolve

    #stop music fadeout 2.0

    pause 2.0

    scene bg white with dissolve
    with Pause(1.5)

    return