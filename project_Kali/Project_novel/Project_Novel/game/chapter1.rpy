label chapter1:

    scene bg roof with fade

    show eel_dark at center with fade

    e "Welcome [p]"

    p "In rooftops?"

    show eel_happy at center

    e "Yep!, we are at the rooftops."

    p "why?"

    show eel_curios at center

    e "cuz, why not?"

    e "anyways! player please accept my precious gift~"

    show eel_happy at center

    show gun at truecenter

    p "a gun?"

    e "yep take it!"

    $ add_item("A gun", "items/gun.png")

    p "{alpha=0.5} breh what do i do with a gun?"

    e "try pointing it at me"

    e "Press 'I' to open you inventory"

    window hide

    $ renpy.call_screen("inventory")

    $ renpy.pause(1.0)  # Small delay to prevent input issues

    window show

    return