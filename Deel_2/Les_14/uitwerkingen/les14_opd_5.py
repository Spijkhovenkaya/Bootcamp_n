namenLijst = ["Hamza" , "Aydin" , "Christian" , "Kaya" , "Bob"]

print (f"Dit is een lijst van de namen: {namenLijst}")

gekozenNaam = input(f"Voer een naam in om hem te verwijderen...")

try:
        namenLijst.remove(gekozenNaam)
     
         
except ValueError:
    print("Die naam is niet gevonden in de lijst, we voegen hem nu toe...")
    namenLijst.append(gekozenNaam)

print (namenLijst)