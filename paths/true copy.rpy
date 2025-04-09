label true_ending_copy:
    
    stop music
    stop sound


    pause 1.0

    show cg sidewalkmariacloseddoor
    pause 1.0
    play sound "door.ogg"
    show cg sidewalkmariaopendoor with dissolve
    pause 1.0

    "…"

    pause 1.0

    hide cg

    pause 1.0

    t "(??:?? - ?????)"

    play music "audio/music/chocolate.mp3" loop volume 0.5

    show stoppingCity at center:
        yoffset -50
    #show boiSubway drain
    show rain
    show train boisubwayonlytrain
    show char boisubwayonlyhandle
    with truthFade

    "…"

    "…"
    mm "Looks like this is my stop."

    pause 2.0

    scene black with hypothetical_fade
    stop music fadeout 1.0

    pause 1.0

    t "(5:50 - Street)"

    scene bg white with truthFade

    mm "It’s time to wake up."
    mm "I need to get dressed, and get to the bakery."
    
    scene street morning

    queue ending_music ["audio/music/Slow_Steps_Together.mp3", "audio/music/Slow_Steps_Together.mp3", "audio/music/Slow_Steps_Together.mp3"] volume 0.5
    play sound "audio/walkingInSnow.mp3" fadein 0.5 loop
    #queue ending_music ["<from 19.5 to 240.5>music/At_Midnight.mp3", "<from 0.5 to 240.5>music/At_Midnight.mp3", "<from 0.5 to 240.5>music/At_Midnight.mp3", "<from 0.5 to 240.5>music/At_Midnight.mp3", "<from 0.5>music/At_Midnight.mp3"] fadein 0.5 volume 0.5
    #$ renpy.sound.play("music/At_Midnight.mp3", channel="ending_music", loop=True)
    #show screen music_screen

    pause 2.0

    #…
    mm "At 6 in the morning, I always notice the still empty street, lit in a slightly blue tint."
    mm "There’s something about this timeframe that makes me a little happy and somewhat hopeful. As if the possibilities were endless."
    mm "It’s a small city, and an hour from now, most of the population is going to fill the streets, commuting to the one factory in town."
    mm "Some of them, passing by to buy some baked goods, some of them, doing their morning jog."
    mm "But right now, it’s just me and a public worker sweeping the streets."
    mm "Cozy vibes."
    #…

    stop sound

    scene bg bakery with bakeryFade

    pause 1.0

    c "How much is the Apfelstrudel?"
    m "It's 5 Euro."
    c "Here. Thanks."
    m "Thank you for your patronage!"
    #…
    mm "My job has a lot of downtime when mornings are nearing their ends."
    mm "I used to take advantage of that time to draw some stuff in my sketchbook when I first got this job, but now I’ve been getting lazier."
    mm "I get so tired of not being home for so long every day."
    mm "I can feel how much older I’ve gotten. I’m so tired."
    mm "I listen to the same playlist of songs every day to make it go by quicker, purposefully picking multiple 10 minute songs to put on my playlist."
    mm "Then I’d know 1 / 6 of an hour has finally passed and I’m closer to finally going the fuck home."
    mm "This helps me cope, daily. And at least it smells nice in here."
    mm "But still, I wish for more."
    mm "I want to be more."
    mm "…"

    pause 0.5

    mm "And suddenly, I’m clocking out."
    #…

    scene street evening with bakeryFade

    play sound "audio/walkingInSnow.mp3" fadein 0.5 loop

    #play sound "audio/crow.mp3"

    mm "Going home, I use long and nimble steps, abusing overtaking strats to get past older, slower people blocking my way."
    mm "I just have one goal in mind: My own four walls."
    mm "Cutting corners where I can, minimizing the time I spend outside."
    mm "…"
    mm "I look forward to getting home more than anyone, visibly."
    mm "And for what? I’ll be too mentally clocked out to work on what I actually want to create anyway."
    mm "Maybe it’s just the fact that I don’t have responsibilities to anyone but me there."
    mm "I can be a lazy mess, watch streams and just shut out anything outside."
    mm "But… is that really what I wanna be doing? Just wasting my days away?"
    mm "…"

    stop sound

    show staticSidewaysScene standstill at right with confrontFadeFull:
        yoffset 10

    pause 1.0

    m "Oh, right."
    scene bg white
    show confrontationAnim at center:
        yoffset 10
    #show mariaMovingSideways
    pause 8.0

    scene hope snow with confrontFadeFull

    m "It’s about time we talk it out, huh?"
    m "Or rather, it’s about time I take {color=#ff0d21}You{/color} back inside."
    m "I want {color=#ff0d21}You{/color} to know, there’s not a lot in my life I regret more than neglecting {color=#ff0d21}You{/color}."
    m "I want us to be together more than anything."
    m "And for that, I need to stop being a coward. {color=#ff0d21}You{/color} pushed me towards my dreams."
    m "It’ll be tough."
    m "It’ll be a lot of work."
    m "There’s a lot of frustration ahead, but I won’t let any of that set the wind off our sails."
    m "There’ll be many setbacks. Some people will mock us, and some will ignore us."
    m "Yet this time, I refuse to give it up."
    #m "But we can’t let that get us down."
    #m "We need to finish what we started. We need to keep shooting for the stars together. Especially when going through our hardest times."
    m "We need to keep shooting for the stars together, especially when going through our hardest times."
    m "Thank {color=#ff0d21}You{/color} for reminding me of that, in your own silly ways."
    m "Let’s go home."

    scene bg white with endingFade

    #$ persistent.truth = True
    $ achievement.grant("truth")
    $ achievement.sync()

    pause 2.0

    jump splashscreen

    return