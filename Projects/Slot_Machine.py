# Making a Slot Machine
# Here we take an amount from the user, on which line they are betting on and their bet
#  

import random

Max_lines = 3
Min_bet = 1
Max_bet = 100

Rows = 3
Cols = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def check_win(columns, lines, bet, values):
    win = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            win += values[symbol] * bet
            win_line.append(line + 1)
    return win, win_line

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print() #new line by default


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
        amount = input("How much would u like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if Min_bet <= amount <= Max_bet:
                break
            else:
                print(f"Amount must be between ${Min_bet} - {Max_bet}.")
        else:
            print("Please enter a number.")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(F"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(Rows,Cols,symbol_count)
    print_slot_machine(slots)
    
    win, win_line = check_win(slots, lines, bet, symbol_count)
    print(f"You won ${win}.")
    print(f"You won on lines: ", *win_line)
    
    return win - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        
        if balance <= 0:
            print("You ran out of money! \nThe game ends here.")
            break
        if answer =="q":
            break
        balance += spin(balance)
        
        print(f"You left with ${balance}")

main()
