screen gallery_cow():
    tag menu
    add "GalleryBGStretch"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25

            add gallery.make_button("cow", unlocked = im.Crop(im.Scale("images/boi clique/kaoriginal.png", 234, 234), 0, 0, 234,132), locked = "locked.jpg")
            add gallery.make_button("cowBG", unlocked = im.Scale("images/boi clique/pasture.png",234,132), locked = "locked.jpg")
            add gallery.make_button("milk", unlocked = im.Scale("images/boi clique/milkriginal.png",66,132), locked = "locked.jpg")
            add gallery.make_button("cowui", unlocked = im.Scale("images/boi clique/button.png",234,132), locked = "locked.jpg")
            add gallery.make_button("ufo", unlocked = im.Crop(im.Scale("images/boi clique/ufo.png", 234, 190), 0, 0, 234,132), locked = "locked.jpg")
            add gallery.make_button("bonusmaria", unlocked = im.Crop(im.Scale("MariaRaincheckScaled.png",234,312), 0, 0, 234,132), locked = "locked.jpg")