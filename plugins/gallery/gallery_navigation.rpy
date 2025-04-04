screen gallery_navigation():
    vbox:
        style_prefix "gallery"
        xoffset - 50
        spacing 20
        textbutton "Characters" action ShowMenu("gallery_a") 
        textbutton "Backgrounds" action ShowMenu("gallery_b") 
        textbutton "CGs" action ShowMenu("gallery_c")
        textbutton "CGs 2" action ShowMenu("gallery_d")
        textbutton "Cow Clicker":
            sensitive persistent.galUnlock
            action ShowMenu("gallery_cow")
        showif not persistent.galUnlock:
            label "Try getting more cows!"
        
        textbutton "Return":
            action Return()
            yoffset 100

style gallery_button_text:
    idle_color "#808080"
    hover_color "#E17BA2"
    selected_color "#AA1945"
    insensitive_color "#404040"
    size 33