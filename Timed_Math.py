# This is a timed math practice program.
# Here we take a set of random math problems and give the user a limited time to solve them.
# The user can input their answers, and the program will keep track of how many attempts were wrong.
# At the end, it will display the total time taken to solve all problems.

import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp) # eval() is used to calculate the result of the expression in string and give the output as an integer
    return exp, answer

wrong_attempts = 0
input("Presss Enter to start! ")
print("-------------------")

start_time = time.time() # Record the start time

for i in range(total_problems):
    exp, answer = generate_problem()
    
    while True:
        guess = input("Problem # " + str(i + 1) + ": " + exp + " = ")
        if guess == str(answer):
            break
        
        wrong_attempts += 1

end_time = time.time() # Record the end time
total_time = round(end_time - start_time, 2) # round() returns the result in 2 decimal places

print("-------------------")
print("Nice work! You finished in " + str(total_time) + "seconds.")
print("You had " + str(wrong_attempts) + " wrong attempts.")