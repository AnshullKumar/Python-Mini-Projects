#Welcome to the Adventure Game!
#Here we are exploring a simple text-based adventure game.
#Here im learning how to use if statements and input functions.
#This is a simple game where the player makes choices that affect the outcome.


name = input("Type your name: ")
print("Welcome" , name, "to the Adventure Game!")

answer = input("You are in a dirt road, it has come to an end and you can go left or right to go? (left/right)").lower()

if answer == "left":
    answer = input("You come to a river, do you want to walk around it or swim across? (swim/walk) ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator. Game over.")

    elif answer == "walk":
        print("You walked for miles, ran out of water and lost the game.")
    
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (back/cross) ").lower()

    if answer == "back":
        print("You go back and lose. Game over.")

    elif answer == "cross":
        print("Your crossed a bridge and u meet a stranger. Do you talk to him. (yes/no)").lower()
        
        if answer == "yes":
            print("You talk to the stranger and he gives you a treasure. You win!")
        elif answer == "no":
            print("You ignore the stranger and lose. Game over.")
    
    else:
        print("Not a valid option. You lose.")
    
    
else:
    print("Not a valid option. You lose.")

print("Thanks for playing the game", name )
