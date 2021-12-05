# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arreta", color="#bb0000")
define m = Character("Marley", color="#fd6dfd")
define s = Character("Seth", color="#6ece6e")

define v1 = Character("Woman", color="#fd6dfd")
define v2 = Character("Man", color="#6ece6e")



define narrator = Character(what_italic=True)

define am = Character("Arreta", what_italic=True, color="#bb0000")




# The game starts here.

label start:

    # Scene 1

    scene bg arretadesk

    narrator "Arreta stretches her arms back and lets out a sigh."

    a "That design report took so long to go over! Glad that the whole team seems to be on the same page now, though. I really can’t wait to see what the finished product looks like!"

    a "Oh, I forgot to pick up one of the documents from the printer that Marley sent me."

    narrator "Arreta gets up from her desk and starts walking to the next room. She pays particular attention to the sound of her shoes hitting the floor. She arrives at the printer and starts picking up papers."

    a "It gets so quiet here in the evening. Seems like no one's here, I ought to be heading out soon too."

    narrator "A door opens down the hall from the printer room. Arreta suddenly hears a man and woman talking, and tries to figure out what they're saying..."

    v1 "I really think we should go through with it anyways, Seth. It’s not like we’re the first ones being asked to do this kind of thing. The payment is incredibly generous, we can't turn this kind of thing down."

    v2 "I agree with what you’re saying, of course, but not everyone is on the same page. It’s so frustrating."

    narrator "Arreta leans in closer, intrigued by the conversation."

    v2 "Huh, I can’t find my keycard on me anywhere. Did you grab it when we were leaving the car?"

    v1 "Don’t look at me! You can't expect me to pick up after you all the time. This is the same thing that happened at the last office party."

    v2 "Yeah, it was July 20, my birthday party. You think you could cut a guy some slack... You know what, let’s just go back to the car for my keycard. Then we can discuss the project more in detail in my office."

    narrator "The two figures exit from the hall."


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
        play music "audio/noir.mp3" fadeout 1 volume 0.6

        a "Maybe this was a bad idea, is it really logical to be snooping around your bosses office at night!? What if he found me? What would I say?"

        narrator "Arreta turns to leave, but before she can even step towards the door, she hears the sound of approaching footsteps and the voices from before."

        v1 "Do you have any snacks in your office? I'm starving."

        s "You’ve been in here hundreds of times, when have you ever seen me eating snacks in my office? We'll get dinner afterwards anyways."

        # narrator "Arretta’s mind races"



        am "What do I do? Should I hide? Should I run? God damn it, why did I get myself into this mess!"
        narrator "Despite the flurry of cluttered options present in her mind, her body only confiders one and she decides to hide."


        menu:
            narrator "She hides..."

            "behind the fireplace":
                jump choice_fireplace

            "under the desk":
                jump choice_desk

            "in the closet":
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
            play sound "audio/dooropen.mp3" volume 0.3
            narrator "the door opens..."

            if hide_choice_flag == 2:
                "Arreta hides behind the fireplace in the corner of the room, trying to stay as quiet as possible to avoid detection."

                scene bg fireplace
                with fade
                play music "audio/noir.mp3" fadeout 1 volume 0.5

            if hide_choice_flag == 3:
                "Arreta hides under the desk, trying to stay as quiet as possible to avoid detection."

                scene bg desk
                with fade
                play music "audio/noir.mp3" fadeout 1 volume 0.5

            if hide_choice_flag == 4:
                "Arreta hides in the closet, trying to stay as quiet as possible to avoid detection."

                scene bg closet
                with fade
                play music "audio/noir.mp3" fadeout 1 volume 0.5

            v1 "Ah the door wasn't locked, we're a bit careless aren't we? Probably nothing to worry about though."
            s "I suppose so, why don't you have a seat?"

            if hide_choice_flag == 2:
                "Arreta strains her neck to peek past the fireplace, able to make out the two figures."
            if hide_choice_flag == 3:
                "Arreta peeks past the edge of the desk, able to make out the two figures."
            if hide_choice_flag == 4:
                "Arreta peeks through the closet panes, able to make out the two figures."

            am"Oh my god, is that Marley with Seth? What's she doing talking with him alone?"

            "Marley was Arreta's best friend in the office, having worked together at Omni Industries for years."

            m "Let's get to business, you need to fill me in on what's going on. Where are you in regards to talks with the company president?"

            s "I'm working on it. He's been hesitant to say the least. But I'm meeting with him later today and I think I'm close to swaying him to our side."

            m "I don't understand, what's taking him so long to decide? Does he think the program isn't up to par?"

            "Seth stands up from his chair and walks around the room, first passing by the closet lost in thought."

            if hide_choice_flag == 2:
                jump fireplace
            if hide_choice_flag == 3:
                jump desk
            if hide_choice_flag == 4:
                jump closet

            $ password_flag = False
            $ suitcase_key = False
            $ code = False
            $ combination = False

            label closet:
                s "No, I assured him that the encryption program is basically a finalized product. You did an amazing job assembling that on your own, by the way."

                "Marley stands up from her chair to confide in Seth."

                m "Well it wasn't easy figuring out how to complete the password failsafe feature. That took months of hard work... I'll still be compensated for it I hope?"

                s "I'll make sure of it. For your anonymity I never told him who developed the program, just in case he tries to shut down the program completely. Don't worry though, I have the 
                    records showing it was all your work."

                "The two walk over to the couches, using a keyboard and mouse to navigate the computer being displayed on the tv, getting farther away from Arreta. She struggles to hear some of their
                conversation."

                s "See? Right here..."

                m "Let me see."

                s "Yeah, it's right here behind this password..."

                "There is a faint sound of typing, and after a few seconds, Arreta can no longer see the glare from the tv screen."

                m "So if he's not worried about the program itself, what's the problem? Shouldn't the company be read to roll it out?"

                s "Well, he's worried it might hurt the company's brand if the public found out how we were handling their information."

                m "But we're doing the right thing here. It's all for the sake of the public's well-being."

                s "I agree, but he's hesitant... I'll promise him that I was assured the program would be used with due diligence."

                m "Remind me again, how did that meeting with him go?"

                s "Well, I flew down with my wife and thought I'd make a short vacation out of it... I barely needed to pack anything."

                m "Did you tell your wife about the meeting?"

                "Seth pauses."

                s "No, there's enough going on for her to worry about. We both have been a little worried for our safety as of late."

                "Seth pauses again to catches his breath."

                s "However, during the meeting, they seemed to be really enthused by the product when I explained the concept..."

                "Arreta tries but cannot hear the end of Seth's sentence."

                m "Jim shouldn't either."

                "Seth and Marley move back towards the empty fireplace."

                s "I'm confident this will all work out, Marley. We just need Jim's approval, and then we're all set... 
                With the right messaging, we can show the country how we're doing the right thing."

                "Seth leans against the couch as he continues talking."

                s "This can only mean upwards growth for you and the rest of the staff."

                m "Plus, she'd do a great job of selling the need for the new encryption of features."

                s "Exactly."

                "Seth and Marley continue talking about other office gossip and Arreta loses interest in their conversation. "

                am "While they're distracted, I wonder if there's any evidence I can find within the closet."

                menu:

                    narrator "Arreta looks around the closet. She decides to inspect the ..."

                    "suit jacket":
                        jump suitjacket

                    "suitcase":
                        jump suitcase

                label suitjacket:

                    scene bg closetletter

                    "Arreta reaches into the suit jacket pocket and finds an empty envelope."

                    am "Hm, the letter isn't here anymore, but it's clearly addressed to Mr. Platt and Ms. Asch."

                    jump office_cont

                label suitcase:

                    if suitcase_key == False:

                        "A small lock prevents Arreta from oppening the suitcase. She still looks at the outside of the suitcase."

                        am "A checked luggage tag to D.C. on June 14th. Wonder if that was for his week vacation?"

                        jump office_cont

                    else:
                        "Arreta inserts the key she found earlier. The suitcase opens. Inside are a pair of phones."

                        scene bg closetheadphones

                        am "It's not stealing if I give them back later right? These might come in handy."

                        "Arreta pockets the headphones."

                        jump office_cont



            label desk:
                s "No, I assured him that the encryption program is basically a finalized product."

                "Marley stands up from her chair to confide in Seth."

                "The two walk over to the couches, using a keyboard and mouse to navigate the computer being displayed on the tv, getting farther away from Arreta. She struggles to hear some of their
                conversation."

                s "See? Right here in the second, hidden folder."

                m "Let me see."

                s "Yeah, it's right here behind this password. It's my wife's maiden and a 7 at the end."

                am "Better keep a mental note of that. Might be useful later."

                $ password_flag = True

                "There is a faint sound of typing, and after a few seconds, Arreta can no longer see the glare from the tv screen."

                m "So if he's not worried about the program itself, what's the problem? Shouldn't the company be read to roll it out?"

                s "Well, he's worried it might hurt the company's brand if the public found out how we were handling their information."

                m "But we're doing the right thing here. It's all for the sake of the public's well-being."

                s "I agree, but he's hesitant. Working with the government always comes with some risks. 
                I'll promise him that I was assured the proram would be used with due diligence."

                m "Remind me again, how did that meeting with him go?"

                s "Well, I flew down with my wife and thought I'd make a short vacation out of it since the government willingly put us up in a nice
                hotel for two nights. I barely needed to pack anything."

                m "Did you tell your wife about the meeting?"

                "Seth pauses."

                s "No, there's enough going on for her to worry about. We both have been a little worried for our safety as of late."

                "Seth pasues again to catches his breath."

                s "However, during the meeting, they seemed to be really enthused by the product when I explained the concept. The FBI has been struggling
                to get into the domestic terrorist's phone for months now to look for more evidence. I don't want another repeat of that tragedy."

                m "Jim shouldn't either."

                "Seth and Marley move back towards the empty fireplace."

                s "I'm confident this will all work out, Marley. We just need Jim's approval, and then we're all set... 
                With the right messaging, we can show the country how we're doing the right thing."

                "Seth leans against the couch as he continues talking."

                s "This can only mean upwards growth for you and the rest of the staff."

                m "Plus, she'd do a great job of selling the need for the new encryption of features."

                s "Exactly."

                "Seth and Marley continue talking about other office gossip and Arreta loses interest in their conversation. "

                am "While they're distracted, I wonder if there's any evidence I can find within the desk."

                menu:

                    narrator "Arreta looks around the desk. She decides to inspect the ..."

                    "trash can":
                        jump trashcan

                    "drawer":
                        jump drawer

            label trashcan:

                "Arreta looks through the trash can and finds a crumpled note."

                scene bg desknote

                am "The note reads  \"code: birthday, so you don't forget.\" I wonder what that's for."

                "Arreta pockets the note."
                
                $ code = True

                jump office_cont

            label drawer:
                
                "Arreta slowly and quietly opens the desk drawer, finding a small key."

                am "Hm, this is an extremely small key, definitely too small for a door. Maybe a small lock?"

                "Arreta pockets the key."

                $ suitcase_key = True

                jump office_cont

                
            label fireplace:
                s "No, I assured him that the encryption program is basically a finalized product."

                "Marley stands up from her chair to confide in Seth."

                "The two walk over to the couches, using a keyboard and mouse to navigate the computer being displayed on the tv, getting farther away from Arreta. She struggles to hear some of their
                conversation."

                s "See? Right here..."

                m "Let me see."

                s "Yeah, it's right here behind this password..."

                $ password_flag = True

                "There is a faint sound of typing, and after a few seconds, Arreta can no longer see the glare from the tv screen."

                m "So if he's not worried about the program itself, what's the problem? Shouldn't the company be read to roll it out?"

                s "Well, he's worried it might hurt the company's brand if the public found out how we were handling their information."

                m "But we're doing the right thing here. It's all for the sake of the public's well-being."

                s "I agree, but he's hesitant.
                I'll promise him that I was assured the proram would be used with due diligence."

                m "Remind me again, how did that meeting with him go?"

                s "Well, I flew down with my wife and thought I'd make a short vacation out of it... I barely needed to pack anything."

                m "Did you tell your wife about the meeting?"

                "Seth pauses."

                s "No, there's enough going on for her to worry about. We both have been a little worried for our safety as of late."

                "Seth pasues again to catches his breath."

                s "However, during the meeting, they seemed to be really enthused by the product when I explained the concept..."

                "Arreta tries but cannot hear the end of Seth's sentence."

                m "Jim shouldn't either."

                "Seth and Marley move back towards the empty fireplace."

                s "I'm confident this will all work out, Marley. We just need Jim's approval, and then we're all set. We can only go up from here with such a 
                lucrative contract. One billion dollars already invested to develop the program. Imagine how much more we could get when we finally sell or license the product.
                The investors will eat that up! 
                With the right messaging, we can show the country how we're doing the right thing."

                "Seth leans against the couch as he continues talking."

                s "This can only mean upwards growth for you and the rest of the staff. Arreta's already due for a 
                promotion. And the fact that she has no ties to the project means she's an uncontroversial choice to become
                head of the marketing division."

                m "Plus, she'd do a great job of selling the need for the new encryption of features."

                s "Exactly."

                "Seth and Marley continue talking about other office gossip and Arreta loses interest in their conversation. "

                am "While they're distracted, I wonder if there's any evidence I can find around the fireplace."

                menu:

                    narrator "Arreta looks around the fireplace. She decides to inspect the ..."

                    "bookshelf":
                        jump bookshelf

                    "painting on the wall":
                        jump p_frame

            label bookshelf:

                "Arreta peeks at the bookshelf from her position and sees a small paper sticking out of a book. She quickly and quietly pulls it out."

                scene bg fireplacecheck

                am "Oh a check. \"$1 billion to Seth Platt from Mr. Ancor\". Holy shit that's a lot of money. I know it would be illegal to cash 
                this check, but wow. That's enough to cover my rent one hundred times over. Who's Mr. Ancor? An investor maybe?"

                "Arreta pockets the check."

                jump office_cont

            label p_frame:
                
                "Arreta leans in and takes a closer look at the painting."

                am "That's strange, it looks like there a hinge running along the edge of the painting frame. "

                "Arreta moves closer to inspect. At the bottom of the painting are four numbers with a small LED screen."

                am "Huh, it's some kind of combination. It seems I have three chances before it locks me out."

                if combination == False:
                    "Arreta tries but fails to guess the combination."

                    am "That sucks. Maybe I should try again after Seth and Marley leaves."

                else:
                    scene bg fireplaceplanner

                    "Arreta remembers the combination from earlier and is able to open the painting. She finds a small day planner. "

                    am "Intersting, it seems four dates are marked. May 5, June 14, October 7, and November 28. I'll be sure to keep a mental note of that."


                $ suitcase_key = True

                jump office_cont


        label office_cont:

            "Arreta hears movement and looks back at Seth and Marley."

            scene bg office
            with fade

            "Seth and Marley stand up and walk to the door."

            s "I need to circle back with my boss in a few minutes, but how about I walk you back to the car first?"

            m "I'd like that."

            "The two pause in the door way, before Seth leans over and kisses Marley, they then ..."

            am "Excuse me what?? What are they doing??"

            "Arreta rubs her eyes to clear any possible debris."

            am "Nope, they're definitely kissing. To think Seth is cheating on his wife with Marley...
            and Marley didn't even tell me! UGH. What kind of friend doesn't tell you that they're dating
            your boss and making him cheat on his wife??"

            "The two leave and Arreta is left alone in the room by herself."

            am "I've got a few minutes, maybe there are some other things that I can find while Seth's gone. I probably only have time to look in two places."

            jump clue_choices


            label clue_choices:    

                menu:

                    am "I should go to the..."

                    "computer desk":
                        jump computer

                    "paintings":
                        jump paintings

                    "conference table":
                        jump c_table


            label computer:
                menu:
                    narrator "Arreta looks at..."
                    
                    "picture":
                        am "It's Seth and his wife Amber posing with their cat Mr. Pickles, how cute."

                        jump computer

                    "computer":

                        narrator "Arreta boots up the computer"

                        menu:

                            am "Which folder should I look through?"

                            "Important_work"
                
        






    # This ends the game.

    return
