import os

ascii_art = '''
+===================================================================+
|                                                                   |
|                                                                   |
|   _______  _______  _       _________ _______  _  _______         |
|  (  ____ \(  ___  )( (    /|\__   __/(  ___  )( )(  ____ \        |
|  | (    \/| (   ) ||  \  ( |   ) (   | (   ) ||/ | (    \/        |
|  | (_____ | (___) ||   \ | |   | |   | (___) |   | (_____         |
|  (_____  )|  ___  || (\ \) |   | |   |  ___  |   (_____  )        |
|        ) || (   ) || | \   |   | |   | (   ) |         ) |        |
|  /\____) || )   ( || )  \  |   | |   | )   ( |   /\____) |        |
|  \_______)|/     \||/    )_)   )_(   |/     \|   \_______)        |
|                                                                   |
|   _       ___________________________ _        _______            |
|  ( \      \__   __/\__   __/\__   __/( \      (  ____ \           |
|  | (         ) (      ) (      ) (   | (      | (    \/           |
|  | |         | |      | |      | |   | |      | (__               |
|  | |         | |      | |      | |   | |      |  __)              |
|  | |         | |      | |      | |   | |      | (                 |
|  | (____/\___) (___   | |      | |   | (____/\| (____/\           |
|  (_______/\_______/   )_(      )_(   (_______/(_______/           |
|                                                                   |
|            _______  _        _______  _______  _______            |
|  |\     /|(  ____ \( \      (  ____ )(  ____ \(  ____ )           |
|  | )   ( || (    \/| (      | (    )|| (    \/| (    )|           |
|  | (___) || (__    | |      | (____)|| (__    | (____)|           |
|  |  ___  ||  __)   | |      |  _____)|  __)   |     __)           |
|  | (   ) || (      | |      | (      | (      | (\ (              |
|  | )   ( || (____/\| (____/\| )      | (____/\| ) \ \__ _  _  _   |
|  |/     \|(_______/(_______/|/       (_______/|/   \__/(_)(_)(_)  |
|                                                                   |
|                                                                   |
+===================================================================+
'''
print(ascii_art)







inventory = []
kamer = "StartScreen"
print("Type start or exit")
start = input("> ")

def addInv(item):
    inventory.append(item)
def removeInv(item):
        inventory.remove(item)
def openInv():
    if choice.lower() == "inv":
        print("----------------------------------------------------")
        for items in inventory:
            print("  -", items)
        print("----------------------------------------------------")
    
Burger = False
Keycard = False

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
    #guard, door or presents
    openInv()

    if choice.lower() == "guard" or choice.lower() == "the guard":
        print("You chose to approach the guard.\nGuard: I am really hungry\n")
        print("Do you want to:\n -Attack\n -Bribe\n")
        choice = input(">")
        if choice.lower() == "attack":
            os.system('cls')
            print("You got beat by the guard and you got put into a holding cell...\n\nDEFEAT")
            break
        elif choice.lower() == "bribe":
            if Burger == True:
                print("You give the guard the burger and you get the keycard")
                addInv("Keycard")
                removeInv("Cheeseburger")
                Keycard = True
                # player no longer has the cheeseburger after giving it away
                Burger = False
            elif Burger == False:
                print("You dont have anything to offer...")
    elif choice.lower() == "door" or choice == "the door":
        if Keycard == False:
            print("The door is locked, find a way to open it...\n")    
            continue
        elif Keycard == True:
            os.system('cls')
            print("You unlocked the door with the keycard and you moved to the next room.")
            kamer = "kamer2"
    elif choice.lower() == "presents" or choice == "the presents":
        if Burger == False:
            while True:
                print("You walked to the presents and one is a really weird shape..\nDo you want to open it?\n  -yes\n  -no\n")
                choice = input(">")
                openInv()
                if choice.lower() == "yes":
                    print("you opened the present, it had a... Cheeseburger?\nThe cheeseburger was added to your inventory\n\nyou returned to your workstation before the guard caught you.")
                    addInv("Cheeseburger")
                    Burger = True
                    break
                elif choice.lower == "no":
                    print("you returned to your workstation before the guard caught you.")
                    break
                else:
                    print("that is not a choice")
            
        elif Burger == True:
            print("You walked to the presents and there is nothing you could need.\nYou returned to your work station.")
    else:
        print("that is not a choice")
   
while kamer == "kamer2":
    print("You arrive in Santa`s storage room.\n When you look around you see:\n -Some storage bins.\n -A pile of old wood.")
    choice = input("Where do you want to go?")
    if choice.lower() == "storage bins" or "bins" or "storage":
        choice = input("Do you want to look inside the bins?")
        if choice.lower() == "yes":
            print("You see 2 things:\n A crowbar\n a jerrycan with fuel")
            choice = input("Do you want to grab them or walk away?")
            if choice == "walk away":
                print("You walked back to your original position.")
            elif choice.lower == "pick up":
                addInv("Wood")
                addInv("Crowbar")
                print("You picked both items up and walked back to the door.")
        elif choice.lower() == "no":
            continue
    elif choice.lower() == "wood" or "wood pile" or "pile of wood" or "pile of old wood":
        print("You walked to the wood pile")