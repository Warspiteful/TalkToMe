image k28_call = "k28_call.png"
define k28 = Character("kriminal28")
image k_neutral = "k_neutral.png"

label kriminal28call1:

scene k28_call

voice "audio/kriminal28/kriminal28_001.mp3"
k28"Hellloooooo... can you hear meeee????"
menu: 
    "Yes":
        voice "audio/kriminal28/kriminal28_002.mp3"
        k28 "Okay, that's good. My mic isn't being shitty for once."

    "No":
        voice "audio/kriminal28/kriminal28_003.MP3"
        k28 "Ha ha. Very funny." 
        voice "audio/kriminal28/kriminal28_004.MP3"
        k28 "But hey, my mic is working for once."
voice "audio/kriminal28/kriminal28_005.MP3"
k28 "Anyways... how does it feel?"
menu:
    "How does what feel?":
        pass
voice "audio/kriminal28/kriminal28_006.mp3"
k28 "Hello? Being in my presence, of course!"
menu:
    "...":
        pass
voice "audio/kriminal28/kriminal28_007.mp3"
k28 "That was a joke, I'm not actually that self-centered."
menu:
    "...":
        pass
voice "audio/kriminal28/kriminal28_008.mp3"
k28 "Sorry... I know jokes are supposed to be funny. It just sounded better in my head, alright?"
menu:
    "Ha ha.":
        pass
voice "audio/kriminal28/kriminal28_009.mp3"
k28 "See! I'm the king of humor, aren't I?"
voice "audio/kriminal28/kriminal28_010.mp3"
k28 "You know what, don't answer that. I'll stop now..."
menu:
    "So... why did you want to video call me if you're not gonna put your camera on?":
        pass
voice "audio/kriminal28/kriminal28_011.mp3"
k28 "Oopsie. I didn't actually know it was off hehe..."

scene k28 room
show k_smile
voice "audio/kriminal28/kriminal28_012.mp3"
k28 "Now we can have a staring contest!"
menu:
    "???":
        pass
show k_neutral
voice "audio/kriminal28/kriminal28_013.mp3"
k28 "What? We're both bored, so..."
voice "audio/kriminal28/kriminal28_014.mp3"
k28 "... hmmmm...."
voice "audio/kriminal28/kriminal28_015.mp3"
k28 "Actually, I'd lose. Ignore that thought."
menu:
    "??????":
        pass
voice "audio/kriminal28/kriminal28_016.mp3"
k28 "Ugh.. the boredom continues. The more I think about it, the worse it gets haaaaa..."
menu:
    "We could talk?":
        pass
hide k_neutral
show k_smile
voice "audio/kriminal28/kriminal28_017.mp3"
k28 "How about we chat as well!"
menu:
    "...":
        pass
voice "audio/kriminal28/kriminal28_018.mp3"
k28 "Get it! Because we're using TalkChat."
hide k_smile
show k_neutral
voice "audio/kriminal28/kriminal28_019.mp3"
k28 "....Ew that was just bad..."
hide k_neutral
show k_smile
voice "audio/kriminal28/kriminal28_020.mp3"
k28 "But yeah, that'd be nice."
menu:
    "So...":
        pass
voice "audio/kriminal28/kriminal28_021.mp3"
k28 "So..."
voice "audio/kriminal28/kriminal28_022.mp3"
k28 "Do you like Pokémon?"
menu:
    "Yes!":
        voice "audio/kriminal28/kriminal28_023.mp3"
        k28 "Really?"
        voice "audio/kriminal28/kriminal28_024.mp3"
        k28 "What's your favorite region? Wait don't tell, me don't tell me!"

        menu:
            "Why?":
                voice "audio/kriminal28/kriminal28_025.mp3"
                k28 "If you don't like Alola I might have to... y'know... block you haha, which I'd rather not do."
                voice "audio/kriminal28/kriminal28_026.mp3"
                k28 "If you can't tell, I'm a HUGE sun & moon fan, and I refuse to associate with its haters. "

    "No...":
        voice "audio/kriminal28/kriminal28_027.mp3"
        k28 "Shame. You seemed like the type to like it."
        voice "audio/kriminal28/kriminal28_028.mp3"
        k28 "That's a good thing by the way!"
        voice "audio/kriminal28/kriminal28_029.mp3"
        k28 "Pokémon means so much to me, don't even get me started!"
        voice "audio/kriminal28/kriminal28_030.mp3"
        k28 "Maybe I can convince you to give it a try one day?"
        menu:
            "Maybe...":
                voice "audio/kriminal28/kriminal28_031.mp3"
                k28 "I'll take what I can get!"
