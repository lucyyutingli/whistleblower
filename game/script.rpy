# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arreta", color="#bb0000")
define n = Character("non aretta", color="#c8ffc8")
define s = Character("seth", color="#ffc8c8")

define v1 = Character("Woman", color="#f587f5")
define v2 = Character("Man", color="#8591ff")

define narrator = Character(what_italic=True)

define am = Character("Arreta", what_italic=True, color="#bb0000")




# The game starts here.

label start:

    scene bg arretadesk

    narrator "Arreta stretches her arms back and lets out a sigh"

    a "That design report took so long to go over! Glad that the whole team seems to be on the same page now, though. I really can’t wait to see what the finished product looks like!"

    a "Oh, I forgot to pick up one of the documents from the printer that Marley sent me."

    narrator "Arreta gets up from her desk and starts walking to the next room. She pays particular attention to the sound of her shoes hitting the floor. She arrives at the printer and starts picking up papers."

    a "It gets so quiet here in the evening. Seems like no one's here, I ought to be heading out soon too."

    narrator "A door opens down the hall from the printer room. Arreta suddenly hears a man and woman talking, and tries to figure out what they're saying..."

    v1 "I really think we should go through with it anyways, Seth. It’s not like we’re the first ones being asked to do this kind of thing. The payment is incredibly generous, we can't turn this kind of thing down."

    v2 "I agree with what you’re saying, of course, but not everyone is on the same page. It’s so frustrating."

    narrator "Arreta leans in closer, intrigued by the conversation"

    v2 "Huh, I can’t find my keycard on me anywhere. Did you grab it when we were leaving the car?"

    v1 "Don’t look at me! You can't expect me to pick up after you all the time. This is the same thing that happened at the last office party."

    v2 "Yeah, it was July 20, my birthday party. You think you could cut a guy some slack... You know what, let’s just go back to the car for my keycard. Then we can discuss the project more in detail in my office."

    narrator "The two figures exit from the hall"


    menu:

        a "That sounded like my boss Seth and someone else talking about something suspicious, to say the least. Should I investigate further?"

        "Yes":
            jump choice1_yes

        "No":
            jump choice1_no

    label choice1_yes:

        $ investigate_choice_flag = True

        a "Yeah I'll just circle by Seth’s office and possibly ask a few questions."

        jump choice1_done

    label choice1_no:

        $ investigate_choice_flag = False

        a "Probably something that doesn't concern me. I should just head home."

        narrator "Arreta goes back to her car and drives home. She stays up late into the night wondering what the two figures could have possibly been talking about. By the following morning, it was no longer on her mind."

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

        scene bg office
        with fade
        play music "audio/noir.mp3" fadeout 1

        a "Maybe this was a bad idea, is it really logical to be snooping around your bosses office at night!? What if he found me? What would I say?"

        narrator "Arreta turns to leave, but before she can even step towards the door, she hears the sound of approaching footsteps"

        v1 "Do you have any snacks in your office? I'm starving."

        v2 "You’ve been in here hundreds of times, when have you ever seen me eating snacks in my office? We'll get dinner afterwards anyways."

        # narrator "Arretta’s mind races"



        am "What do I do? Should I hide? Should I run? God damn it, why did I get myself into this mess!"
        narrator "Despite the flurry of cluttered options present in her mind, her body only considers one and she decides to hide."


        menu:
            narrator "She hides..."

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
            stop music fadeout 0.8

            scene bg black
            play sound "audio/dooropen.mp3" volume 0.7
            narrator "the door opens..."








    # This ends the game.

    return
