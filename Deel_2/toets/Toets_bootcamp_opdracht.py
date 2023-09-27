# Opdracht 1 
# a = in visual studio code laat het je al zien waar jij de fout in gaat het laat jou de code in kleuren zien en het heeft extra features zoals comit en push
# b = het is goed om te pushen naar github zodat je een backup heb staan van al je opdrachten en het is makkelijk te delen


# opdracht 2
# a = 5  # dit is een voorbeeld van het datatype:int
# b = 10.5# dit is een voorbeeld van het datatype:float
# c = "Hallo wereld" # dit is een voorbeeld van het datatype:str

# opdracht 3
# a = 5
# b = 10
# temp = a
# a = b
# b = temp
# print(f"a = {a}, b = {b}") 

# opdracht 4
# leeftijd = input("Hoe oud ben je?")
# leeftijd = int(leeftijd)  
# pensioen = 67 - leeftijd 
# print(f"Dan duurt het nog ongeveer {pensioen} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

# opdracht 5
# from opdracht_5  import*
# print (eindantwoord)

# opdracht 6
# AANTAL_GB = 20 
# AANTAL_MINUTEN = 200 
# ONBEPERKT = False 
# aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
# aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))

# if not ONBEPERKT and (aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB):
#     print("Let op: je moet bijbetalen!")
# else:
#     print("Niets aan de hand, gebruik je mobiel lekker verder!")

# opdracht 7 
# A
# [print(i) for i in range(1, 251)]

# opdracht 8
# lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

# print("Onze menukaart:")
# for gerecht in lijst_eten:
#     print(gerecht)
# B
# ijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']

# langste_naam = ""
# for voedsel in ijst_eten:
#     if len(voedsel) > len(langste_naam):
#         langste_naam = voedsel

# print("Het voedsel met de langste naam is:", langste_naam)

# opdracht 9
# while True:
#     try:
#         input_str = input("Voer een getal tussen 0 en 10 in: ")

#         getal = int(input_str)

#         if 0 <= getal <= 10:
#             print("Je hebt een geldig getal ingevoerd:", getal)
#             break 
#         else:
#             print("Het ingevoerde getal moet tussen 0 en 10 liggen.")
#     except ValueError:
#         print("Fout: Voer alstublieft een geldig getal in.")

# opdracht 10
MAX = 20 
getal = int(input("Voer een getal in: "))  
if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX: 
    print(f"Het getal is kleiner dan {MAX}")
else: 
    print(f"Het getal is gelijk aan {MAX}")

