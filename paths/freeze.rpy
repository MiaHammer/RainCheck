label freeze_ending:

    pause 1.0

    t "(0:20 - Desk)"
    
    scene streetwindow figurehere rainon

    m concern "I need to pay close attention to their actions so I’m ready for anything."
    m concern "I’m not sure what exactly I can do when I see them moving, but at least I’ll be aware of it and my instincts will guide me to safety."
    m queiss "… Or something like that."
    m concern "…"

    m queiss "{color=#ff0d21}They{/color} haven’t moved an inch yet. Maybe I really am overthinking this, but it’s not like I can turn away now."

    m concern "{color=#ff0d21}They{/color}’re like a giant lizard glued to the wall for hours doing absolutely nothing until it’s their time to strike."

    scene cg gecko with hypothetical_fade

    m concern "Crawling behind the curtains at night. Hiding behind my favorite book on the shelf, just out of sight."
    m concern "I cannot stand being in the vicinity of those creatures. They completely break the peace and any illusion of personal space by just existing, with me knowing they might, or might not, still be there."
    m concern "And the idea that they could just jump on top of me at any second, from outside my field of view, if they so desired?"
    m concern "It is pure agony, and makes it so hard for me to sleep at night, if I ever catch a glimpse of them."

    scene black
    show cg sidewalk at center:
        yoffset - 120
    show theFigure at center:
        yoffset - 120
    show rain
    show framey sidewalkwindowframe
    with hypothetical_fade

    m concern "This feels similar, yet much worse."

    stop music

    hide theFigure
    show cg sidewalk at sshake:
        xoffset + 320
        yoffset + 120
    play audio "audio/shakesound.ogg"

    m shock "!"

    play music "audio/music/Out_Of_The_Window.mp3"

    m shock "{color=#ff0d21}They{/color} jumped my fence, stepped into the front garden and quickly went for the front door."
    m concern "…"

    play sound "door.ogg"
    
    m concern "I can hear the front door opening up."
    m concern "Whoever that is, {color=#ff0d21}They{/color}'re now here with me."
    m shock "what do I do what do i do what do i do!?"
    m concern "…"
    m concern "I need to get the fuck out of here, I could probably swerve around {color=#ff0d21}Them{/color} by going through the window."
    m concern "Right! The police also said I should call again if the situation changes!"
    m concern "Where’s my phone? I need to find it fast."
    m concern "…"
    m concern "Got it."
    m concern "Time to go."

    play sound "grass_jump.mp3"

    ##################################################
    scene black with forestFade # running scene later?
    ##################################################

    pause 0.5

    t "(??:?? - ?????)"

    play sound "grass_run.mp3" loop

    m neutral "…"
    m concern "I’ve been running for so long."
    m concern "My ribs feel like they’re cutting into my lungs. My heart aches."
    m concern "I’m nauseous, nothing in my body is working right."
    m concern "I hope {color=#ff0d21}They{/color} lost track of me."
    m neutral "…"
    stop sound fadeout 0.5
    m neutral "I have to call the police. I’ll take a break from running now."

    scene black

    pause 0.5

    m queiss "Did… I drop my phone?"
    m concern "No, there’s no way, I was gripping it tightly."
    m concern "Where is it? And where am I now?"

    scene black
    show cg forestcrazy with dissolve

    m "I can barely see anything anywhere I look."
    m "This forest is pitch black. The foliage is so dense I can rarely catch glimpses of the sky above."
    m "How the hell do I get out of here?"

    play sound "audio/camera.mp3"
    pause 0.5

    show cg mariaphoto1

    m "!!!!!"
    m "Is someone here?!"

    play sound "audio/camera.mp3"
    pause 0.5

    show cg mariaphoto2

    m "Wh-?"

    play sound "audio/camera.mp3"
    pause 0.5
    stop music

    hide cg

    pause 4.0

    t "(??:?? - ?????)"

    play sound "audio/train.mp3" loop
    queue ending_music ["audio/music/chocolate.mp3", "audio/music/chocolate.mp3", "audio/music/chocolate.mp3"] volume 0.4

    show wrappingCity at center:
        yoffset -50
    show boiSubway
    with forestBoiFade

    b "…"
    b "Ah, hello there."
    show boiSubway strain
    b "I see you've decided to pick and choose the right time to act, believing a specific one would come."
    m concern "You really don’t get it, huh?"
    show boiSubway brain
    b "…?"
    m concern "If I knew beforehand what I know now, I would make the same mistakes."
    m crying "I would make them over and over and over and over and over again."
    m crying "I’m doing my best. All the time. At everything."
    m crying "It’s not on me to change."
    show boiSubway refrain
    b "…"
    show boiSubway brain
    m crying "I’m so tired of always having to deal with this bullshit in my head."
    m crying "You win, okay? Please, just leave me be for now."
    m crying "I give up this time."
    show boiSubway strain
    b "…"
    show boiSubway sprain
    b "Understood."

    scene black with forestFade

    pause 1.0

    if not achievement.has("choked") and not achievement.has("stalked") and not achievement.has("decapitated"):
        "Use ctrl or tab to skip through text"
        pause 1.0

    #$ persistent.stalked = True
    $ achievement.grant("stalked")
    $ achievement.sync()
    $ MainMenu(confirm=False)()

    '''
    scene cg maria head on 1

    m "I might know why."
    m "But…"
    m "I'd rather not think about this right now."
    m "Just…"
    m "Leave me alone."

    play sound "audio/camera.mp3"
    pause 0.5

    show cg maria head on 2

    m "Get away from me!"

    play sound "audio/camera.mp3"
    pause 0.5

    show cg maria head on 3

    m "Get OUT!"

    play sound "audio/camera.mp3"
    pause 0.5

    show cg maria head on 4

    m "…"

    scene black with inRoomFlash

    stop music

    pause 2.0

    #return
    '''