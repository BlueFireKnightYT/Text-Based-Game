import os

ascii_art = '''
+===================================================================+ g    
|                                                                   | g    
|                                                                   | g    
|   _______  _______  _       _________ _______  _  _______         | g    
|  (  ____ \(  ___  )( (    /|\__   __/(  ___  )( )(  ____ \        | g    
|  | (    \/| (   ) ||  \  ( |   ) (   | (   ) ||/ | (    \/        | g    
|  | (_____ | (___) ||   \ | |   | |   | (___) |   | (_____         | g    
|  (_____  )|  ___  || (\ \) |   | |   |  ___  |   (_____  )        | g    
|        ) || (   ) || | \   |   | |   | (   ) |         ) |        | g    
|  /\____) || )   ( || )  \  |   | |   | )   ( |   /\____) |        | g    
|  \_______)|/     \||/    )_)   )_(   |/     \|   \_______)        | g    
|                                                                   | g    
|   _       ___________________________ _        _______            | g    
|  ( \      \__   __/\__   __/\__   __/( \      (  ____ \           | g    
|  | (         ) (      ) (      ) (   | (      | (    \/           | g    
|  | |         | |      | |      | |   | |      | (__               | g    
|  | |         | |      | |      | |   | |      |  __)              | g    
|  | |         | |      | |      | |   | |      | (                 | g    
|  | (____/\___) (___   | |      | |   | (____/\| (____/\           | g    
|  (_______/\_______/   )_(      )_(   (_______/(_______/           | g    
|                                                                   | g    
|            _______  _        _______  _______  _______            | g    
|  |\     /|(  ____ \( \      (  ____ )(  ____ \(  ____ )           | g    
|  | )   ( || (    \/| (      | (    )|| (    \/| (    )|           | g    
|  | (___) || (__    | |      | (____)|| (__    | (____)|           | g    
|  |  ___  ||  __)   | |      |  _____)|  __)   |     __)           | g    
|  | (   ) || (      | |      | (      | (      | (\ (              | g    
|  | )   ( || (____/\| (____/\| )      | (____/\| ) \ \__ _  _  _   | g    
|  |/     \|(_______/(_______/|/       (_______/|/   \__/(_)(_)(_)  | g    
|                                                                   | g    
|                                                                   | g    
+===================================================================+ g    
'''
print(ascii_art)

inventory = []
kamer = "StartScreen"
print("Type start or exit")
start = input("> ")

def addInv(item):
    inventory.append(item)
def removeInv(item):
    try:
        inventory.remove(item)
    except ValueError:
        # Item not found; ignore to avoid crashing the game
        pass
def openInv():
    # normalize and accept several variants for inventory
    if choice.lower() == "inv" or choice.lower() == "inventory" or choice.lower() == "i":
        print("----------------------------------------------------")
        for items in inventory:
            print("  -", items)
        print("----------------------------------------------------")
    
Burger = False
Keycard = True
fuel = False
crowbar = False
matches = False

while kamer == "StartScreen":
    if start.lower() == "start":
        kamer = "kamer1"
        os.system('cls') 
        print("You have been kidnapped by Santa because you are short.\nYou want to escape Santa's workshop, but have not found a way out yet.\n\nYou look around and you see:\n")   
    elif start.lower() == "exit":
        break
    else:
        print("That was not an option")
        start = input("Type Start or exit: ")
while kamer == "kamer1":
    print("  -A guard\n  -A door\n  -Presents\n")
    choice = input("Wich of these do you want to go to? \n>")
    openInv()
    if "guard" in choice.lower():
        print("You chose to approach the guard.\nGuard: I am really hungry\n")
        print("Do you want to:\n -Attack\n -Bribe\n")
        choice = input(">")
        openInv()
        if "attack" in choice.lower() or "beat" in choice.lower():
            os.system('cls')
            print("You got beat by the guard and you got put into a holding cell...\n\nDEFEAT")
            break
        elif "bribe" in choice.lower():
            if Burger == True:
                print("You give the guard the burger and you get the keycard")
                addInv("Keycard")
                removeInv("Cheeseburger")
                Keycard = False
                Burger = False
            elif Burger == False:
                print("You dont have anything to offer... \nYou walk back to your workstation.")
            
    elif "door" in choice.lower():
        if Keycard == False:
            print("The door is locked, find a way to open it...\n")    
            continue
        elif Keycard == True:
            os.system('cls')
            print("You unlocked the door with the keycard and you moved to the next room.")
            kamer = "kamer2"
            print("You arrive in Santa`s storage room.\n")
    elif "presents" in choice.lower() or "gifts" in choice.lower() or "present" in choice.lower() or "gift" in choice.lower():
        if Burger == False and Keycard == False:
            while True:
                print("You walked to the presents and one is a really weird shape..\nDo you want to open it?\n  -yes\n  -no\n")
                choice = input(">")
                openInv()
                if choice.lower() == "yes":
                    print("you opened the present, it had a... Cheeseburger?\nThe cheeseburger was added to your inventory\n\nyou returned to your workstation before the guard caught you.")
                    addInv("Cheeseburger")
                    Burger = True
                    break
                elif choice.lower() == "no":
                    print("you returned to your workstation before the guard caught you.")
                    break
                else:
                    print("that is not a choice")
            
        elif Burger == True:
            print("You walked to the presents and there is nothing you could need.\nYou returned to your work station.")
    else:
        print("that is not a choice") 
