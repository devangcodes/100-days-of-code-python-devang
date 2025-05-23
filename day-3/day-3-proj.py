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
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Dear User - Please make sure to type all your inputs in small-case and with the correct spellings for the game to proceed.")
print("🏴‍☠️ WELCOME TO TREASURE ISLAND 🏴‍☠️")
print("You are an adventurer seeking the Lost Treasure of Captain Arkenstone, hidden deep within the cursed island of Xandora. \nBeware: This land tests not just courage—but wit. Make the wrong choice, and you may not live to regret it.")

scene1_choice = input("Do you go left or right? ")

if scene1_choice == "left":
    print(" ")
    print("You reach a wide river, There’s a half-sunken rowboat tangled in vines. On the bank, a rusty bell hangs.")
    scene2_choice = input("Do you ring the bell and wait or swim? Type swim or wait: ")

    if scene2_choice == "wait":
        print(" ")
        print("A moment later, a ghostly gondola floats from the mist. You step in… and cross safely.")
        scene3_choice = input("On the other side, you hike up a cliff trail. \nThree massive doors stand before you: red, blue, and yellow. \n Which one do you choose? ")

        if scene3_choice == "red":
            print("You push the red door open. Flames erupt instantly. You scream as you're engulfed in fire. 💀 GAME OVER.")
        elif scene3_choice == "blue":
            print("The door creaks open into darkness. \nEyes open all around you. \nA pack of ancient temple beasts attacks! 💀 GAME OVER.")
        elif scene3_choice == "yellow":
            print(" ")
            print("As the door swings open you step into a quiet corridor lit by glowing crystals.")
            scene4_choice = input("You see a riddle on a stone tablet which says: \n'I have cities but no houses. \nI have mountains but no trees. \nI have water but no fish. \nWhat am I?' ")

            if scene4_choice == "map":
                print(" ")
                print("The tablet glows and disintegrates into sand. A silver staircase reveals itself, descending into the treasure vault.")
                scene5_choice = input("You step into a glowing vault. At the center are three chests, each carved from a different material: Wood, Gold and Stone. \nWhich chest do you open? ")

                if scene5_choice == "wooden":
                    print("It creaks open... nothing inside. A trapdoor opens beneath you. \n💀 GAME OVER. Too cautious.")
                elif scene5_choice == "golden":
                    print("The lid burst open--poison darts fly out. \n💀 GAME OVER. Too greedy.")
                elif scene5_choice == "stone":
                    print(" ")
                    print("You lift the heavy lid. Inside: a glowing ord and a scroll. \nThe Treasure of Arkenstone is yours. \n🎉 YOU WIN.")
            else:
                print("The ceiling groans. Sand begins to pour from all corners. 💀 GAME OVER.")
    else:
        print(" ")
        print("You dive in. Suddenly—a giant shadow rushes toward you. \nA monstrous trout launches from the depths and drags you under. \n💀 GAME OVER.")
else:
    print(" ")
    print("You step on a loose rock. The ground crumbles. \nYou fall into a hidden sinkhole filled with bones. \n💀 GAME OVER.")







