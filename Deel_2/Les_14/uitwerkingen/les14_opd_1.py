getallen_lijst = []

for i in range(5):
    getal = int(input("Voer een getal in: ")) 
    getallen_lijst.append(getal) 

print(f"De lijst met ingevoerde getallen is: {getallen_lijst}")

index = int(input("Voer een index in om een getal te verwijderen: "))

if 0 <= index < len(getallen_lijst):
    verwijderd_getal = getallen_lijst.pop(index)
    print(f"Het verwijderde getal is: {verwijderd_getal}")
    print(f"De bijgewerkte lijst is: {getallen_lijst}")
else:
    print("Ongeldige index. Voer een index in tussen 0 en 4.")
