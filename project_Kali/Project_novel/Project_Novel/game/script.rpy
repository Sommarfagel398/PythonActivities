# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
label start:

    $ player_name = renpy.input("Enter your name: ").strip()

    if player_name == "":
        $ player_name = "Alex"

    $ p = Character("[player_name]")

    p "..."
    p "..."
    p "..."

    m1 "wake up... [player_name]"

    scene bg room with glitch

    e "hai~"

    "A loud breathing can be heard, as you open your eyes. A shadow figure in a form of female surprises you"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show shadow with glitch
    # These display lines of dialogue.
    e "Wakey wakey!"

    p "what the hell...?"

    e "Yes hell!...Ahem by the way name's [e]"

    e "Before we start the yk stuff testing, may I know if you're [player_name]?"

    window hide
    pause 0.5
    window show

    menu:

        "Yeah, I am":
            $ player_choice = "Yeah, I am"
            p "Yeah, I am [player_name]."
        "I don't know?":
            $ player_choice = "I don't know?"
            p "I actually don't know what I just named my character... my bad, I guess?"

    if player_choice == "Yeah, I am":
        e "Great! My name is Eileen. I'm your assistant in this story progress."
        jump back_to_topic

    elif player_choice == "I don't know?":
        e "...Oh, okay? That sucks... or are you just teasing me [player_name]?"
        jump ydk

label ydk:
        p "why would i tease you?"

        e "Because why not? or is it just me and my own world assumptions?"

        p "uh what?"

        e "Nvm! slow thinker"

        jump back_to_topic

label back_to_topic:

    e "So... back to topic. Have you ever played a novel game before?"

    menu:
        "Yeah, I do":
            $ player_choice = "I do"
            p "I do"

        "Nope, never tried it before":
            $ player_choice = "Nope, never tried it before"
            p "Nope, never tried a novel game before."

    if player_choice == "I do":
        e "Great! A weirdo!"
        jump back_to_topic1
    elif player_choice == "Nope, never tried it before":
        e "Uh, cool?"
        jump back_to_topic1

label back_to_topic1:

    e "Anyways! [player_name], let's get started!"

    jump chapter1
    return
