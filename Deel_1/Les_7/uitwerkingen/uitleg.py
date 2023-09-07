naam = input('Wat is je naam? ')
zin = f'Hoi {naam}, wat is jouw leeftijd? '
leeftijd = int(input(zin))

STUDENTEN_TARIEF = 25
STANDAARD_TARIEF = 27.50
SENIOREN_TARIEF = 35
prijs = STANDAARD_TARIEF

TEKST = f"Ons abonnement is {prijs} per maand!!! en u krijgt van ons:"
aanbiedings_zin = " "

if leeftijd < 18:
    aanbiedings_zin = "Jij mag zelf nog geen abonnement afsluiten"
elif leeftijd < 50:
    aanbiedings_zin = "Je krijgt van ons gratis 2 GB extra data (vanaf 25 GB)"
    if leeftijd < 25:
        prijs = STUDENTEN_TARIEF
else:
    prijs = SENIOREN_TARIEF

if leeftijd >= 18:
    print(TEKST + " " + aanbiedings_zin)