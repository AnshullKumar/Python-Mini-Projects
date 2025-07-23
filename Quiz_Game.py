print("Welcome to thee Quiz!")
print("This is a simple quiz game where you can test your knowledge.")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()

print("Great! Let's start the quiz :D")
print("You will be asked a series of 7 questions, answer them correctly to score points.")
points=0

answer = input("Q1. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")
    
answer = input("Q2. What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

answer = input("Q3. What does GPU stand for? ").lower()
if answer == "graphics processing unit" or answer == "graphic processor unit":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

answer = input("Q4. What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

answer = input("Q5. What does USB stand for? ").lower()
if answer == "universal serial bus":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

answer = input("Q6. What does 'www' stand for? ").lower()
if answer == "world wide web":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

answer = input("Q7. What does ROM stand for? ").lower()
if answer == "random access memory" or answer == "read only memory":
    print("Correct Answer!")
    points += 1
else:
    print("Wrong!")

print(f"You scored {points} points out of 7.")
print(f"You got {(points / 7) * 100:.2f}% correct.")

if points == 7:    
    print("Excellent! You are a quiz master!") 

print("Thank you for playing the quiz!")