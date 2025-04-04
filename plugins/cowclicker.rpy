######################
### Cow Clicker
######################

define MILKSTART=0
define COWSTART=1
define COWPRICESTART=40
define COWFACTOR=1.1
define MAXMILK=1177
define LOCKMILK=555
define UFOMILK=678
define GALLERYCOWS=49
define FARMERSTART=0
define FARMERPRICESTART=60
define FARMERFACTOR=1.5
define SECONDSPERFARMER=2
define BARNSTART=1
define COWSPERBARN=5
define BARNFACTOR=3
define BARNPRICESTART=100
define UPGRADECOUNT=4
define SLACKOFFSECONDS=300.0
define BONUSSECONDS=10
define BONUSFACTOR=5

define TIREDMESSAGETIMER=180
define TIREDMESSAGEDURATION=10
define UFOLOWERTIME=300
define UFOUPPERTIME=600
define UFODURATION=15

define MUSICQUEUE=["audio/music/Oyasumi.mp3", "audio/music/kerutosong.mp3", "audio/music/kerutosong_2.mp3", "audio/music/Yawning_cow.mp3", "audio/music/Farm_To_Farm.mp3", "audio/music/yoruno.mp3", "audio/music/kocchi_ushi.mp3", "audio/music/alien.mp3"]
define TIREDMESSAGES=["Are you tired? Maybe you should take a break!", "Milk is good for your bones!", "Cows are your friends!", "You can let the farmers handle it!", "Take your time, no need to rush!", "Moo!", "How was your day?", "Why not read a book in the meantime?", "Remember to stretch!", "Yeehaw!", "Wow, you're doing great!", "Keep it up!", "Cats are also pretty cute!", "Press F27 to unlock Big head mode!"]
default currentTiredMessage="Moo!"

define FTFPRICE=500000
default persistent.ftf=0
default slackoff=1
define EFFARCHPRICE=750000
default persistent.effarch=0
define BONUSPRICE=10000
default bonus=1
define INVASIONPRICE=1000000
define INVASIONFACTOR=10

default milk=MILKSTART
default cows=COWSTART
default cowprice=COWPRICESTART
default particleCounter=0
default farmers=FARMERSTART
default farmerprice=FARMERPRICESTART
default barns=BARNSTART
default barnprice=BARNPRICESTART
default clickableCow = True
#default milkGen = False
default fadeOutRepetitionPreventer = False
default doorlocked = True
default ufoReady = True
default ufotimer = 120
default ufoX = 0.5



default persistent.milk=MILKSTART
default persistent.cows=COWSTART
default persistent.cowprice=COWPRICESTART
default persistent.farmers=FARMERSTART
default persistent.farmerSpeed=FARMERSTART
default persistent.farmerMult=1
default persistent.farmerprice=FARMERPRICESTART
default persistent.barns=BARNSTART
default persistent.barnprice=BARNPRICESTART
default persistent.secondsperfarmer=SECONDSPERFARMER
default persistent.upgradesAvaillable=UPGRADECOUNT
default persistent.galUnlock=False
default persistent.invasion=1
default persistent.invasionBought=False
default persistent.currentAlienAchievement=0

image milksplosion:
    "boi clique/milk.png"
    animation
    parallel:
        yalign 0.5
        easeout 0.4 yalign 1.1
    parallel:
        xalign 0.5
        linear 0.5 xalign renpy.random.random()

layeredimage bonusmilkTagged:
    always:
        "boi clique/megamilk.png"
    
    group tag:
        attribute yes default:
            "boi clique/megamilkmult.png"

image bonusmilksplosion:
    "bonusmilkTagged"
    animation
    parallel:
        yalign 0.5
        easeout 0.4 yalign 1.1
    parallel:
        xalign 0.5
        linear 0.5 xalign renpy.random.random()

image chokeFlashImage:
    "red.png"
    xysize (1280, 720)
    animation
    alpha 0.0
    linear 5 alpha 1.0
    pause 2.0
    alpha 0.0

image kao:
    "boi clique/kao.png"

image kao2:
    "boi clique/kao2.png"

image smolkao:
    "kao"
    matrixcolor TintMatrix("#dde")*BrightnessMatrix(0.25)*SaturationMatrix(0.5)
    zoom 0.1

image smolkao2:
    "kao2"
    matrixcolor TintMatrix("#dde")*BrightnessMatrix(0.25)*SaturationMatrix(0.5)
    zoom 0.1

