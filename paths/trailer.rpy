label trailer:  #auto-forward below first r, Text speed between T and i
    $ persistent.trailer = False
    $ quick_menu = False
    $ _preferences.afm_enable = True
    pause 0.5
    play sound "audio/train.mp3" loop
    play music "audio/music/chocolate.mp3" loop volume 0.4

    show wrappingCity at center:
        yoffset -50
    show boiSubway
    with truthFade

    m neutral "I've been stressed. Every day feels shorter than the last."

    m "My thoughts are blind to my fleeting soul. Out of sight, out of mind."

    m concern "All I can do is lay down once more and wait for yet another day."

    m "…"

    m neutral "It's not hard keeping this act up. I already know all my lines."

    m concern "But I can't bear treading the beaten path much longer... what can I do?"

    b "It sounds like you made up your mind."

    show boiSubway strain

    b "And I wouldn't dare change it if I were you."

    m "…"

    b "Good luck…"

    pause 1.4

    play sound rain

    scene black

    pause 2.5

    show trailerRain
    show trailerRain2
    show trailerRain3
    with dissolve

    pause 1.0

    show trailerMaria

    pause 2.0

    show trailerLogo at left with logoDissolve

    pause 2.0


    scene bg white with endingFade

    jump splashscreen