screen inventory():
    modal True  # Prevents interaction with the background
    frame:
        align (0.5, 0.5)  # Centers the inventory
        xsize 400
        ysize 300
        background "#222"  # Dark gray background

        vbox:
            spacing 10
            text "Inventory" size 40 color "#FFF"  # White title
            for item in inventory:
                text item["name"] color "#FFF"
                add item["image"] xalign 0.5  # Centers the image

            textbutton "Close" action Hide("inventory") xalign 0.5

init python:
    def add_item(name, image):
        inventory.append({"name": name, "image": image})

    config.keymap["inventory"] = ["i"]  # Press 'I' to open inventory