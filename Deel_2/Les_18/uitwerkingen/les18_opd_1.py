import random

min_range = 1
max_range = 100

def is_within_range(number):
    return min_range <= number <= max_range

correct_answer = random.randint(min_range, max_range)

rounds_played = 0
wrong_guesses = 0

while True:
    user_input = input(f"Raad een getal tussen {min_range} en {max_range}: ")

    # Controleer of de gebruikersinvoer een geldig getal is
    if user_input.isdigit():
        user_guess = int(user_input)
        
        # Controleer of de gok binnen de juiste range valt
        if is_within_range(user_guess):
            if user_guess == correct_answer:
                print("Gefeliciteerd! Je hebt het juiste antwoord geraden.")
                rounds_played += 1

                play_again = input("Wil je nog een ronde spelen? (ja/nee): ")
                if play_again.lower() == "ja":
                    correct_answer = random.randint(min_range, max_range)
                else:
                    print(f"Aantal gespeelde ronden: {rounds_played}")
                    print(f"Aantal foute gokken: {wrong_guesses}")
                    break
            else:
                print("Helaas, dat is niet het juiste antwoord. Probeer opnieuw.")
                wrong_guesses += 1
        else:
            print(f"Je moet een getal raden tussen {min_range} en {max_range}. Probeer opnieuw.")
    else:
        print(f"Ongeldige invoer. Voer een getal in tussen {min_range} en {max_range}. Probeer opnieuw.")
