# Making a Slot Machine
# Here we take an amount from the user, on which line they are betting on and their bet
#  


Max_lines = 3
Min_bet = 1
Max_bet = 100


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
    bet = get_bet()
    
    print(balance,lines)


main()
