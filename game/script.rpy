# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define narrator = nvl_narrator
define k_nvl = Character("kriminal28", kind=nvl, image="ki_pfp.png", callback=Phone_ReceiveSound)
define MC_nvl = Character("talkchatguest", kind=nvl, image="placeholder_pfp.png", callback=Phone_SendSound)
define y_nvl = Character("yinnrenn", kind=nvl, image="ren_pfp.png", callback=Phone_ReceiveSound)
# The game starts here.

label start:

"kriminal28 is online"
k_nvl "you called?"
MC_nvl "what do you want now?"
k_nvl "wowwww"
k_nvl "you really think i want something from you"
y_nvl "seriously..."
k_nvl "yknow thats just kinda sad"
MC_nvl "stfu"
k_nvl "you wound me"
k_nvl "you called?"
MC_nvl "what do you want now?"
k_nvl "wowwww"
k_nvl "you really think i want something from you"
y_nvl "seriously..."
k_nvl "yknow thats just kinda sad"
MC_nvl "stfu"
k_nvl "you wound me"
k_nvl "you called?"
MC_nvl "what do you want now?"
k_nvl "wowwww"
k_nvl "you really think i want something from you"
y_nvl "seriously..."
k_nvl "yknow thats just kinda sad"
MC_nvl "stfu"
k_nvl "you wound me"
k_nvl "you called?"
MC_nvl "what do you want now?"
k_nvl "wowwww"
k_nvl "you really think i want something from you"
y_nvl "seriously..."
k_nvl "yknow thats just kinda sad"
MC_nvl "stfu"
k_nvl "you wound me"
return
