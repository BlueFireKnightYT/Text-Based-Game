import sys

def vraag_naar_input(vraag_tekst):
    # 1. Toon de vraag en lees input
    antwoord = input(vraag_tekst + " ")

    # 2. Doe wat checks op de input
    if "exit" in antwoord.lower():
        print("you quit the game")
        sys.exit()
        return None  # dit geeft 'niets' terug

    if "help" in antwoord.lower():
        choice = input("Which level are you in?\n -The workshop\n -The storage\n -The hangar\n >")
        if "workshop" in choice.lower():
            print("There may be something the guard likes in the presents...\n__________________________________________________________")
        elif "storage" in choice.lower():
            print("The door must be able to go open in some way or another...\n__________________________________________________________")
        elif "hangar" in choice.lower():
            print("The back door doesnt seem like the best idea...\n__________________________________________________________")
        return vraag_naar_input(vraag_tekst)  # Ask again after help
    
    return antwoord


