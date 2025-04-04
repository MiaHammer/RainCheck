label decap_ending:

    pause 1.0

    t "(0:20 - Garage)"

    
    m neutral "My best shot is going to Annie’s for the night."
    scene bg stairs at sshake
    play audio "audio/shakesound.ogg"
    mm "I almost tripped running down the stairs to the hallway, and then to the garage."
    mm "I pulled out my phone and messaged Annie to let her know I’m coming:"
    m phone "Hey Annie, are you still awake?"
    a phone "Yeah"
    m phone "I think I’d feel safer sleeping at your place tonight, would that be ok?"
    mm "…"
    m phone "Hello? Annie?"
    a phone "Yes, that’s fine! Just… Be careful on the way!"
    m phone "Thank you. I’m coming now."
    mm "I pocket my phone, then prepare to grab my helmet and ride off."
    mm "I’ll be okay as soon as I get there. Tomorrow will be a good day, I’ll make sure of that."

    scene black with Fade(2,0.5,0)

    stop music

    $ renpy.movie_cutscene("images/BikeScene.mpg")

    scene black
    stop sound
    pause 3.0
    
    t "(??:?? - ?????)"

    play sound "audio/train.mp3" loop
    queue ending_music ["audio/music/chocolate.mp3", "audio/music/chocolate.mp3", "audio/music/chocolate.mp3"] volume 0.4

    show wrappingCity at center:
        yoffset -50
    show boiSubway
    with truthFade

    b "Oh."
    b "You’re back."
    show boiSubway strain
    b "Haven’t found your stop yet, huh?"
    b "…"
    show boiSubway brain
    b "Let me ask you something."
    b "Have you ever heard of the Immortal Snail Dilemma?"

    show cg slime with hypothetical_fade
    
    b "An Invincible, Invisible Snail. It moves relentlessly towards you, wherever you might be. No matter the distance. It’s only a matter of time."
    b "In the Zeitgeist, it appears as a Snail, but in truth, it could be anything."
    b "Even if you pushed {color=#ff0d21}Them{/color} halfway around the world, {color=#ff0d21}They{/color} would loop back around to find you."
    
    hide cg slime
    show boiSubway refrain
    with hypothetical_fade

    b "No matter how many doors you lock."
    b "The control you have is an illusion."
    show boiSubway strain
    b "…"
    show boiSubway brain
    b "Now tell me, if the Snail were on the train right now, what would you do?"
    b "…"
    show boiSubway refrain
    b "You’d better pick your stop."


    show boiSubway drain
    with dissolve

    pause 1.0

    scene black with forestFade

    pause 1.0

    if not achievement.has("choked") and not achievement.has("stalked") and not achievement.has("decapitated"):
        "Use ctrl or tab to skip through text"
        pause 1.0

    #$ persistent.decapitated = True
    $ achievement.grant("decapitated")
    $ achievement.sync()
    $ MainMenu(confirm=False)()
    #return