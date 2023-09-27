from user_input2 import*

def get_position() -> str:
    position = 0
    while position < 11 or position > 33:
        position = get_integer("Kies een vakje tussen 11 en 33: ")
        # print("Kies een waarde tussen 11 en 33")
    
    return str(position)



rij_1 = ["u","u","u"]
rij_2 = ["u","u","u"]
rij_3 = ["u","u","u"]

print(rij_1)
print(rij_2)
print(rij_3)

# move speler 1 - x
move = get_position() 
print (move)
print(move[0])