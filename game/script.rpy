# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define narrator = nvl_narrator
define k_nvl = Character("kriminal28", kind=nvl, image="ki_pfp.png", callback=Phone_ReceiveSound)
define MC_nvl = Character("talkchatguest", kind=nvl, image="placeholder_pfp.png", callback=Phone_SendSound)
define y_nvl = Character("yinnrenn", kind=nvl, image="ren_pfp.png", callback=Phone_ReceiveSound)
define j_nvl = Character("jamesunpak", kind=nvl, image="placeholder_pfp.png", callback=Phone_ReceiveSound)
define MC = Character("You")

init python:
    nvl_mode = "phone"



# The game starts here.

label start:

    MC "I open the curtains letting the sun in."

    MC "My head’s still all fuzzy just waking up… nngh, today I’m not in a rush though, This weekend will be all to myself. I need the time to think."

    MC "These past few weeks have been busy, school just started, and I’m already covered in homework and projects."

    MC "They say the first weeks are the most relaxed, but I think I have some of the worst luck out there."

    MC "My computer starts chiming, letting me know that I have a new notification from TalkChat."

    MC "Well, maybe it wouldn’t hurt to try the college support group I found on there. I didn’t have much time to think about what I want to do with the rest of my life, and who knows, maybe my luck will improve. Besides, it’s a good way to pass time."

    MC "It can’t get much worse, right… right?"

    MC "I guess finding the group has been my only stroke of luck, so maybe it’s a good sign… It’s made for students by students, so that means everyone can be genuine with how they feel without repercussions. I think that’s a positive, maybe."

    MC "Or it’s just out of control students… Well it won’t hurt to try. Just a bit of help deciding a major will lift a lot off my shoulders."

    $ MC_nvl =  renpy.call_screen("input", prompt="What will your username be?", someText = "Something")

    $ MC_nvl = MC_nvl.strip()

    if MC_nvl == "":
      $ MC_nvl="talkchatguest"

    "Welcome to TalkChat, [MC_nvl] !"

label selectPronoun:

    "check"
    menu (nvl=True):
        "Please select your pronouns!"
        "[pronounlist[0]!t]":
            $ pronoun = 0
        "[pronounlist[1]!t]":
            $ pronoun = 1
        "[pronounlist[2]!t]":
            $ pronoun = 2
    menu (nvl=True):
        "How would you describe your gender?"
        "[genderlist[0]!t]":
            $ gender = 0
        "[genderlist[1]!t]":
            $ gender = 1
        "[genderlist[2]!t]":
            $ gender = 2




    "Thank you for completing the sign up process! Enjoy TalkChat!"

    nvl clear

    "[MC_nvl] has entered the chatroom"

    j_nvl "Kriminal28, I\’m sorry, but you’re just plain wrong"

    k_nvl "INCORRECT."

    k_nvl "I AM VERY RIGHT TY"

    r_nvl "wow no respect for the classic regions wowww"

    k_nvl "brueh"

    k_nvl "theyre oldd"

    k_nvl "THIS IS THE PRESENT!!! TECHNOLOGY!!!"

    j_nvl "My point still stands."

    k_nvl "LOLOLOL NO"

    j_nvl "Ok, why not?"

    k_nvl "YOU´RE JUST PLAIN WRONG THE NEW REGIONS ARE UPDATED WITH THE NEW THINGS AND ARE WAY COOLER"

    j_nvl "Come on, those ‘additions’ only make things more complicated and get ignored as soon as a new game gets released"

    k_nvl "REN HELP MEE HERE I KNOW YOU’RE MORE INTELLLIGENT"

    r_nvl "What about the remakes? They’re the best of both worlds"

    k_nvl "THEYRE JUST THE STUPID OLD STORY AGAIN  AND HALF THE TIME THE GAMES ARE UNRECOGNIZABLE LOL"

    j_nvl "Yeah, and tons of new mechanics that just hurt the original experience."

    k_nvl "JAMES AGREED WITH ME OMG"

    r_nvl "well now I think you're both wrong!!!"

    j_nvl "Oh"

    k_nvl "LOLOLOLOL"

    j_nvl "Hello, new person."

    r_nvl "oh! hiii!"

    k_nvl "HHHHHUUUHHHHHH"

    j_nvl "Why are you surprised? The chatroom is public."

    k_nvl "stfu"

    k_nvl "WAIT DID YOU SERIOSLY CHANGE THE DESC TO ‘COLLEGE SUPPORT GROUP’ HELP"

    r_nvl "isnt that what we are supposed to be?"

    k_nvl "YEAH but"

    k_nvl "all we do is talk about dumb shit lmao"

    k_nvl "you think im giving support lol"

    k_nvl "im like a colleges worst nightmare"

    r_nvl "true"

    j_nvl "Very true, actually."

    k_nvl ":’D"



    return
