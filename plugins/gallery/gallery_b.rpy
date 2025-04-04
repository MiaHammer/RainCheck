screen gallery_b():
    tag menu
    add "GalleryBGStretch"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25 
            
            add gallery.make_button("room", unlocked = im.Scale("bg desk.png",234,132), locked = "locked.jpg")
            add gallery.make_button("stairs", unlocked = im.Scale("bg stairs.png",234,132), locked = "locked.jpg")
            add gallery.make_button("streets", unlocked = im.Scale("bg streets.png",234,132), locked = "locked.jpg")
            add gallery.make_button("bakery", unlocked = im.Scale("bg bakery.png",234,132), locked = "locked.jpg")
           