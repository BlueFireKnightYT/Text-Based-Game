import sys


# def get_user_input(frans):
#     choice = input(frans)
#     if choice.lower() == 'exit':
#         sys.exit()
#     return

def vraag_naar_input(vraag_tekst):
    # 1. Toon de vraag en lees input
    antwoord = input(vraag_tekst + " ")

    # 2. Doe wat checks op de input
    if antwoord.lower() == "exit" or antwoord.lower == "door":
        print("you have enterd exit")
        quit
        return None  # dit geeft 'niets' terug

    # if antwoord.lower() == "inv" or antwoord.lower() == "inventory":
        
    #     return antwoord  # we geven True terug


    if antwoord.lower() == "help":
        choice = input("In witch level are you?\n -The workshop\n -The storage\n -The hangar\n >")
        if choice.lower() == "The workshop" or choice.lower() == "workshop":
            print("There may be something the guard likes in the pressents.\n__________________________________________________________")
        elif choice.lower() == "the storage" or choice.lower() == "storage":
            print("nah figure it out\n__________________________________________________________")
        elif choice.lower() == "the hangar" or choice.lower() == "hangar":
            print("what do you think\n__________________________________________________________")
        return "presents"
        


    # 3. Geen enkele check klopte → geef gewoon het antwoord terug
    return antwoord