image smolkaomirror:
    "kao"
    matrixcolor TintMatrix("#dde")*BrightnessMatrix(0.25)*SaturationMatrix(0.5)
    zoom 0.1
    xzoom -1

image smolkaomirror2:
    "kao2"
    matrixcolor TintMatrix("#dde")*BrightnessMatrix(0.25)*SaturationMatrix(0.5)
    zoom 0.1
    xzoom -1

image tinykao:
    "kao"
    matrixcolor TintMatrix("#eef")*BrightnessMatrix(0.5)*SaturationMatrix(0.25)
    zoom 0.05

image tinykao2:
    "kao2"
    matrixcolor TintMatrix("#eef")*BrightnessMatrix(0.5)*SaturationMatrix(0.25)
    zoom 0.05

image spinboi:
    "smolkao"
    xanchor 0.5
    animation
    parallel:
        xzoom 1.0
        linear 1.0 xzoom -1.0
        linear 1.0 xzoom 1.0
    repeat
    parallel:
        xoffset 0
        linear 0.5 xoffset -50


layeredimage ufoimage:
    always:
        "spinboi"
        yoffset 100
        xoffset 113
    
    group ufo:
        attribute yes default:
            "boi clique/ufo.png" zoom 0.5


transform moveFO:
    subpixel True
    yoffset 640
    animation
    linear UFODURATION yoffset -160


image wood_board:
    Frame("boi clique/text.png", 30, 10, 30, 10)

image wood_board_sel:
    "wood_board"
    matrixcolor BrightnessMatrix(0.25)


image button_board:
    Frame("boi clique/button.png", 30, 10, 30, 10)

image button_board_ins:
    "button_board"
    matrixcolor BrightnessMatrix(-0.25)

image button_board_sel:
    "button_board"
    matrixcolor BrightnessMatrix(0.25)



style wooden_board:
    background "wood_board"
    hover_background "wood_board_sel"
    padding (30, 10)

style wooden_button:
    background "button_board"
    insensitive_background "button_board_ins"
    hover_background "button_board_sel"
    padding (30, 10)


image cloque_ins:
    "boi clique/cloque.png"
    matrixcolor BrightnessMatrix(-0.5)





