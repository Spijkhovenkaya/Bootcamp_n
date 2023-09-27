getallen_lijst = [0 , 1 , 2 , 3, 4]

print (getallen_lijst)



try:
        getal = int(input("Voer een getal in die je weg wilt hebben (0-4) "))
     
         
except ValueError:
    print("Die staat niet tussen 0-4")

getallen_lijst.pop (getal)

print (getallen_lijst)