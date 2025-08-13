

# Welcome to this game!
# This is a simple dice game called PIG.
# The rules are simple:
# Rules of the PIG Dice Game:
# 1. 2 to 4 players can play.
# 2. Players take turns rolling a single die.
# 3. On each turn, a player can roll as many times as they like.
# 4. If a player rolls a 1, they lose all points for that turn and their total score resets to 0. Their turn ends.
# 5. If a player rolls 2-6, the value is added to their current turn score.
# 6. At any time, a player can choose to bank their score(end their turn), adding their current turn score to their total score, thereby, banking.
# 7. The first player to reach or exceed 50 points wins.
# 8. Players can choose to quit the game; if two players quit in a row, the player with the highest score wins.

import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
    players = input("Enter the nubers of players (1-4): ")
    # We arent using " int(input()) " here because it might raise a Value Error and crash the program.
    # We will check if the input is a digit and then convert it to an integer to avoid this issue.
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 to 4 players")
    else:
        print("Invalid. Try again.")

max_score = 50
player_scores = [0 for _ in range(players)] 

while max(player_scores) < max_score:

    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s  turn to roll the dice. \n")
        current_score = 0
        while True:
                
            should_roll = input("DO you want to roll the dice? (y/n) or quit the game and decide the winner! (q): ").lower()
            quit_count = 0
            if should_roll == "q":
                quit_count += 1
                print(f"\nPlayer {player_index + 1} has chosen to quit the game.")
                quit = input(f"\nDoes player {player_index + 2} want to quit the game? (q/n): \n")
                
                if quit == "q":
                    quit_count += 1
                    print(f"\nPlayer {player_index + 2} has chosen to quit the game.")
                else:
                    print(f"\nPlayer {player_index + 2} has chosen to continue the game.\n")
                    break

                if quit_count == 2:
                    print("You have already quit the game. Exiting now.")
                print("Game quit by player.")
                
                max_score_now = max(player_scores)
                winning_index = player_scores.index(max_score_now)
                print(f"\nPlayer {winning_index + 1} wins with a score of {max_score_now}!")
                exit()
            
            
            if should_roll != "y":
                print(f"Player {player_index + 1} ends their turn with a score of {current_score}.")
                
                player_scores[player_index] += current_score
                
                print(f"Player {player_index + 1}'s total score is {player_scores[player_index]}")
                break
                
            value = roll()
            if value == 1:
                print("You rolled a 1. You lose your turn and score. ")
                current_score = 0
                print(f"Your score for this turn is: {current_score} and your total score is resetted to 0.")
                player_scores[player_index] = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
            print(f"Your current score is: {current_score}")
        
        #player_scores[player_index] += current_score
        print(f"Player {player_index + 1}'s total score is {player_scores[player_index]}")

max_score = max(player_scores)
Winning_index = player_scores.index(max_score)
print(f"\nPlayer {Winning_index + 1} wins with a score of {max_score}!")
