# First we create a file called Story.txt
# And asked AI to make us a story with placeholders.
# Then copied that story into the Story.txt file.
# Now we will read the story, find the placeholders,
# And ask the user to fill in the blanks.

with open("Story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    replace_word = answers[word]
    story = story.replace(word, replace_word)

print(story)