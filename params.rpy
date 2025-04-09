default persistent.choked = False
default persistent.stalked = False
default persistent.decapitated = False
default persistent.truth = False
default persistent.overflow = False
default persistent.trailer = False


init python:
    renpy.music.register_channel("voices", "voice", True)
    renpy.music.register_channel("moo", "sfx", loop=False)
    renpy.music.register_channel("ufo_sound", "sfx", loop=False)
    renpy.music.register_channel("megamilk", "sfx", loop=False)
    renpy.music.register_channel("ending_music", "music", loop=False)

    achievement.register("choked")
    achievement.register("stalked")
    achievement.register("decapitated")
    achievement.register("truth")
    achievement.register("overflow")
    achievement.register("alienAchievementProgress", stat_max=10)

init python:
    def boopy_voice(event, interact=True, boopfile="typewriter.mp3", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(boopfile, channel="voices", loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel="voices")


define m = Character("Maria", color="#ff0d21", image="m", callback=boopy_voice, cb_boopfile="Maria.mp3")
image side m neutral = im.Scale("Maria3.png", 200, 200)
image side m queiss = im.Scale("Maria3-2.png", 200, 200)
image side m concern = im.Scale("Maria3-3.png", 200, 200)
image side m shock = im.Scale("Maria3-4.png", 200, 200)
image side m crying = im.Scale("Maria3-5.png", 200, 200)
image side m phone = im.Scale("Phone.png", 200, 200)
define mm = Character("Maria", color="#aa0912", what_prefix="{i}", what_suffix="{/i}", callback=boopy_voice, cb_boopfile="MentalMaria.mp3")
define a = Character("Annie", color="#21be44", image="a", callback=boopy_voice, cb_boopfile="Annie.mp3")
image side a neutral = im.Scale("Annie1.png", 200, 200)
image side a concern = im.Scale("Annie2.png", 200, 200)
image side a phone = im.Scale("Phone.png", 200, 200)
image a bakery = "Annie3.png"
define p = Character("Policewoman", color="#1131aa", callback=boopy_voice, cb_boopfile="policewoman.mp3")
define old = Character("Customer", color="#848", callback=boopy_voice, cb_boopfile="policewoman.mp3")
define c = Character("Customer", color="#1131aa", callback=boopy_voice, cb_boopfile="man.mp3")
define t = Character("", callback=boopy_voice, what_prefix="{cps=6}", what_suffix="{/cps}")
define n = Character("", callback=boopy_voice, cb_boopfile="narration.mp3")
define b = Character("Bullhead", color="#FBF236", callback=boopy_voice, cb_boopfile="narration.mp3")




define flashIn = Fade(.2, 0, 0, color="#fff")
define flashOut = Fade(0, 0, .2, color="#fff")
define flashInOut = Fade(0.5, 0, 0.5, color="#fff")

define hypothetical_fade = Fade(.2, 0, .2)

define clickerFade = Fade(1, 1, 0)
#define chokeFlash = Fade(3, 2, .1, color="#f00")
define forestFade = Fade(3, 1, 0)
define forestBoiFade = Fade(0, 0, 3)
define inRoomFlash = Fade(5, 1, 0.5, color="#f00")
#define decapFlash = Fade(.05, 2, 0, color="#f00")
define truthFade = Fade(0, 0, 5)
define bakeryFade = Fade(0.5, 0.0, 0.5, color="#fff")
define confrontFadeOut = Fade(2, 0, 0, color="#fff")
define confrontFadeIn = Fade(0, 0, 2, color="#fff")
define confrontFadeFull = Fade(2, 1, 2, color="#fff")
define endingFade = Fade(5, 0, 0, color="#fff")



image rain = Fixed(SnowBlossom("gui/raindrop.png", count=200, xspeed=100, yspeed=900, start=0.2))
image rainSubway = Fixed(SnowBlossom("gui/raindrop.png", count=200, xspeed=1500, yspeed=900, start=0.2))



image rFigure:
    "char raincoat.png"
    matrixcolor TintMatrix("#f00") * OpacityMatrix(0.3)

image gFigure:
    "char raincoat.png"
    matrixcolor TintMatrix("#0f0") * OpacityMatrix(0.3)

image bFigure:
    "char raincoat.png"
    matrixcolor TintMatrix("#00f") * OpacityMatrix(0.3)

layeredimage rgbFigure:
    always:
        "bFigure"
    
    group left:
        attribute left default:
            "rFigure"
            xoffset -5
    
    group right:
        attribute right default:
            "rFigure"
            xoffset 5

image theFigure:
    "rgbFigure"
    animation
    linear 0.050 xoffset -2
    linear 0.050 xoffset +2
    repeat


define morningTint = TintMatrix("#cce")
define eveningTint = TintMatrix("#ecb")

image mornSnowflake1:
    "gui/snow1.png"
    matrixcolor morningTint

image mornSnowflake2:
    "gui/snow2.png"
    matrixcolor morningTint

image eveSnowflake1:
    "gui/snow1.png"
    matrixcolor eveningTint

image eveSnowflake2:
    "gui/snow2.png"
    matrixcolor eveningTint

image smolsno1:
    "gui/snow1.png"
    zoom .5

image smolsno2:
    "gui/snow2.png"
    zoom .5

image smolmornsno1:
    "smolsno1"
    matrixcolor morningTint

image smolmornsno2:
    "smolsno2"
    matrixcolor morningTint

image smolevesno1:
    "smolsno1"
    matrixcolor eveningTint

image smolevesno2:
    "smolsno2"
    matrixcolor eveningTint

image snow1 = Fixed(SnowBlossom("gui/snow1.png", start=0.5))
image snow2 = Fixed(SnowBlossom("gui/snow2.png", start=0.5))
image snow3 = Fixed(SnowBlossom("smolsno1", start=0.5))
image snow4 = Fixed(SnowBlossom("smolsno2", start=0.5))
image snowmo1 = Fixed(SnowBlossom("mornSnowflake1", start=0.5))
image snowmo2 = Fixed(SnowBlossom("mornSnowflake2", start=0.5))
image snowmo3 = Fixed(SnowBlossom("smolmornsno1", start=0.5))
image snowmo4 = Fixed(SnowBlossom("smolmornsno2", start=0.5))
image snoweve1 = Fixed(SnowBlossom("eveSnowflake1", start=0.5))
image snoweve2 = Fixed(SnowBlossom("eveSnowflake2", start=0.5))
image snoweve3 = Fixed(SnowBlossom("smolevesno1", start=0.5))
image snoweve4 = Fixed(SnowBlossom("smolevesno2", start=0.5))


image morningstreet:
    "bg streets.png"
    matrixcolor morningTint

image eveningstreet:
    "bg streets.png"
    matrixcolor eveningTint


image GalleryBGStretch:
    "galleryBG.png"
    xysize (1280, 720)





layeredimage galDesk:
    always:
        "bg outside"
    
    group rain:
        attribute r default:
            "rain"
    
    group fg:
        attribute desk default:
            "bg2 onlydesks"
        attribute deskmaria:
            "bg2 deskmaria"
        attribute deskmariadiscord:
            "bg2 deskmariadiscord"
        attribute deskmariacow:
            "bg2 deskmariacow"

layeredimage street:
    group bg:
        attribute noon default:
            "bg streets"
        attribute morning:
            "morningstreet"
        attribute evening:
            "eveningstreet"
    
    group snow1:
        attribute noon default:
            "snow1"
        attribute morning:
            "snowmo1"
        attribute evening:
            "snoweve1"
    
    group snow2:
        attribute noon default:
            "snow2"
        attribute morning:
            "snowmo2"
        attribute evening:
            "snoweve2"
    
    group snow3:
        attribute noon default:
            "snow3"
        attribute morning:
            "snowmo3"
        attribute evening:
            "snoweve3"
    
    group snow4:
        attribute noon default:
            "snow4"
        attribute morning:
            "snowmo4"
        attribute evening:
            "snoweve4"

layeredimage streetwindow:
    always:
        "cg sidewalk" at center
        yoffset - 120
    
    group figure:
        attribute figurehere:
            "theFigure" at center
            yoffset - 10
    
    group rain:
        attribute rainon:
            "rain"
    
    group framey:
        attribute framey default:
            "framey sidewalkwindowframe"


layeredimage hope:
    always:
        "bg hope"
    
    group snow3:
        attribute snow:
            "snow3"
    
    group snow4:
        attribute snow:
            "snow4"
    
    group maria:
        attribute maria default:
            "cg hope"
    
    group snow1:
        attribute snow:
            "snow1"
    
    group snow2:
        attribute snow:
            "snow2"



image wrappingCity:
    "BoiSubwayCityWrap.png"
    animation
    xoffset -1280
    linear 8.0 xoffset 1280
    repeat

image stoppingCity:
    "BoiSubwayCityWrap.png"
    animation
    xoffset -1280
    easein 12.0 xoffset 1280

image animatedTrain:
    "train BoiSubwayONLYTRAIN.png"
    animation
    yoffset 0
    pause 2.0
    easein 0.25 yoffset -5
    easein 0.25 yoffset 5
    linear 0.25 yoffset 0
    repeat


layeredimage boiSubway:
    #group city:
    #    attribute city default:
    #        "wrappingCity" at center yoffset -50
    
    group rain:
        attribute rain default:
            "rainSubway"
    
    group train:
        attribute train default:
            "animatedTrain"
    
    group brain:
        attribute brain default:
            "BoiSubwayONLYBOI.png"
        attribute strain:
            "BoiSubwayONLYBOICLOSEDEYES.png"
        attribute refrain:
            "BoiSubwayONLYBOISIDEWAY.png"
        attribute sprain:
            "BoiSubwayONLYBOISIDEWAYCLOSEDEYE.png"
        attribute drain:
            "char BoiSubwayONLYHANDLE.png"



image mariaMovingSideways:
    "SidewaysMaria.png"
    animation
    parallel:
        xoffset 1800
        linear 4 xoffset 700
    parallel:
        yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        easein 0.25 yoffset 0
        easeout 0.25 yoffset 10
        ease 0.25 yoffset 0


layeredimage staticSidewaysScene:
    always:
        "MariaWalkingStreetBG.png"
    
    group snow3:
        attribute here default:
            "snow3"

    group snow4:
        attribute here default:
            "snow4"

    group hood:
        attribute here default:
            "SidewaysHood.png"

    group maria:
        attribute here default:
            "mariaMovingSideways"
        attribute standstill:
            "SidewaysMaria.png" xoffset 1800

    group snow1:
        attribute here default:
            "snow1"

    group snow2:
        attribute here default:
            "snow2"

image confrontationAnim:
    "staticSidewaysScene"
    animation
    xoffset -640
    ease 7.5 xoffset +640



image trailerRain = Fixed(SnowBlossom("gui/trailer_rain.png", count=25, xspeed=400, yspeed=900, start=0.2, fast=True))
image trailerRain2 = Fixed(SnowBlossom("gui/trailer_rain2.png", count=25, xspeed=400, yspeed=900, start=0.2, fast=True))
image trailerRain3 = Fixed(SnowBlossom("gui/trailer_rain3.png", count=25, xspeed=400, yspeed=900, start=0.2, fast=True))

image trailerMaria:
    "Capsule_Library_HeroONLYMARIA.png"
    zoom 0.5
    animation
    xalign 1.5
    easein 1.5 xalign 0.9

image trailerLogo:
    "Capsule Library Logo Hero.png"
    zoom 0.5

define logoDissolve = Dissolve(3)