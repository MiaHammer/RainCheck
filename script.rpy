# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sshake = Shake((0, 0, 0, 0), 0.5, dist=15)

# The game starts here.

label start:

    $ _game_menu_screen = "load"

    if persistent.trailer:
        jump trailer

    scene black

    pause 0.5

    t "(??:?? - ?????)"

    play sound "audio/train.mp3" loop
    play music "audio/music/chocolate.mp3" loop volume 0.4

    show wrappingCity at center:
        yoffset -50
    show boiSubway
    with truthFade

    n "You've been here a while."
    show boiSubway strain
    n "…"
    show boiSubway brain
    n "Have you been feeling stressed?"
    n "Be it from work, from the lack of it, from a chronic illness, from paying rent, or maybe from an approaching deadline?"
    n "…"
    n "Do you perhaps have a dream project you are trying to achieve? Have you been making steady progress on it?"
    n "…"
    n "Ah, I see…"
    n "Oh, me? Well…"
    show boiSubway refrain
    n "Lately, I’ve been very conscious of the flow of time. It’s all-encompassing, it feels uncomfortable."
    n "In a sense, there is no “choice” when time is concerned."
    n "It irrevocably moves onwards."
    show boiSubway sprain
    n "…"
    n "A certain level of anxiety and precaution is good for our longevity, but too much can possibly lead to a miserable existence."
    show boiSubway refrain
    n "I used to try to seal away the origin of my stress, only to despair later when I was unprepared for the worst."
    show boiSubway brain
    n "But nowadays, I prefer to rush into things head-on."
    n "I think it’s the best way to handle things, especially for Bullheads like me, with precious little time on this Earth."
    b "I charge forth, trying to keep up with the flow."
    show boiSubway strain
    b "Sometimes I’m able to catch up a bit, but in the end, entropy is still inevitable."
    b "…"
    show boiSubway refrain
    b "These kinds of thoughts constantly manage to find their ways into my mind."
    b "Yet, despite not enjoying pondering these ideas, I still value them for pushing me forward."
    show boiSubway brain
    b "Now, I’d like to ask you a question. Answer sincerely:"
    b "How are you planning on spending your precious time?"
    b "…"

    pause 0.5

    stop sound
    stop music
    scene black

    t "(19:00 - Desk)"

    scene galDesk deskmaria

    play sound "audio/rain.mp3" loop

    mm "I've always found solace in my room, it’s my very own sanctuary."
    mm "It’s easier to ignore all my issues here."

    show galDesk deskmariadiscord

    mm "As usual, I open social media and scroll to and from my favorite group chat, checking if my best friend, Annie, the owner of said group chat, has written anything tonight."
    m "Guess she hasn’t come back from work yet."
    mm "As the minutes pass, I feel a familiar sense of loneliness."
    mm "I go through every new message, every notification, there's nothing else worth reading, but I keep scrolling."
    mm "I consider writing about what’s going on with me there, writing opinions about the latest game I played, or what I am expecting out of the next."
    mm "But in the end, I feel better just reading other people’s stories and commiserating with them, giving them advice, or expressing sympathy towards them."
    mm "Reminding myself there are always people worse off than me helps. I am grateful for what I have, and should strive to express myself positively."
    mm "But I know deep down I don’t care about any of these people. And I’m absolutely sure none of them care about me either."
    mm "At the smallest hint of a differing opinion, at the slightest glimpse of a misunderstanding, a stressful, completely useless argument would follow."
    mm "I’m not cut out for that anymore."
    mm "I’m overwhelmed, some days I want to scream, but at the same time, I can’t fathom opening up to more people, revealing my weaknesses, only for them to abuse me in return."
    mm "…"
    mm "It looks like Annie is home now."
    

    stop sound

    scene black

    pause 0.5

    t "(20:00 - Desk)"

    scene galDesk deskmariadiscord

    play sound "audio/rain.mp3" loop

    m "Hey Ann!"
    a "Hey! How are you feeling tonight?"
    m "I’m ok."
    m "Wanna watch something for a bit?"
    a "Ah, yeah sure. Wanna continue watching that girl’s band anime?"
    m "Sure, whatever you want!"
    a "Mmmkay! Just let me put the bread in the oven."

    stop sound

    scene black

    pause 0.5

    t "(21:00 - Desk)"

    scene cg mariaandanniecall1

    play sound "audio/computer-hum.mp3" loop fadein 1.0


    m "I love that ending song so much."
    a "It’s brilliant, but I prefer the opening, personally."
    a "Oh, just some more minutes and the bread will be done!"
    a "So Maria, what have you been up to?"
    m "I’ve been thinking of making some art and maybe making a game again. I’ve been posting some of my old drawings around, but they don’t seem to gain any traction online."
    m "I feel like a fraud, and that I’ll never escape being a wage slave with no energy for anything productive at home."
    a "Yeah, that sucks... But I do think your drawings are lovely! Even though I don’t see you making them that often anymore."
    m "Thanks. You don’t need to lie though, my stuff kinda sucks and hasn't improved in ages."

    show cg mariaandanniecall2

    a "I’m not lying! Maria, I know it’s kinda delicate, but please stop with the self deprecation, for your own good."
    a "It never leads to a good place."
    m "I know all of that already. You don’t need to lecture me."
    a "Maria, please…"


    show cg mariaandanniecall1

    a "The grind always sucks, especially when it relies on luck and other people, but you will be okay in the end. If you have a dream, please don’t let go of it"
    a "Anyway, brb"

    stop sound

    scene black

    mm "In-between episodes, we take a little break from watching, so that Annie can pick up her bread."
    mm "Meanwhile, I sit with my own thoughts for a bit."

    scene cg mariaandanniecall1

    play sound "audio/computer-hum.mp3" loop fadein 1.0

    a "Back."
    m "Sorry. I know you’ve told me that before but it’s hard to internalize."
    a "It's okay!"
    m "How was your day, Ann?"
    a "My day was spent thinking about this bread."
    a "Making my own made me so happy, thank you for the recipe!"
    a "The difference in quality from grocery store bread is crazy!"
    m "Yeah, you tell me lol"

    stop sound

    scene black
    mm "After watching another episode, we wish each other a good night and go to bed."

    pause 0.5
    
    t "(23:40 - Bed)"

    play sound "audio/ticking-clock.mp3" loop

    mm "Tonight, the quiet feels different. I can't sleep."
    mm "I already know from experience staying in bed doesn’t help when my mind grows anxious. I need to do something about this."
    
    stop sound

    scene black

    pause 0.5

    t "(23:50 - Desk)"

    show cg der notizblock

    play sound "audio/raven-call.mp3" loop

    mm "Sitting with a pencil over the page, I glance toward the window."

    scene streetwindow framey

    mm "I feel a heavier than usual atmosphere, the skies above are pitch black."
    
    scene black
    show cg der notizblock
    
    mm "…"
    mm "My hand trembles, as I try to keep the pencil hovering over the page."
    mm "…"
    mm "Push it down and I can finally make some progress."
    mm "I can’t. I feel trapped."
    mm "Trapped in the future."
    mm "Too cognizant of the outcome, to be able to live out the process."
    mm "…"
    mm "I's scary: The prospect of sketching something today worse than yesterday, and wasting all of that time for nothing."
    mm "I’ve never been able to keep a consistent practice routine. My art has looked the same for years."
    mm "… But it wasn’t always like this."
    mm "The world outside is unforgiving. Ruthless, at points. It leads to so much pain, exposing my vulnerable side to the world. Right now, I crave safety. "
    mm "The unknown is too great a risk. The next step, nebulous."
    mm "…"

    stop sound

    scene black

    pause 0.5

    t "(00:00 - Room)"

    play sound "audio/rain.mp3" loop

    show cg der notizblock

    mm "Usually, I have trouble focusing with any kind of noise, but the rain is different."
    mm "Accompanied by the beautiful sounds of the rain, I feel calm, like I can get under a comfy blanket and just exist in peace."
    mm "But at the same time I don’t feel like I deserve to be feeling comfortable now."
    mm "…"
    mm "I notice the streetlight beside my house starting to flicker."
    mm "…"
    show cg der notizblock with flashInOut
    mm "…"
    m queiss "… What’s going on out there at this time of the night?"

    scene streetwindow figurehere rainon
    with flashInOut

    pause 3.0

    mm "I freeze, with my heart pounding in my chest."
    mm "Is there someone standing there? Why?"
    mm "I can barely make out this figure—someone wearing a red raincoat?"
    mm "{color=#ff0d21}They{/color} are standing there, in the middle of the street, shifting slightly, as if drowsy."
    mm "It feels like {color=#ff0d21}They{/color} are looking vaguely in my direction."

    play music "audio/echoing-kick-drum.mp3" fadein 3.0 loop

    mm "Suddenly, my thoughts start racing in a chaotic whirl."
    m shock "Is that a stalker!? A burglar scouting my house!?"
    m concern "What the fuck."

    scene black
    show bg outside
    show theFigure at top
    show rain
    show bg2 onlydesks at sshake
    play audio "audio/shakesound.ogg"

    mm "I have to act. Fast."
    mm "My hands tremble as I grab my phone and dial the cops."

    p "Almhuf Police, what’s your emergency?"
    scene black
    show bg outside
    show theFigure at top
    show rain
    show bg2 onlydesks at sshake
    play audio "audio/shakesound.ogg"
    m concern "There’s someone outside my house, standing in the middle of the street,
    looking right in the direction of my house. They’re wearing some kind of coat and
    look kinda tipsy and very shady. Please send someone!"
    p "They’re just standing there?"
    m concern "Yes, and looking directly at me!"
    p "I understand this must feel unsettling, but unless they take further action,
    there’s not much we can do right now. It’s not unusual for drunk people to act weirdly,
    even if it seems odd."
    mm "She says in an aggressively direct tone that leaves me without any will to continue this conversation."
    p "Please, lock your doors and windows. If the situation escalates, do call us
    immediately."
    m concern "... Ok"

    show rgbFigure at top behind bg2
    hide theFigure

    mm "The line goes dead. Outside, the figure stops moving completely."
    mm "I recoil, my breathing gets heavier."
    m concern "Nobody’s coming…"

    scene black

    pause 0.5

    t "(00:15 – Messaging App)"
    mm "I pulled back my phone to message Annie, and quickly explained the situation to her."
    a phone "And the police did nothing? Fuck"
    m phone "Yeah… I’m freaking out rn."
    a phone "If you’d like, you can stay overnight at my place? Though I’m not sure if it’d
    be wise to leave your house right now."
    m phone "I haven’t even checked the doors and windows yet. I’m in shock"
    a phone "You should do that! Check everything right now!"
    m phone "I think I will…"

    if achievement.has("choked") and achievement.has("stalked") and achievement.has("decapitated"):
        jump unlocked
    else:
        jump standard