screen cow_clicker(story_mode = False):
    zorder 3
    $ renpy.random.shuffle(MUSICQUEUE)
    $ renpy.music.set_volume(0.5)
    if story_mode:
        on "show" action [Queue("music", MUSICQUEUE, loop=True, fadein=0.5),
                            Show("StorySky")]
    else:
        on "show" action [Queue("music", MUSICQUEUE, loop=True, fadein=0.5),
                            SetVariable("ufotimer", renpy.random.randint(UFOLOWERTIME, UFOUPPERTIME)),
                            Show("Sky", story_mode)]
    timer TIREDMESSAGETIMER repeat True action [Show("TiredMessage")]

    add "boi clique/pastureMiddle.png"
    add "boi clique/pastureFront.png"
    imagebutton:
        #text "[milk] / [MAXMILK]" size 40
        #background "#000"
        idle "kao"
        hover "kao2"
        xpos .5
        ypos .5
        sensitive clickableCow
        keysym "K_SPACE"
        anchor (0.5, 0.5)
        action [If(story_mode, true=If(milk < MAXMILK,
                    true=[SetVariable("milk", milk + cows),
                        If(milk > LOCKMILK and doorlocked, 
                            true=[SetVariable("doorlocked", False),
                            Play("audio", "door.ogg")]),
                        If(milk > UFOMILK and ufoReady and cows > 1,
                            true=[SetVariable("ufoReady", False),
                            Show("StoryUfo")])],
                    false=[SetVariable("clickableCow", False),
                        Show("storyFadeOut")]),
                false=SetVariable("persistent.milk", persistent.milk + persistent.cows * bonus)),
                SetVariable("particleCounter", (particleCounter+1)%8),
                Show("milkFall%d" % particleCounter),
                Show("proceduralMoo"),
                SetVariable("slackoff", 1),
                Hide("slackOffTimer"),
                Show("slackOffTimer")]
    
    #add Milkdrop((0.5, 0.5))

    showif not story_mode:
        button:
            text "{color=#fff}return{/color}"
            style "wooden_board"
            tooltip "(to main menu)"
            xpos 0
            ypos .1
            anchor (0, 0.5)
            action [Stop("music"),
                    Stop("ufo_sound"),
                    Play("sound", "/audio/rain.mp3", loop=True, fadein=0.5),
                    Hide("Sky"),
                    Hide("Ufo"),
                    Hide("TiredMessage"),
                    Hide("cow_clicker")]
        label "{color=#fff}[persistent.milk] bottles of milk!{/color}":
            style "wooden_board"
            xpos .5
            ypos .25
            anchor (0.5, 0.5)
        button:
            text "{color=#f00}move to new farm{/color}"
            style "wooden_board"
            tooltip "{color=#f00}deletes all your cow clicking progress{/color}"
            xpos 0
            ypos .9
            anchor (0, 0.5)
            action Show("confirmNewFarm")
        button:
            text "{color=#fff}Cow count: [persistent.cows]/[persistent.barns*(COWSPERBARN+persistent.effarch)]\nPurchase price:\n[persistent.cowprice]{/color}"
            style "wooden_button"
            tooltip "Determines bottles of milk per click"
            activate_sound "audio/upgrade.mp3"
            sensitive persistent.milk >= persistent.cowprice and persistent.cows < persistent.barns*(COWSPERBARN+persistent.effarch)
            xpos 1.0
            ypos .3
            anchor (1.0, 0.5)
            action [SetVariable("persistent.milk", persistent.milk-persistent.cowprice),
                    SetVariable("persistent.cows", persistent.cows + 1),
                    SetVariable("persistent.cowprice", round(persistent.cowprice * COWFACTOR)),
                    If(persistent.cows>=GALLERYCOWS, true=SetVariable("persistent.galUnlock", True))]
        button:
            text "{color=#fff}Farmer count: [persistent.farmers]\nPurchase price:\n[persistent.farmerprice]{/color}"
            style "wooden_button"
            tooltip "Each farmer clicks once every 2 seconds"
            activate_sound "audio/upgrade.mp3"
            sensitive persistent.milk >= persistent.farmerprice
            xpos 1.0
            ypos .5
            anchor (1.0, 0.5)
            action [SetVariable("persistent.milk", persistent.milk-persistent.farmerprice),
                    Show("addFarmer"),
                    SetVariable("persistent.farmerprice", round(persistent.farmerprice * FARMERFACTOR))]
        button:
            text "{color=#fff}Barn count: [persistent.barns]\nPurchase price:\n[persistent.barnprice]{/color}"
            style "wooden_button"
            tooltip "Each barn holds " + str(COWSPERBARN)+ " cows"
            activate_sound "audio/upgrade.mp3"
            sensitive persistent.milk >= persistent.barnprice
            xpos 1.0
            ypos .7
            anchor (1.0, 0.5)
            action [SetVariable("persistent.milk", persistent.milk-persistent.barnprice),
                    SetVariable("persistent.barns", persistent.barns + 1),
                    SetVariable("persistent.barnprice", round(persistent.barnprice * BARNFACTOR))]
    
    
    
    else:
        label "{color=#fff}[milk] bottles of milk!{/color}":
            style "wooden_board"
            xpos .5
            ypos .25
            anchor (0.5, 0.5)
        button:
            text "{color=#fff}Cow count: [cows]/[barns*COWSPERBARN]\nPurchase price:\n[cowprice]{/color}"
            style "wooden_button"
            tooltip "Determines bottles of milk per click"
            activate_sound "audio/upgrade.mp3"
            sensitive milk >= cowprice and cows < barns*COWSPERBARN
            xpos 1.0
            ypos .3
            anchor (1.0, 0.5)
            action [SetVariable("milk", milk-cowprice),
                    SetVariable("cows", cows + 1),
                    SetVariable("cowprice", round(cowprice * COWFACTOR))]
        button:
            text "{color=#fff}Farmer count: [farmers]\nPurchase price:\n[farmerprice]{/color}"
            style "wooden_button"
            tooltip "Each farmer clicks once every 2 seconds"
            activate_sound "audio/upgrade.mp3"
            sensitive milk >= farmerprice
            xpos 1.0
            ypos .5
            anchor (1.0, 0.5)
            action [SetVariable("milk", milk-farmerprice),
                    SetVariable("farmers", farmers + 1),
                    SetVariable("farmerprice", round(farmerprice * FARMERFACTOR))]
        button:
            text "{color=#fff}Barn count: [barns]\nPurchase price:\n[barnprice]{/color}"
            style "wooden_button"
            tooltip "Each barn holds " + str(COWSPERBARN)+ " cows"
            activate_sound "audio/upgrade.mp3"
            sensitive milk >= barnprice
            xpos 1.0
            ypos .7
            anchor (1.0, 0.5)
            action [SetVariable("milk", milk-barnprice),
                    SetVariable("barns", barns + 1),
                    SetVariable("barnprice", round(barnprice * BARNFACTOR))]

    if story_mode and farmers >= 1:
        timer SECONDSPERFARMER/farmers repeat True action [If(milk >= MAXMILK and not fadeOutRepetitionPreventer,
                                                                true=[SetVariable("clickableCow", False) , Show("storyFadeOut")]),
                                                            SetVariable("milk", milk + cows),
                                                            If(milk > LOCKMILK and doorlocked, 
                                                                true=[SetVariable("doorlocked", False),
                                                                Play("audio", "door.ogg")]),
                                                            If(milk > UFOMILK and ufoReady and cows > 1,
                                                                true=[SetVariable("ufoReady", False),
                                                                Show("StoryUfo")])]
    elif not story_mode and persistent.farmerSpeed >= 1:
        timer SECONDSPERFARMER/persistent.farmerSpeed repeat True action SetVariable("persistent.milk", persistent.milk+(persistent.cows*(1+persistent.ftf*slackoff)*persistent.farmerMult))


    if not story_mode:
        if persistent.cows >= 10:
            imagebutton:
                idle "smolkao"
                hover "smolkao2"
                xpos 300
                ypos 300
                #anchor (0.5, 0.5)
                action [SetVariable("persistent.milk", persistent.milk + persistent.cows * bonus),
                        Show("proceduralMoo"),
                        SetVariable("slackoff", 1),
                        Hide("slackOffTimer"),
                        Show("slackOffTimer")]
            #add "smolkao" xpos 100 ypos 350 xzoom -1
        if persistent.cows >= 25:
            imagebutton:
                idle "smolkaomirror"
                hover "smolkaomirror2"
                xpos 155
                ypos 285
                #anchor (0.5, 0.5)
                action [SetVariable("persistent.milk", persistent.milk + persistent.cows * bonus),
                        Show("proceduralMoo"),
                        SetVariable("slackoff", 1),
                        Hide("slackOffTimer"),
                        Show("slackOffTimer")]
            #add "smolkao" xpos 150 ypos 300
        if persistent.cows >= 50:
            imagebutton:
                idle "tinykao"
                hover "tinykao2"
                xpos 1000
                ypos 300
                #anchor (0.5, 0.5)
                action [SetVariable("persistent.milk", persistent.milk + persistent.cows * bonus),
                        Show("proceduralMoo"),
                        SetVariable("slackoff", 1),
                        Hide("slackOffTimer"),
                        Show("slackOffTimer")]
            add "tinykao" xpos 1000 ypos 300  
        if persistent.cows >= 75:
            imagebutton:
                idle "tinykao"
                hover "tinykao2"
                xpos 1075
                ypos 290
                #anchor (0.5, 0.5)
                action [SetVariable("persistent.milk", persistent.milk + persistent.cows * bonus),
                        Show("proceduralMoo"),
                        SetVariable("slackoff", 1),
                        Hide("slackOffTimer"),
                        Show("slackOffTimer")]
            add "tinykao" xpos 1000 ypos 300
        if persistent.ftf:
            imagebutton:
                idle "boi clique/cloque.png"
                insensitive "cloque_ins"
                sensitive slackoff
                anchor (1.0, 1.0)
                pos (1.0, 1.0)
                tooltip "Full time farmers active!"
                action [Hide("slackOffTimer"),
                        Show("slackOffTimer")]
        hbox:
            grid 1 UPGRADECOUNT:
                button:
                        style "wooden_button"
                        text "Hyper speed milking\n"+ str(BONUSPRICE) + " milk"
                        tooltip "Clicking the cow milks for " + str(BONUSFACTOR) + " times the milk for " + str(BONUSSECONDS) + " seconds (repeatable!)"
                        activate_sound "audio/upgrade.mp3"
                        sensitive persistent.milk >= BONUSPRICE and bonus == 1
                        action [SetVariable("bonus", BONUSFACTOR),
                                SetVariable("persistent.milk",persistent.milk-BONUSPRICE),
                                Show("bonusOffTimer")]
                if persistent.ftf == 0:
                    button:
                        style "wooden_button"
                        text "Full-time farmers\n"+ str(FTFPRICE) + " milk"
                        tooltip "Farmers work twice as efficiently, as long as you don't slack off"
                        activate_sound "audio/upgrade.mp3"
                        sensitive persistent.milk >= FTFPRICE
                        action [SetVariable("persistent.ftf", 1),
                                SetVariable("persistent.milk",persistent.milk-FTFPRICE),
                                SetVariable("persistent.upgradesAvaillable", persistent.upgradesAvaillable-1)]
                
                if persistent.effarch == 0:
                    button:
                        style "wooden_button"
                        text "Efficient Architecture\n"+ str(EFFARCHPRICE) + " milk"
                        tooltip "Barns hold 3 additional cows each"
                        activate_sound "audio/upgrade.mp3"
                        sensitive persistent.milk >= EFFARCHPRICE
                        action [SetVariable("persistent.effarch", 3),
                                SetVariable("persistent.milk", persistent.milk-EFFARCHPRICE),
                                SetVariable("persistent.upgradesAvaillable", persistent.upgradesAvaillable-1)]
                if persistent.invasionBought == False:
                    button:
                        style "wooden_button"
                        text "ALIEN INVASION!\n"+ str(INVASIONPRICE) + " milk"
                        tooltip "UFOs appear " + str(INVASIONFACTOR) + " times as often (toggleable!)\nEffect starts after next UFO/returning to main menu"
                        activate_sound "audio/upgrade.mp3"
                        sensitive persistent.milk >= INVASIONPRICE
                        action [SetVariable("persistent.invasionBought", True),
                                SetVariable("persistent.invasion", INVASIONFACTOR),
                                SetVariable("persistent.milk", persistent.milk-INVASIONPRICE)]
                else:
                    button:
                        style "wooden_button"
                        text "TOGGLE ALIEN INVASION!\n"+ If(persistent.invasion==INVASIONFACTOR, true="ON", false="OFF")
                        tooltip "UFOs appear " + str(INVASIONFACTOR) + " times as often (toggleable!)\nEffect starts after next UFO/returning to main menu"
                        activate_sound "audio/upgrade.mp3"
                        action If(persistent.invasion==INVASIONFACTOR, true=SetVariable("persistent.invasion", 1), false=SetVariable("persistent.invasion", INVASIONFACTOR))
            yalign 0.75
                

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip



