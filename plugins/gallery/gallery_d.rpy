screen gallery_d():
    tag menu
    add "GalleryBGStretch"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25
            
            add gallery.make_button("alien", unlocked = im.Scale("cg BoiAlien.png",234,132), locked = "locked.jpg")
            add gallery.make_button("gecko", unlocked = im.Scale("cg Gecko.png",234,132), locked = "locked.jpg")
            add gallery.make_button("forest", unlocked = im.Scale("cg ForestCrazy.png",234,132), locked = "locked.jpg")
            add gallery.make_button("slime", unlocked = im.Scale("cg Slime.png",234,132), locked = "locked.jpg")
            add gallery.make_button("meeting", unlocked = im.Scale(im.Crop("MariaWalkingStreet.png", 1280, 0, 1280, 720),234,132), locked = "locked.jpg")
            add gallery.make_button("hope", unlocked = im.Scale("cg Hope.png",234,132), locked = "locked.jpg")