naam = input('Wat is uw naam?: ')

favcolor = input(f'Wat is jouw favoriete kleur, {naam}? A) Rood, B) Blauw, C) Geel of D) Groen of E) Paars of F) Roze ')
mytuple = ("rood", "blauw", "geel", "groen", "paars", "roze")

if favcolor.lower() == 'a':
    print("Zo rood als een roos.")
elif favcolor.lower() == 'b':
    print("Zo blauw als de zee.")
elif favcolor.lower() == 'c':
    print("Zo geel als de zon.")
elif favcolor.lower() == 'd':
    print("Zo groen als gras.")
elif favcolor.lower() == 'e':
    print("Zo paars als bosbessen.")
elif favcolor.lower() == 'f':
    print("Zo roze als een bloem.")
else:
    print("Deze kleur is niet zo geweldig!")