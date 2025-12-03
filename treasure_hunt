import time

# --- Utility function for timed printing ---
def pause_print(text, delay=1.5):
    print(text)
    time.sleep(delay)

# --- INTRO ASCII ART ---
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
*******************************************************************************
''')

pause_print("Welcome to TREASURE ISLAND – ASCII Adventure Edition!")
pause_print("Your mission: survive the island and uncover one of its hidden treasures.\n")

# --- CROSSROADS ---
print(r'''
      ~  ~  ~  ~
    ~    🌴  🌴     ~
  ~   🌴   🪵   🌴     ~
~   🌴    ⛓️     🌴   ~
    ~   🌴     🌴   ~
          🧭
''')
choice1 = input("You stand at a crossroads deep in the jungle.\n"
                "Do you venture LEFT into the misty forest or RIGHT toward the roaring waves?\n\n"
                "Type 'left' or 'right': ").lower()

# --- LEFT PATH ---
if choice1 == "left":
    print(r'''
        🌫️🌫️🌲🌫️🌲🌫️
     The forest thickens...
    🦜  Shadows dart between trees  🦜
    ''')
    pause_print("The air chills as you approach a glowing blue river.\n")

    print(r'''
        ~~~~~~~~~~~~~~~
       ~~~~~🌊~~~~🌊~~~~~
        ~~~~~🌊~~~~🌊~~~~~
       ~~~~~🌊~~~~🌊~~~~~
        ~~~~~~~~~~~~~~~
    ''')
    choice2 = input("Do you BUILD a raft, WAIT for sunrise, or CROSS using the fallen tree?\n"
                    "Type 'build', 'wait', or 'cross': ").lower()

    if choice2 == "wait":
        print(r'''
        🌅  ☀️ Morning breaks across the misty river
        Stepping stones shimmer below the water...
        ''')
        choice3 = input("Do you STEP carefully across or SEARCH the riverbank first?\n"
                        "Type 'step' or 'search': ").lower()

        if choice3 == "search":
            pause_print("🗝️ You uncover an ancient key under a mossy stone! You pocket it.\n")

        print(r'''
            ⛰️ Ancient Shrine Ahead ⛰️
              /\
             /__\  🔥
            /____\
        ''')
        choice4 = input("Two entrances appear: a NARROW crack or a LARGE doorway.\n"
                        "Type 'narrow' or 'large': ").lower()

        if choice4 == "narrow":
            print(r'''
             💎 Hidden Chamber 💎
            ┌──────────────┐
            │    ⛓️  Chest   │
            └──────────────┘
            ''')
            choice5 = input("A locked chest glimmers in torchlight.\n"
                            "Do you USE your key or FORCE it open? Type 'key' or 'force': ").lower()
            if choice5 == "key":
                print(r'''
                💚 EMERALD IDOL 💚
                 🏆 You found the Lost Treasure!
                ''')
                pause_print("Congratulations! You claim the Emerald Idol and escape the island.\n🏆 YOU WIN!")
            else:
                print(r'''
                💥 A magic trap bursts open! 💥
                The chamber collapses in a roar of dust.
                ''')
                pause_print("You were too forceful.\nGAME OVER.")
        else:
            print(r'''
             🪨💀 GIANT BOULDER 💀🪨
            ''')
            pause_print("A rolling boulder crushes the entrance. You never had a chance.\nGAME OVER.")

    elif choice2 == "build":
        print(r'''
         🪵 You tie vines together...
         🌊 Your raft floats gently downstream...
        ''')
        choice3 = input("Do you ROW downstream or CROSS directly?\nType 'row' or 'cross': ").lower()

        if choice3 == "row":
            print(r'''
             🪶  Hidden Cove Appears  🪶
             🌌 Glowing cave mouth ahead...
            ''')
            choice4 = input("Do you ENTER the cave or EXPLORE the beach?\nType 'enter' or 'explore': ").lower()
            if choice4 == "enter":
                print(r'''
                💎 SAPPHIRE CROWN 💎
                 👑 Light dances off ancient gems
                ''')
                pause_print("You claim the Sapphire Crown of the Deep!\n🏆 YOU WIN!")
            else:
                print(r'''
                ☠️ PIRATES! ☠️
                ''')
                pause_print("They steal your supplies and leave you stranded.\nGAME OVER.")
        else:
            print(r'''
            🌊 SPLASH! 🌊
            Your raft collapses in the current.
            ''')
            pause_print("You drown beneath the swirling blue water.\nGAME OVER.")

    else:
        print(r'''
        💀 The tree snaps beneath your feet 💀
        ''')
        pause_print("You vanish beneath the raging current.\nGAME OVER.")

# --- RIGHT PATH ---
elif choice1 == "right":
    print(r'''
     🌊🌊🌊  🏖️  🌊🌊🌊
     A shipwreck lies twisted on the beach...
    ''')
    choice2 = input("Do you SEARCH the wreck, FOLLOW the coast, or CLIMB the cliffs?\n"
                    "Type 'search', 'follow', or 'climb': ").lower()

    if choice2 == "search":
        print(r'''
        ⚓ Inside the wreck lies gold and a crumpled map ⚓
        ''')
        choice3 = input("Do you FOLLOW the map inland or KEEP scavenging the ship?\n"
                        "Type 'follow' or 'keep': ").lower()
        if choice3 == "follow":
            print(r'''
            🏛️ Ancient Temple 🏛️
            Two statues guard the door...
            🐍 Serpent   🦁 Lion
            ''')
            choice4 = input("Which do you bow to? Type 'serpent' or 'lion': ").lower()
            if choice4 == "lion":
                print(r'''
                🦁 GOLDEN CHAMBER 🦁
                 💰 Gold and light surround you
                ''')
                pause_print("The Lion accepts your courage. The treasure is yours.\n🏆 YOU WIN!")
            else:
                print(r'''
                🐍💀 Poisonous Mist 💀🐍
                ''')
                pause_print("The serpent breathes venom. You collapse instantly.\nGAME OVER.")
        else:
            print(r'''
            💥 The ship collapses around you 💥
            ''')
            pause_print("You are buried under the wreck.\nGAME OVER.")

    elif choice2 == "follow":
        print(r'''
        🏕️ Abandoned Camp 🏕️
        A journal mentions a waterfall secret...
        ''')
        choice3 = input("Do you SEEK the waterfall or REST here?\nType 'seek' or 'rest': ").lower()
        if choice3 == "seek":
            print(r'''
            💧 Hidden Grotto 💧
            🌈 Light shimmers behind the falls...
            ''')
            choice4 = input("Two tunnels: LEFT (glowing) or RIGHT (echoing)? Type 'left' or 'right': ").lower()
            if choice4 == "left":
                print(r'''
                🐚 PEARL OF TIDES 🐚
                 🌊 Found floating in a calm lagoon
                ''')
                pause_print("You’ve claimed the legendary Pearl of Tides!\n🏆 YOU WIN!")
            else:
                print(r'''
                🌑 Endless dark... 🌑
                ''')
                pause_print("You wander until your light fades.\nGAME OVER.")
        else:
            print(r'''
            🌊 Rising Tide 🌊
            ''')
            pause_print("You fall asleep as the tide swallows your camp.\nGAME OVER.")

    elif choice2 == "climb":
        print(r'''
         🧗‍♂️ Rocky Cliffs 🧗‍♂️
         Above lies a glowing archway...
        ''')
        choice3 = input("Through the arch you see a PORTAL. Do you ENTER or RETURN?\nType 'enter' or 'return': ").lower()
        if choice3 == "enter":
            print(r'''
            🌌 MYSTIC PORTAL 🌌
             👑 You are crowned Keeper of the Island
            ''')
            pause_print("You transcend mortality and rule the island.\n🏆 YOU WIN!")
        else:
            print(r'''
            🪨 The cliff gives way beneath you 🪨
            ''')
            pause_print("You fall to your doom.\nGAME OVER.")
    else:
        print(r'''
        🌊 The tide rises behind you 🌊
        ''')
        pause_print("You are trapped by the waves.\nGAME OVER.")

else:
    print(r'''
    🌫️ Lost in indecision 🌫️
    ''')
    pause_print("The jungle swallows you whole.\nGAME OVER.")
