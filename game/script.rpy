# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("arreta", color="#0000ff")
define n = Character("non aretta", color="#c8ffc8")
define s = Character("seth", color="#ffc8c8")

define v1 = Character("???", color="#c8ffc8")
define v2 = Character("???", color="#ffc8c8")

define narrator = Character(what_italic=True)

define am = Character("arreta", what_italic=True, color="#ffcccc")




# The game starts here.

label start:

    scene bg arretadesk

    narrator "Arreta stretches her arms back and lets out a sigh"

    a "That design report took so long to go over! Glad that the whole team seems to be on the same page now, though. I really can’t wait to see what the finished product looks like!"

    a "Oh, I forgot to pick up one of the documents from the printer that Marley sent me."

    narrator "Arreta gets up from her desk and starts walking to the next room. She pays particular attention to the sound of her shoes hitting the floor. She arrives at the printer and starts picking up papers."

    a "It gets so quiet here in the evening. Well, I ought to be heading out soon too."

    narrator "A door opens down one of the halls from the printer room accompanied with the sound of several footsteps.
    Arreta hears a voice, but it is very muffled"

    v1 "I really think we should go through with it anyways, Seth. It’s not like we’re the first ones being asked to do this kind of thing. The payment is incredibly… generous, as well."

    v2 "I agree with what you’re saying, of course, but not everyone is on the same page. It’s so frustrating…"

    narrator "Arreta strains to make out what the two figures are discussing"

    v2 "Huh, I can’t find my keycard on me anywhere. Did you grab it when we were leaving?"

    v1 "Don’t look at me! You can't expect me to pick up after you all the time. This is the same thing that happened at the last office party."

    v2 "Yeah, it was July 20! My birthday. Can’t you cut a guy a break for being a bit absent-minded at his own birthday par– . You know what, let’s just check in my car for the card. Then we can discuss the project more in detail in my office, away from prying ears."

    narrator "The two figures exit from the room"


    menu:

        a "That sounded like Seth, my boss, and someone else talking about… something suspicious, that’s for sure. Maybe I should investigate further?"

        "Yes":
            jump choice1_yes

        "No":
            jump choice1_no

    label choice1_yes:

        $ investigate_choice_flag = True

        a "Yeah I should just circle by Seth’s office, and possibly ask a few questions."

        jump choice1_done

    label choice1_no:

        $ investigate_choice_flag = False

        a "Well, maybe this doesn’t concern me at all. I should just head home."

        narrator "Arreta went back to her car and drove home. She stayed up late into the night wondering what the two figures could have possibly been talking about. But by the following morning, it was no longer on her mind."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

    if investigate_choice_flag:

        narrator "Arreta locks up her office, making sure to pack all her belongings. She carefully tip toes over the Director’s room and looks around."

        jump office

    else:
        scene bg notend

        narrator "Arreta's story ends here, but what are the implications of this choice? There may very well be more to uncover..."
        jump start

    label office:

        play music "audio/noir.mp3" fadeout 1
        scene bg office

        a "Wait what am I doing? Is it really logical to be snooping around your bosses office at night? What if he found me? What would I say?"

        narrator "Arreta turns to leave, but before she can even step towards the door, she hears the loud sound of approaching footsteps"

        v1 "Do you have any snacks in your office? I'm starving"

        v2 "When have you ever seen me eating snacks in my office? You’ve been in here hundreds of times."

        narrator "Arretta’s mind races."


        stop music fadeout 1

        am "What do I do? Should I hide? Make some excuse? Agghhhh"
        narrator "Despite the flurry of cluttered options present in her mind, her body only considers one."


        menu:
            narrator "she hides..."

            "Behind the Fireplace":
                jump choice_fireplace

            "Under the Desk":
                jump choice_desk

            "In the Closet":
                jump choice_closet

        label choice_fireplace:
            $ hide_choice_flag = 2


            jump hide_choice_done

        label choice_desk:
            $ hide_choice_flag = 3


            jump hide_choice_done

        label choice_closet:
            $ hide_choice_flag = 4


            jump hide_choice_done


        label hide_choice_done:

            scene bg black
            play sound "audio/dooropen.mp3"
            narrator "the door opens..."








    # This ends the game.

    return
