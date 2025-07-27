print('Welcome to the Number Guessing Game!')

import random
def start_game():
    top_number = input('Type a number: ')

    if top_number.isdigit():
        top_number = int(top_number)
        if top_number <= 0:
            print('Please type a number greater than 0 next time.')
            quit()
    else:
        print('Try again type a number.')
        quit()


    random_number = random.randint(0,top_number)
    print(f'You are guessing a number between 0 and {top_number}.')

    guesses_count = 0

    while True:
        guesses_count += 1
        user_guess = input('Make a guess: ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time. ")
            continue

        if user_guess == random_number:
            print('You guessed it right!')
        else:
            if user_guess < random_number:
                print('You guessed a number too low!')
            else:
                print('You guessed a number too high!')
            continue
        break
    print(f'You got it in' ,guesses_count,' guesses!')

if __name__ == "__main__":
    start_game()
    while input('Do you want to play again? (yes/no): ').lower() == 'yes':
        start_game()
    print('Thanks for playing! Goodbye!')