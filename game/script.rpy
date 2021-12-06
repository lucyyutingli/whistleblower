# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Arreta", color="#bb0000")
define m = Character("Marley", color="#fd6dfd")
define s = Character("Seth", color="#6ece6e")
define j = Character("Jim", color="#ff6c00")

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

# Hiding #1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

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

            default password_flag = False
            default suitcase_key = False
            default code = False
            default combination = False
            default usb = False

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

# Clues #1 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            label clue_choices:    

                menu:

                    am "I should go to the..."

                    "computer desk":
                        jump computer
                        scene bg seth computer

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

                                # "Important_work"

                if scene_num == 6:
                    jump scene_6
                    
        

# Hide #2 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        label hide_2:

            $ hide_2 = 0
            menu:
                narrator "Arreta hears Seth's footsteps and quickly goes to find a new hiding spot. She hides..."

                "behind the fireplace":
                    $ hide_2 = 1

                "under the desk":
                    $ hide_2 = 2

                "in the closet":
                    $ hide_2 = 3


            "The scuffle of rubber can be heard as Seth enters the room again wearing his crocs. He is alone this time."

            if hide_2 == 2:
                "Seth walks over to the couches and turn on the tv. He then walks over to the conference table and begins dialing a number and puts it on speaker phone."

                "Arreta peaks from behind the desk to look at the tv screen. IT appears Seth is recording his current phone conversation."

                am " Seems a bit overly paranoid to me. But I suppose the nature of this new project warrants that kind of cautiousness. "

            else:
                "Seth walks over to the couches and turn on the tv. He then walks over to the conference table and begins dialing a number and puts it on speaker phone."

                am "It looks like Seth is typing something on the keyboard but I can't see from my angle. "

            s "Hey Jim! Pleasure talking to you today. "

            j "Glad to talk to you too, Seth. Was hoping you could walk me through your program proposal and the nature of the deal."

            s "Certainly, certainly."

            "Seth walks over toward the end of the room near the closet. "

            if hide_2 == 3:

                s "Marley and I have been working on something big the last couple of months. It looks fully operational and ready to roll out. 
                I think you’ll be excited. This is going to save lives and reflect well on our company, not to mention the massive subsidies we’ll receive."

            else:

                s "...It looks fully operational and ready to roll out 
                I think you’ll be excited. This is going to save lives and reflect well on our company, not to mention the massive subsidies we’ll receive."


            if hide_2 == 3:
                j "I’m aware of the “benefits” you claim this project will net the company. I can’t say I’m convinced yet.
                But even before we go into that, are you sure you’re not overestimating the efficacy of the product? 
                The relationship between you and {i}that woman{/i} may be complicating your view on it."
            else:
                j "I’m aware of the “benefits” you claim this project will net the company. I can’t say I’m convinced yet.
                But even before we go into that, are you sure you’re not overestimating the efficacy of the product?..."

            if hide_2 == 1:
                "Seth is visibly shaken by the comment. He fiddles with a USB drive in his hand. "

            if hide_2 == 2:
                "Seth is visibly shaken by the comment. He pauses before continuing. "
            if hide_2 == 3:
                "Seth is visibly shaken by the comment. His shoulders slouch as he pauses. "

            if hide_2 == 3:
                s "That has nothing to do with my ability to assess the de-encryption service, I can promise you. And for that matter, our relationship has been cleared by HR. I would just rather it was not made public.
                In terms of the program itself, I can speak more extensively about recent testing and its practical applications."
            else:
                s "... In terms of the program itself, I can speak more extensively about recent testing and its practical applications."

            j "Go ahead. "

            if hide_2 == 3:
                s "I personally oversaw early testing. Marley ran the program on several mock devices. I think that with a bit more testing it will be nearly completed if we want to go public."
            else:
                s "I personally oversaw early testing... I think that with a bit more testing it will be nearly completed if we want to go public."

            "Seth walks back over towards his desk. "

            if hide_2 == 2:
                s "None of that information, of course, has been publicized. The government has no idea where we are specifically on the project creation. For all they know, we may be considering dropping it."

                j "Which I am currently for."

                s "Jim, I’d beg you to consider the social good we’ll be doing with this product. 
                I met with some of the FBI heads a fews months ago like we discussed and heard their case. 
                I was skeptical at first, just like you. But their reasoning holds."

                j "Well what about our consumers, Seth? Don't they have a right to privacy? I don't want to be seen as the bad guy here."

                s "And they have a right to safety too. We can provide them both. I was told that they would only seek to use the de-encryption program when holding a warrant. And only in the most extenuating circumstances."

            else:
                s "None of that information, of course, has been publicized... For all they know, we may be considering dropping it."

                j "Which I am currently for."

                s "Jim, I’d beg you to consider the social good we’ll be doing with this product...
                I was skeptical at first, just like you. But their reasoning holds."

                j "Well what about our consumers, Seth? Don't they have a right to privacy? I don't want to be seen as the bad guy here."

            j "Let's just say that you're right, that we're protecting our consumers. What makes you think that this still won’t blow up in our faces? 
            We already ran a risk by developing the program. The press can spin this any way they want to."

            if hide_2 == 1:
                "Seth grabs the phone from the desk and stands up. He places a USB on the desk behind him."

                s "And we’ll beat it. Our investors should be thrilled to know who we are partnering with. 
                We already received some money under the table. The sellout would be amazing. 
                Not to mention that immediately once it starts getting put to use, we’ll get good press to drown out any criticisms."

            else:
                "Seth grabs the phone from the desk and stands up..."

                s "And we’ll beat it. Our investors should be thrilled...
                Not to mention that immediately once it starts getting put to use, we’ll get good press to drown out any criticisms."

            j "..."

            s "..."

            j "How long until it's operational?"

            s "One month. I can promise you, one month is all we need. "

            j "I don't want any hiccups before then. If anyone leaks, everything comes to a halt, and all we get is bad press. "

            s "I can assure you, that this will all stay confidential. Among the only people that know about this,
            I'm the only one with incriminating evience, and I've locked it away behind lock and key."

            j "An encrypted lock like the kinds you're trying to break?"

            s "Haha, yes I suppose so Jim."

            j "And you're sure of this?"

            if hide_2 == 1:
                s "I am. And just to be safe, I’ll continue reviewing the rest of my staff. 
                They’re fiercely loyal sir, none of them newer than a few years. 
                Plus, most of them are due a raise of some kind soon. They have no incentive to leak. 
                I’ll talk them out of it even if they try."
            
            else:
                s "I am. And just to be safe, I’ll continue reviewing the rest of my staff. 
                They’re fiercely loyal sir..."

            j "That's good to hear... Let's meete again once you've finalized the program. I think it's high time we move ahead with the deal."

            s "Glad you've come around. Let's talk more about this soon. "

            j "Sure, see you. "

            if hide_2 == 2:

                "Seth turns off the phone and gets up to leave. He turns off the audio recording on his computer. 
                But leaves his bag behind. The room is now empty save for Arreta, hiding in the desk."

            if hide_2 == 1:

                "Seth turns off the phone and gets up to leave... 
                But leaves his bag behind. The room is now empty save for Arreta, hiding behind the fireplace."

            if hide_2 == 3:
                "Seth turns off the phone and gets up to leave... 
                But leaves his bag behind. The room is now empty save for Arreta, hiding in the closet."

            am "I probably should take one last look around and leave before he gets back, I probably have limited time. Where should I look?"

            $ scene_num = 6

            jump clue_choices