screen storyFadeOut():
    zorder 10
    modal True
    $ fadeOutRepetitionPreventer = True
    #if not fadeOutRepetitionPreventer:
        #$ fadeOutRepetitionPreventer = True
        #$ renpy.transition(chokeFlash)
        #$ renpy.pause(4.0)
        #$ renpy.jump("clicker_done")
    add "chokeFlashImage"
    on "show" action [Play("sound", "audio/cowchoke.mp3"), Stop("music", fadeout=6.0)]
    timer 6.0 action [Hide("cow_clicker"), Hide("StorySky"), Hide("StoryUfo")]
    timer 10.0 action [Hide("storyFadeOut"), Jump("clicker_done")]



screen confirmNewFarm():
    zorder 4
    modal True
    label "{color=#fff}Abandon farm and start from scratch?{/color}{color=#f00} You can never return to this farm!{/color}":
        style "wooden_board"
        xpos .5
        ypos .4
        anchor (0.5, 0.5)
    button:
        text "{color=#f00}Farewell, my friends!{/color}"
        style "wooden_board"
        xpos .4
        ypos .6
        anchor (0.5, 0.5)
        action [SetVariable("persistent.milk", MILKSTART),
                SetVariable("persistent.cows", COWSTART),
                SetVariable("persistent.cowprice", COWPRICESTART),
                SetVariable("persistent.farmers", FARMERSTART),
                SetVariable("persistent.farmerSpeed", FARMERSTART),
                SetVariable("persistent.farmerMult", 1),
                SetVariable("persistent.farmerprice", FARMERPRICESTART),
                SetVariable("persistent.barns", BARNSTART),
                SetVariable("persistent.barnprice", BARNPRICESTART),
                SetVariable("persistent.ftf", 0),
                SetVariable("persistent.effarch", 0),
                SetVariable("persistent.upgradesAvaillable", UPGRADECOUNT),
                SetVariable("persistent.invasionBought", False),
                SetVariable("persistent.invasion", 1),
                SetVariable("bonus", 1),
                Hide("confirmNewFarm")]
    button:
        text "{color=#fff}Wait, no!{/color}"
        style "wooden_board"
        xpos .6
        ypos .6
        anchor (0.5, 0.5)
        action Hide("confirmNewFarm")



