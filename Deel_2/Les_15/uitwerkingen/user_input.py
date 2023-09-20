def get_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Voer een integer in.")

def get_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Voer een float in.")

def get_string(prompt):
    user_input = input(prompt)
    return user_input

def get_letter(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.upper()
        else:
            print("Ongeldige invoer. Voer één letter in.")
