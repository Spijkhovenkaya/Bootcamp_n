a = 9
b = 6
c = 8

if a > b and a > c:
    grootste = "a"
elif b > a and b > c:
    grootste = "b"
else:
    grootste = "c"

print(f"Variabele {grootste} is het grootst.")

a = float(input("Voer de waarde van a in: "))
b = float(input("Voer de waarde van b in: "))
c = float(input("Voer de waarde van c in: "))

if a > b and a > c:
    grootste = "a"
elif b > a and b > c:
    grootste = "b"
else:
    grootste = "c"

print(f"Variabele {grootste} is het grootst.")