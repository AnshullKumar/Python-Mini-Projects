# Password Manager
# ----------------
# 1. Imports letters, digits, and symbols.
# 2. Builds a pool of characters based on user choices.
# 3. Randomly picks characters until password meets length and criteria (numbers/specials if required).
# 4. Returns and prints the generated password.


import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
    return pwd

min_Length = int(input("Enter the minimum length of your password: "))
has_number = input("Do you want to have numbers (y/n)?: ").lower() == "y"
has_special =  input("Do you want to hae special characters (y/n)?: ").lower() == "y"
pwd = generate_password(min_Length, has_number, has_special)
print("The generated password is: ", pwd)