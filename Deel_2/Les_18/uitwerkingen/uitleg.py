def get_integer(vraag):
    getal = int(input(vraag))
    return getal
def get_float(floating):
    getal2 = float(input(floating))
    return getal2
def get_string(string):
    word = str(input(string))
    return (word)
def get_letter(letter):
    word2 = input(letter)
    if len(word2) != 1:
        print ("voer een letter in")
        word2 = ""
    elif not(letter in word2):
        print ('voer een letter in')
    
    return word2

    




    