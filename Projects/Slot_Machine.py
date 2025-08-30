# Making a Slot Machine
# Here we take an amount from the user, on which line they are betting on and their bet
#  

import random

Max_lines = 3
Min_bet = 1
Max_bet = 100

Rows = 3
Columns = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows,columns,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [[],[],[]]
    for col in range(cols):
        column = []


def deposit():
    while True:
        amount = input("What would u like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the no. of lines to bet on (1-" + str(Max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= Max_lines:
                break
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would u like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if Min_bet <= amount <= Max_bet:
                break
            else:
                print(f"Amount must be between ${Min_bet} - {Max_bet}.")
        else:
            print("Please enter a number.")
    
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(F"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
