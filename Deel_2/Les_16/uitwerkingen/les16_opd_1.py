from user_input2 import *

integer_value = get_integer("Voer een integer in: ")
print("Ingevoerde integer:", integer_value)

float_value = get_float("Voer een float in: ")
print("Ingevoerde float:", float_value)

string_value = get_string("Voer een string in: ")
print("Ingevoerde string:", string_value)

letter_value = get_letter("Voer één letter in: ")
print("Ingevoerde letter:", letter_value)


# als het naar (zes) word veranderd dan blijft het de correcte

#def get_integer(zes):
#     while True:
#         try:
#             user_input = int(input(zes))
#             return user_input
#         except ValueError:
#             print("Ongeldige invoer. Voer een integer in.")

# def get_float(zes):
#     while True:
#         try:
#             user_input = float(input(zes))
#             return user_input
#         except ValueError:
#             print("Ongeldige invoer. Voer een float in.")
