label clicker_ending:

    pause 1.0

    t "(0:20 - Desk)"

    scene bg outside
    show theFigure at top
    show rain
    show bg2 onlydesks

    mm "I stood frozen for a moment, panic grasping at my throat."
    m phone "Right, I gotta get myself on lockdown here now Ann. ttyl"

    scene black
    show bg stairs at sshake
    play audio "audio/shakesound.ogg"

    mm "I rushed from room to room, in the dark, checking every door, every window, every possible entrance into the house."
    mm "At every corner my mind produced violent scenarios, ways in which I could get caught, hit, slashed, shot, tortured on the spot."
    mm "At some point, I got into a trance, time was not a variable for me, I was checking locks on auto-pilot, while trying to vaguely stay in silence with every move."
    mm "Every noise felt like the last."
    mm "Eventually I locked down every possible entrance, and went back to my desk."
    
    scene black

    pause 0.5

    t "(0:30 - Desk)"

    scene bg desk
    
    mm "Coming back to my desk, I slowly veered towards the window and reluctantly peered through it."
    m concern "Are {color=#ff0d21}They{/color} still there…?"

    scene streetwindow rainon

    m concern "…"
    m queiss "Mmm, guess not."
    m concern "I’m… not sure if that’s better or worse."
    m neutral "But I’ve done everything I could."
    m concern "Goddamnit, my adrenaline is so high, I don’t think I can sleep until morning."

    m concern "…"
    m neutral "I’m gonna lay down for a bit."
    
    stop music
    stop sound

    scene black

    pause 0.5

    t "(1:00 - Laying down)"

    #scene bg desk #bed?

    play sound "audio/ticking-clock.mp3" loop

    mm "While laying down, I tried to put my head back into place."
    mm "I tried to process it all."
    
    menu:
        "Check your phone":
            $ decision=0
            jump phone_checked
        
        "Look at picture frame":
            $ decision=1
            jump frame_pictured
    
    


label phone_checked:
    mm "I grabbed my phone, there were multiple message notifications from Annie asking if I was safe."
    mm "The most recent one was from 20 minutes ago."
    a phone "Maria, is everything alright? Please, call me again if you can."
    m phone "I think I’m ok, ty."
    m phone "I got all my doors and windows locked up tight. I’ll just try to calm down right now."
    a phone "Okay, call me tomorrow then?"
    m phone "Okay"
    mm "I put my phone down."

    pause 1.0

    if decision == 0:
        jump frame_pictured
    else:
        jump continued_clicking



label frame_pictured:
    mm "I turn my head to the picture frame beside my bed."
    mm "…"
    mm "This picture reminds me of a distant, cherished memory."
    scene cg ninjas with hypothetical_fade

    mm "A memory of the time when I took a trip, and with nothing to do in the back seat of the car, I looked out the window and imagined multiple superhuman Ninjas parkouring through the landscape."
    mm "In my mind, they did flips, ran on electricity wires, rolled under pedestrians, climbed trees, went up and down houses…"
    mm "And then they stopped, took rests and did cool poses whenever the car stopped at a red light."

    scene black with hypothetical_fade

    m neutral "..."
    m neutral "I miss those family road trips."
    m concern "I miss the simpler times."
    m neutral "..."

    pause 1.0

    if decision == 1:
        jump phone_checked
    else:
        jump continued_clicking



label continued_clicking:
    m neutral "I need another distraction."
    m neutral "I think I know just the one!"

    stop sound

    scene black

    pause 0.5

    t "(1:30 - Desk)"

    scene galDesk deskmariacow

    play sound "audio/rain.mp3" loop

    m "I love this game."
    m "It always picks me up when I’m down, no matter the occasion."
    m "I’ve been meaning to replay it, but I’ve been waiting for the right time."
    m "That time is now!"


    scene black with clickerFade

    $ renpy.block_rollback()
    call screen cow_clicker(True)


label clicker_done:
    $ renpy.block_rollback()

    play sound "audio/raven-call.mp3"

    pause 4.0

    stop sound

    pause 1.0

    play audio "audio/impact.mp3"

    scene cg strangling hands

    play sound "audio/computer-hum.mp3" fadein 0.5 loop

    mm "…"

    pause 2.0
    
    scene black
    stop sound

    pause 2.0

    queue ending_music ["audio/music/rantan.mp3", "audio/music/rantan.mp3", "audio/music/rantan.mp3"]

    mm "i’m a cow grazing on a pasture"
    mm "look left look right"
    mm "no predators only grass"
    mm "rumination"
    mm "everything is right with the world"
    mm "as i chew on the cud"
    mm "i hear a strange sound above me"

    scene cg boialien

    pause 1.0

    mm "suddenly i'm bathed in a shower of light"
    mm "i sense myself weightless as {color=#ff0d21}They{/color} lift me off the ground"


    pause 2.0

    scene black with hypothetical_fade

    pause 2.0

    if not achievement.has("choked") and not achievement.has("stalked") and not achievement.has("decapitated"):
        "Use ctrl or tab to skip through text"

    #$ persistent.choked = True
    $ achievement.grant("choked")
    $ achievement.sync()
    $ MainMenu(confirm=False)()
    #return