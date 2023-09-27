import random

juiste_getal = random.randint(1, 10)

while True:
    getal = int(input('Raad het nummer: '))

    if getal == juiste_getal:
        print("\033[92mJe hebt het juiste getal geraden!\033[0m")
        break 
    else:
        print("\033[91mJe hebt het nummer niet goed geraden. Probeer opnieuw.\033[0m")