transform tiredTransform:
    yalign -0.1
    easein 1 yalign 0.1

screen TiredMessage():
    zorder 4
    on "show" action SetVariable("currentTiredMessage", renpy.random.choice(TIREDMESSAGES))
    label currentTiredMessage:
            style "wooden_board"
            xpos .5
            #ypos .1
            anchor (0.5, 0.5)
            at tiredTransform
    timer TIREDMESSAGEDURATION action Hide("TiredMessage")


screen Sky():
    modal True
    zorder 1
    add "boi clique/pastureBG.png"
    if persistent.cows >= 10:
        timer ufotimer/persistent.invasion repeat True action [SetVariable("ufotimer", renpy.random.randint(UFOLOWERTIME, UFOUPPERTIME)),
                                            Show("Ufo")]

screen StorySky():
    modal True
    zorder 1
    add "boi clique/pastureBG.png"

screen Ufo():
    zorder 2
    on "show" action [SetVariable("ufoX", renpy.random.random()),
                        Play("ufo_sound", "ufo.mp3")]
    imagebutton:
        align (ufoX, -0.5)
        idle "ufoimage"
        at moveFO
        activate_sound "audio/upgrade.mp3"
        action [Show("addFarmer"),
                Show("AlienAchievement"),
                Stop("ufo_sound"),
                Hide("Ufo")]
    
    timer UFODURATION action [SetVariable("persistent.cowprice", round(persistent.cowprice/COWFACTOR)),
                                SetVariable("persistent.cows", persistent.cows-1),
                                Hide("Ufo")]

