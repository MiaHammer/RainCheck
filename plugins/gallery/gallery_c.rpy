screen gallery_c():
    tag menu
    add "GalleryBGStretch"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25

            add gallery.make_button("train", unlocked = im.Scale("BoiSubwayFULL.png",234,132), locked = "locked.jpg")
            add gallery.make_button("call", unlocked = im.Scale("cg MariaAndAnnieCall1.png",234,132), locked = "locked.jpg")
            add gallery.make_button("notiz", unlocked = im.Scale("cg Der Notizblock.png",234,132), locked = "locked.jpg")
            add gallery.make_button("streetwindow", unlocked = im.Scale("cg sidewalk.png",234,132), locked = "locked.jpg")
            add gallery.make_button("ninjas", unlocked = im.Scale("cg Ninjas.png",234,132), locked = "locked.jpg")
            add gallery.make_button("strangle", unlocked = im.Scale("cg Strangling Hands.png",234,132), locked = "locked.jpg")