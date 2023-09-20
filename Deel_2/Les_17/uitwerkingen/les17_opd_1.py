getal = int(input('Raad het nummer tussen 1 - 5: '))

if getal == 5:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m")
elif getal == 4:
    print("\033[92mJe hebt het getal goed geraden!\033[0m")
elif getal == 3:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m")
elif getal == 2:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m")
elif getal == 1:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m")
else:
    print("Ongeldige invoer. Voer een nummer tussen 1 en 5 in.")