while kamer == "kamer2":
    print(" When you look around you see:\n -Some storage bins.\n -A pile of old wood.\n -A door that seems to be locked.")
    choice = input("Where do you want to go? \n>")
    openInv()
    if "storage" in choice.lower() or "bin" in choice.lower():
        while True:
            choice = input("Do you want to look inside the bins?\n>")
            openInv()
            if "yes" in choice.lower() and fuel == False and crowbar == False:
                print("You see 2 things:\n A crowbar\n a jerrycan with fuel")
                choice = input("Do you want to grab them or walk away?\n>")
                openInv()
                while True:
                    if "walk" in choice.lower() or "leave" in choice.lower():
                        print("You walked back to your original position.")
                        break
                    elif "grab" in choice.lower() or "take" in choice.lower() or "pick" in choice.lower():
                        addInv("jerrycan with fuel")
                        addInv("Crowbar")
                        print("You picked both items up and walked back to the entrance of the room.")
                        fuel = True
                        crowbar = True
                        break
                    else:
                        print("That was not an option...")
            elif "no" in choice.lower():
                break
            else:
                print("That was not an option...")
    elif "wood" in choice.lower() or "pile" in choice.lower():
        print("You walked to the wood pile")
        print("as you look through the woodpile you find a weard button and a box of matches. What do you want to do?\n -Push button\n -Take matches\n -Go back")
        while True:
            choice = input(">")
            openInv()
            if "button" in choice.lower():
                os.system('cls')
                print("You pushed the button and a hidden door opened, you walk through it and find yourself in the hangars.")
                kamer = "kamer3"
                break
            elif "matches" in choice.lower() or "take" in choice.lower():
                print("You took the box of matches and put them in your inventory.")
                addInv("Box of matches")
                matches = True
                break
            elif "back" in choice.lower():
                print("You walked back to your original position.")
                break
            else:
                print("That was not an option...")
    elif "door" in choice.lower():
        print("The door is locked. find a way to open the door.")  
        if fuel == True and matches == True:
            print("You think of an option and look at what you have. You have:")
            for items in inventory:
                print(items)
            while True:
                choice = input("You think you can blow up the door using the fuel and matches. Do you want to try it?\n -yes\n -no\n>")
                openInv()
                if choice.lower() == "yes":
                    os.system('cls')
                    print("You poured the fuel on the door and used the matches to light it up. The door exploded and you walked through it and found yourself in the hangars.")
                    # remove the exact items that were added to inventory earlier
                    removeInv("Box of matches")
                    removeInv("jerrycan with fuel")
                    fuel = False
                    matches = False
                    kamer = "kamer3"
                    break
                elif choice.lower() == "no":
                    break
                else:
                    print("That was not an option...")

        while True:
            if crowbar == True and kamer != "kamer3":
                choice = input("do you want to use the crowbar to try and open the door?\n -yes\n -no\n>")
                openInv()
                if choice.lower() == "yes":
                    os.system('cls')
                    print("You used the crowbar to open the door and you walked through it and found yourself in the hangars.")
                    kamer = "kamer3"
                    break
                elif choice.lower() == "no":
                    print("you didn't use the crowbar.")
                    break
                else:
                    print("That was not an option")
    else:
        print("That was not an option...")
while kamer == "kamer3":
    print("As you walk into the hangars you see:\n -Santa's sleigh\n -A door that seems to lead outside\n\n where do you want to go?")
    choice = input(">")
    openInv()
    if "sleigh" in choice.lower() or "sled" in choice.lower():
        print("You approach santa's sleigh and you find that it has no more fuel...")
        if fuel == True:
            print("Do you want to fuel the sleigh using the jerrycan with fuel?\n -Yes\n -No")
            choice = input(">")
            openInv()
            if choice.lower() == "yes":
                print("You put the fuel into the sleigh and the start buttun lights up.\nDo you want to leave with the sleigh?\n -Yes\n -No")
                choice = input(">")
                openInv()
                if choice.lower() == "yes":
                    print("You start the sleigh and you leave the factory. as you look back, Santa was right behind you with a rifle..\n YOU WON!!!")
                    break   
                elif choice.lower() == "no":
                    print("You moved back to your original position.")
            elif choice.lower() == "no":
                print("You didn't fuel the sleigh and you moved back to your starting position.")
        elif fuel == False:
            print("You dont have any fuel...")
    elif "door" in choice.lower():
        print("You ran through the door and you hear the guards coming close.\nafter a while, you thought you were in the clear,\nbut then the guards storm outside and take you back to the holding cell..\n\n YOU LOST")
        break