voice "audio/kriminal28/kriminal28_032.mp3"
k28 "But please, even if you just listen to me talk about pokemon I'll love you forever."
voice "audio/kriminal28/kriminal28_033.mp3"
k28 "I mean what haha."
menu:
    "Very smooth.":
        pass
voice "audio/kriminal28/kriminal28_034.mp3"
k28 "See! I'm quite the charmer! 100 percent suave!"

k28 "..."
menu:
    "pfft":
        pass

k28 "..." 
voice "audio/kriminal28/kriminal28_035.mp3"
k28 "Maybe I can't handle my camera being on.."
menu:
    "What?":
        pass
voice "audio/kriminal28/kriminal28_036.mp3"
k28 "What?"
menu:
    "Huh?":
        pass
voice "audio/kriminal28/kriminal28_037.mp3"
k28 "Huh?"
menu:
    "...":
        pass
voice "audio/kriminal28/kriminal28_038.mp3"
k28 "pfffft"
menu:
    "Why are you laughing?":
        pass
voice "audio/kriminal28/kriminal28_039.mp3"
k28 "Haaa... you're so cute when you're frustrated."
voice "audio/kriminal28/kriminal28_040.mp3"
k28 "I mean what."
menu:
    "Are you... trying to flirt?":
        pass
voice "audio/kriminal28/kriminal28_041.mp3"
k28 "Is it...effective?"
menu:
    "It is":
        voice "audio/kriminal28/kriminal28_042.mp3"
        k28 "See! I am suave!"

        menu:
            "Don't get so confident!":
                voice "audio/kriminal28/kriminal28_043.mp3"
                k28 "Fine, fine. I won't! Pinky promise!"

    "...":
        voice "audio/kriminal28/kriminal28_044.mp3"
        k28 "Oh..."
        voice "audio/kriminal28/kriminal28_045.mp3"
        k28 "Maybe I'm Not as suave as I think heh..."
        voice "audio/kriminal28/kriminal28_046.mp3"
        k28 "Sorry if that was uncomfortable, I was mainly joking hah..."
voice "audio/kriminal28/kriminal28_047.mp3"
k28 "Anyways~"
voice "audio/kriminal28/kriminal28_048.mp3"
k28 "I have an important question for you!"
menu:
    "What is it?":
        pass
    


voice "audio/kriminal28/veryloud_049.mp3"
k28 "ARE YOU GAY?"
menu:
    "Ow! Can you be any louder?":
        pass
voice "audio/kriminal28/veryloud_050.mp3"
k28 "YES I CAN, ACTUALLY!"
menu:
    "My ears!":
        pass
voice "audio/kriminal28/veryloud_051.mp3"
k28 "DO YOU REGRET CALLING ME YET?"
menu:
    "Yes!":
        voice "audio/kriminal28/kriminal28_052.mp3"
        k28 "Ouch!"
        voice "audio/kriminal28/kriminal28_053.mp3"
        k28 "You're gonna hurt my feelingsssss~"
    "No!":
        voice "audio/kriminal28/kriminal28_054.mp3"
        k28 "Well aren't you gracious!"
        voice "audio/kriminal28/kriminal28_055.mp3"
        k28 "I destroy your ears and you somehow don't hate me!"

return

