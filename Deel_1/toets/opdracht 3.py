naam = (input("wat is jou naam"))
leeftijd = int(input("wat is jou leeftijd"))

if leeftijd <18:
    input ("Beste" + naam +" , je bent nog geen 18. Alleen autorijden zit er dus niet in")
else:
    print("Beste " + naam + ", je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).")