label standard:
    menu:
        
        "{font=DejaVuSans.ttf}E̴̡̨̛̘̟͇̝̳͚̜̞͚̖̯̼̻͔̫͋̅̈́̓́́̍̎̀̾͌͘͘͘͝Ń̸̲̠̮̠̟̼̞̃̑̈́͋͊͑̄́̍Ḑ̶̧̗̦̹̯̳͌̃͛͂̅̇̏͂̽̿̾̇̕Ḽ̵̜̗̱̭̼̈͒̂̆̔͂͘͝͠͝Ė̶̯̪̹͒̿̓S̷̢̧̨̢̝̝̟̺̣̦̼͙͙̥̱͈̎͌̈́̀̎͋̈͜͠͝S̴͖͋́͒̕͜ ̸̨̡̤͎͉̼̮̜͕͓̞̬̪̤̬̮̔͌̀͂̓̃̎̿͝S̷̡̱͚̞̞̖̩̰͓̏̀̀̿̒̎̓͗̐U̷͙̠̼̙̖̼̼̫͍̼̬̮̹͗̀̐͆ͅͅF̵̢̛͙̫͎̜̹͚͂͆̍͋̆ͅF̷̰̼̀̃͛̓͐̄̋̑̈̕͝E̵̡̧̢̘͈̞̫̠̝̫̊̊̃̋͒̋́̊̓̈̃̈́̕̚̚͜͝ͅR̶̡͎̟͓͍̻̪̤̖͕̟̞̃̈́̂̋̐̈́͒̋̐̑̊̔́͝I̵͓̺̼͈͚̫̖̩̚͜N̴̨̧̰͈̼̗̥͙̳̠̲̻̼̣̼̎̾̄͋̔̃͒͜ͅG̷̖̓̐͐{/font}":
            "..."
            jump standard

        "Check the doors and windows, and try to calm down":
            jump clicker_ending
        
        "Keep staring at them":
            jump freeze_ending
        
        "Abandon the house for the night and go to Annie’s house":
            jump decap_ending

label unlocked:
    menu:
        
        "Confront {color=#ff0d21}Them{/color}":
            jump true_ending

        "Check the doors and windows, and try to calm down.":
            jump clicker_ending
        
        "Keep staring at {color=#ff0d21}Them{/color}":
            jump freeze_ending
        
        "Abandon the house for the night and go to Annie’s house":
            jump decap_ending
