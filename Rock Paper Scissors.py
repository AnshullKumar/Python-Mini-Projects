print("Welcome to The Rock Paper Scissors game!")

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]



while True:
    user_input = input("Enter Rock, Paper, or Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("Thanks for playing!")
        break
    if user_input not in options:
        print("Invalid input, please try again.")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}")