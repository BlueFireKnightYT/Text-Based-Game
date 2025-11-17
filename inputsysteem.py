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
    if antwoord.lower() == "stop":
        print("Je hebt 'stop' ingevoerd, dus we stoppen nu.")
        return None  # dit geeft 'niets' terug

    if antwoord.lower() == "ja":
        print("Je zei JA!")
        return True   # we geven True terug

    if antwoord.lower() == "nee":
        print("Je zei NEE!")
        return False  # we geven False terug

    # 3. Geen enkele check klopte → geef gewoon het antwoord terug
    return antwoord
