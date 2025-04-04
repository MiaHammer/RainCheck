screen gallery_a():
    tag menu
    add "GalleryBGStretch"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation

        grid 3 2:
            spacing 25 
            
            add gallery.make_button("maria", unlocked = im.Crop(im.Scale("Maria3.png", 234, 234), 0, 32, 234,132), locked = "locked.jpg")
            add gallery.make_button("figure", unlocked = im.Crop(im.Scale("char Raincoat.png", 234, 486), 0, 0, 234,132), locked = "locked.jpg")
            add gallery.make_button("annie", unlocked = im.Crop(im.Scale("Annie1.png", 234, 234), 0, 64, 234,132))
            add gallery.make_button("phone", unlocked = im.Crop(im.Scale("phone.png", 234, 234), 0, 32, 234,132))
           