# Scene 6: Seth Confrontation -----------------------------------------------------------------------------------------------------------------------------------------------------

    label scene_6:
    
        menu:
            am "Something still feels off about all of this... Should I confront Seth to ask about his reasoning? Or just go or mull over my options for tomorrow?"

            "talk to Seth":
                jump seth_confront

            "go home":
                am "It's been a long day, I'll just home and take a breather for now."

        label seth_confront:
            am "I think I need some answers from Seth. I'm just gonna give him a call now."

            "Arreta dials Seth, anxiously waiting for his answer. "

            s "Hello? Arreta? What are you doing calling at this hour?"

            am "Play it cool, I don't need to tell him anything yet, and definitely not that I was sneaking around his room."
        
            s "Hello? Arreta?"

            a "I heard some chatter at work about an encryption program. What's that all about?"

            s "You heard... Who did you hear this from?"

            menu:
                "Nobody in particular.":
                    s "Really? Tell me the truth Arreta. There has to be someone. "

                    menu:
                        am "What should I say?"

                        "From someone close to me":
                            s "As in Marley?? "

                            a "Not explicitly. But I could tell something was up based on how she was acting."

                        "No one important":
                            s "Hm. Fine."

                            a "You’ve been acting really strange lately. And I overheard you talking to someone about encryption software earlier today."

                "From someone close to me.":
                    s "As in Marley?? "

                    a "Not explicitly. But I could tell something was up based on how she was acting."

                        
            s "What do you happen to know about in particular?"

            menu :

                am "Time to make my decision about what to confront Seth about. I only have one shot at this. I'll confront him about..."

                "working with the government to break user's privacy for national security.":
                    jump gov_choice

                "him and Marley working together, and not necessarily keeping it all professional. "
                    jump seth_marley_choice

                "planning to test loyalty of staff to make sure they don't leak information. "
                    jump loyalty_choice

                "selling users data to the highest bidder, and Jim's onboard. "
                    jump bid_choice

                "not having any dogs. "
                    jump dog_choice
        
        label gov_choice:

            s "It’s not that simple Aretta. We’re not just selling this to anybody. I know you’ll get on board once I explain what we’re doing."

            s "I get that you might be ancy about the government being able to access user’s data. But this is supposed to be a one time thing. 
            We’re creating a backdoor where we can investigate real criminals. The worst kind. 
            The ones who commit terrorist attacks and might have incriminating evidence, or ties to co-conspirators that we can only determine with this program. "

            default gov_a = False
            default gov_b = False
            default gov_c = False
            default gov_d = False
            

            menu arreta_gov:
                am "I still want more information. What to ask him..."

                "How can you be sure the backdoor won't be opened by the wrong people?" if gov_a == False:
                    $ gov_a = True
                    s "There will always be hackers out there trying to get into our servers. That’s why we have people like your friend Marley are continuously working on software updates. "

                    s "Yeah, this backdoor might invite some risk to start, but I’m positive we’ll be able to close any gaps extremely quickly. 
                    Not to mention, we can make even more positive change to outweigh those bumps almost immediately once the program’s operational. Isn’t that a worthwhile venture?"

                    a "Hard to say."

                    jump arreta_gov

                "Why should we trust the government on this?" if gov_b == False:
                    $gov_b = True

                    s "Well, why do we allow the government to search our homes? If they have a warrant and reasonable grounds to suspect an imminent threat, 
                    they should be able do conduct a thorough search. Why shouldn’t the same apply to our devices?"

                    s" I’m not gonna allow the government to use this arbitrarily. I can agree with you this is all about upholding the rule of law. Right?"

                    a "It's too early to tell. "

                    jump arreta_gov

                "Don't our users deserve to have a say in their own privacy?" if gov_c == False:
                    $gov_c = True

                    s "Of course. For the average person this wont change anything. And its not as if we won’t make people aware that we are developing this program. 
                    We’ll make sure to put out a report when we’re ready. And I want you to help with that."

                    s"You’re a crucial part of our media team, Arreta, and I think you could really help us with this. Are you interested?"

                    a "That's not something I can answer right now."

                    jump arreta_gov

                "What about our competitors?" if gov_d == False:
                    $gov_d = True

                    s "What about them?"

                    default d_2_1 = False
                    default d_2_2 = False

                    menu d_2:

                        "What if they follow our lead?" if d_2_1 == False:
                            $d_2_1 = True

                            s "The government will make similar demands on them too. And they might rush developing their equivalent program. 
                            We have a responsibility as the first company to potentially do this. Shouldn’t we stop, or at least try to slow down and avoid running that risk?"

                            jump d_2

                        "How do we know they won't capitalize on public outcry?" if d_2_2 == False:
                            d_2_2 = True

                            s "It’s not a winning narrative to say that we’re the only company that sells your information to the government."

                            jump d_2

                    jump arreta_gov

            jump scene_6_final

        label seth_marley_choice:
            s "You know about that... Okay. I need to set the record straight. "

            default marley_a = False
            default marley_b = False
            default marley_c = False

            menu arreta_marley:
                a "About what? That you're..."

                "cheating on your wife with a co-worker? I couldn't before but I can believe it now." if marley_a == False:
                    $marley_a = True

                    s "I… Look, it’s all been cleared by HR. But please, don’t tell anyone about this. It could put Marley and I in a bad situation when she’s due for a promotion."

                    s " I promise you though, her and my relationship doesn’t affect the nature of our work on this project. We both believe in the mission. "

                    jump arreta_marley
                "using your relationship with Marley toget her to do your dirty work?" if marley_b == False:
                    marley_b = True

                    s " No. Of course not! Say what you will about our relationship, but that all happens outside of the office. 
                    She joined because she genuinely believes in the same mission as I do. I asked her to help because she was the best person for the job. "

                    s "I can’t go into all the details, but the project is being conducted with collaboration from the government. We’re creating a backdoor where we can investigate real criminals. 
                    The worst kind. The ones who commit terrorist attacks and might have incriminating evidence, or ties to co-conspirators that we can only determine only this program."

                    jump arreta_marley

            default seth_a = False
            default seth_b = False

            menu arreta_seth:
                am "I still don't feel great about this. What should I ask next?"

                "How can you be sure you're not putting yourself and Marley at risk?" if seth_a == False:
                    seth_a = True

                    s " I can promise you, Marley and I won’t be in danger. Her involvement will be anonymous, unless she wants to go public. 
                    And the higher-ups will show loyalty to us two for taking the lead on the project. "

                    s "Plus, that’s why I want you to head the media team moving forward. You do amazing work, and you could help us explain why we’re doing the right thing for the country. 
                    You know, just like I’m doing now."

                    jump arreta_seth

                "Why should I trust you seth?" if seth_b == False:
                    seth_b = True

                    a " First, an inter-office relationship. Next, a secret government-sponsored program… You’ve been keeping secrets from the whole office. 
                    So why should the rest of us have faith in something we’ve been in the dark about?"

                    s "I understand… You can trust that I’m doing what’s best for the company. The entire staff included. It’s not as if I’m doing this unilaterally and stringing Marley along. 
                    The board, the… not to name names… but our company heads are behind this. They had me oversee contact with the government for a long while. "

                    s "Besides, can I trust you? To be quite about this whole thing? And my relationship with Marley? We both don’t want her to get hurt. "

                    jump arreta_seth

            jump scene_6_final

        label loyalty_choice:
            s "Loyalty? No, this isn’t about loyalty. It’s about commitment to the team. The project you’re referring to is extremely sensitive material that we can’t just have leaking to the public."

            s "Not only would it jeopardize our entire company if word got out ahead of time, but the government might need to step in. 
            It’s important that you trust the process, especially when you’re so close to being promoted. "

            s "I can’t explain all the details, but there’s more to the story. The project is being conducted with collaboration from the government. We’re creating a backdoor where we can investigate real criminals. 
            The worst kind. The ones who commit terrorist attacks and might have incriminating evidence, or ties to co-conspirators that we can only determine only this program."

            default loyal_a = False
            default loyal_b = False

            menu arreta_loyalty:
                am "Not good enough, I still need to ask more."

                "Are you threatening me to stay quiet on this?" if loyal_a == False:
                    $loyal_a = True

                    s "Of course not! I’m just saying that I can’t personally protect you if you leaked information.Our higher-ups have a real vested interest in keeping this on the down-low. 
                    I need to report to them on how things are going or else I’m the one in trouble. "

                    s "What I can promise though is that if something does leak. I’ll back you up so long as you promise me now that you won’t say anything. Is that a deal?"

                    jump arreta_loyalty

                "Why don’t you have faith in me and my abilities? We've worked together for a while now. " if loyal_b == False:
                    $loyal_b = True

                    s "Of course I have faith in you. That’s why I want to promote you to the head of the media team. 
                    I suspect we’re gonna make a public statement eventually about the de-encryption project. You’d be the best for resolving that problem."

                    jump arreta_loyalty


            jump scene_6_final

        label bid_choice:
            
            s "Don't make such wild accusations!"

            "Arreta can hear the anger in Seth's voice as he takes a breath to calm down. "

            s "You don’t know at all what is we’re doing… Do you really think I’m the type of person to throw the company under the bus for my own self interests? "

            default bid_a = False 
            default bid_b = False 

            menu arreta_bid:

                am "What should I say?"

                "Maybe! I don't know what to believe anymore. " if bid_a == False:

                    bid_a = True

                    s " Think for a second Aretta! Why would Jim, the fucking CEO of the company, also be willing to sell information that could destroy our credibility. "

                    a "Well then what's going on? I don't understand."

                    s " I can’t explain all the details, but the project is being conducted in collaboration with the government. It’s perfectly legal and most of all, safe. "

                    s "We’re creating a backdoor where we can investigate real criminals. The worst kind. 
                    The ones who commit terrorist attacks and might have incriminating evidence, or ties to co-conspirators that we can only determine only this program."

                    jump arreta_bid

                "No, that's why I'm so confused. " if bid_b == False:
                    bid_b = True

                    a " I just want some clarity so I can have some peace of mind."

                    s "I can’t explain all the details, but there’s more to the story. The project is being conducted in collaboration with the government. We’re creating a backdoor where we can investigate real criminals. "

                    s "The worst kind. The ones who commit terrorist attacks and might have incriminating evidence, or ties to co-conspirators that we can only determine only this program. 
                    I’m sure you understand why that’s important. I promise you, this is all in service of the public, and Jim agrees."

                    jump arreta_bid

            jump scene_6_final

        label dog_choice:
            
            "Seth starts to laugh on the phone"

            s "I'm not a dog-person, as you know. What are you..."

            "Seth takes a pause before realizing what Arreta was referring to."

            a "Yes, I saw you have some \“dog pictures\” on your computer."

            s "What do you mean by that. "

            default dog_a = False
            default dog_b = False

            menu arreta_dog:
                am "What should I talk about?"

                "How come you never shared any pictures with the rest of the office?" if dog_a == False:
                    dog_a = True

                    a "How come you never shared any pictures with the rest of the office?"

                    s "..."
                    s "Oh, yeah, haha! Marley and I have been competing to find the cutest dog pictures online. I can’t let her sneak in and steal one from my hoard. "

                    menu seth_dog:

                        s "Was there anything else you wanted to ask me about?"

                        "Yeah the pictures. I couldn't resist and had to look for myself. " if password_flag == True:
                            jump dog_b

                        "Nope! That's all":
                            jump scene_7


                "I know all about the de-encryption program." if password_flag == True:
                    jump dog_b

                label dog_b:
                    a "I know about you’re “generous” dealings with the government and that this goes all the way to the top and all across the organization. Care to explain?"

                    s "I ... Look, this project has been a long time coming. I was assigned by Jim and the board to begin collaborating with the FBI, even while they were still deliberating. 
                    But I promise you, this is for a good cause."

                    s "Remember the attack a while ago downtown? I haven’t felt safe ever since then. My wife too. So we thought that developing a backdoor to investigate the devices of criminals would be a good idea. "

                    s "Think about it. There’s dozens, no hundreds of phones piled up in storage that could uncover entire terrorist cells. They might not all be lone gunmen, you know. And we can stop it. "
                    
                    s "Of course, we would only allow the use of the pgram in extenuating circumstances and when investigators have a warrant. "

                    "The line goes silent for a moment"

                    s "Arreta can I ask you a question?"

                    menu seth_q:
                        am "What should I say?"

                        "Yes.": 
                            s "What are you going to do with all of the info you found on there? I really can’t have that leaking on my watch. What do you need? I promise you, I’ll make sure it happens."

                            jump scene_6_final

                        "No.":

                            a "No. You've said enough tonight. "

                            s "No?... You know what, fine. I hope you know what's gonna happen if you decide to cross me."

                            jump scene_6_final
        
        label scene_6_final:

            a "I have a lot to think about tonight, Seth."

            s "Yes, I do too. Promise me you’ll heed what I told you today. I only want what’s best for both of us, Aretta. "

            a "I can't promise anything Seth. Goodnight. "

            s "Yes, goodnight."

            "The call ends"

            am "What should I do next?"
                        



                    


        






    # This ends the game.

    return