screen AlienAchievement():
    $ persistent.currentAlienAchievement += 1
    $ achievement.progress("alienAchievementProgress", persistent.currentAlienAchievement)
    $ achievement.sync()
    $ renpy.hide("AlienAchievement")



screen StoryUfo():
    zorder 2
    on "show" action [SetVariable("ufoX", renpy.random.random()),
                        Play("ufo_sound", "ufo.mp3")]
    imagebutton:
        align (ufoX, -0.5)
        idle "ufoimage"
        at moveFO
        activate_sound "audio/upgrade.mp3"
        action [SetVariable("farmers", farmers+1),
                Stop("ufo_sound"),
                Hide("StoryUfo")]
    
    timer UFODURATION action [SetVariable("cowprice", round(cowprice/COWFACTOR)),
                                SetVariable("cows", cows-1),
                                Hide("Ufo")]



screen proceduralMoo():
    on "show" action [Play("moo", "audio/moo" + str(renpy.random.randint(1, 6)) + ".mp3"),
                    Hide("proceduralMoo")]



screen addFarmer():
    on "show" action [SetVariable("persistent.farmers", persistent.farmers+1),
                        If(persistent.farmers%10 == 9 and persistent.farmers > 10,
                            true=[SetVariable("persistent.farmerMult", persistent.farmerMult+1),
                                SetVariable("persistent.farmerSpeed", 10)],
                            false=If(persistent.farmers < 19,
                                    true=SetVariable("persistent.farmerSpeed", persistent.farmers+1),
                                    false=SetVariable("persistent.farmerSpeed", 10 + (1/persistent.farmerMult)*(persistent.farmers+1)%10))),
                        Hide("addFarmer")]



screen slackOffTimer():
    timer SLACKOFFSECONDS action SetVariable("slackoff", 0)

screen bonusOffTimer():
    timer BONUSSECONDS action [SetVariable("bonus", 1),
                                Hide("bonusOffTimer")]


screen milkFall0():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall0")

screen milkFall1():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall1")

screen milkFall2():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall2")

screen milkFall3():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall3")

screen milkFall4():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall4")

screen milkFall5():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall5")

screen milkFall6():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall6")

screen milkFall7():
    zorder 4
    if bonus != BONUSFACTOR:
        add "milksplosion"
    else:
        add "bonusmilksplosion"
        on "show" action Play("megamilk", "megamilk.ogg")
    timer 0.5 action Hide("milkFall7")
