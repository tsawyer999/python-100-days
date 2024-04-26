# 1. Concatenate both names and check for the number of times the letter in the word TRUE occurs
# 2. Then check for the number of times the letters in the word LOVE occurs
# 3. Then combine these numbers to make a 2 digits numbers

# For the scores less than 10 or greater than 90, the message should be:
# Your score is *x*, you go together like coke and mentos.

# For scores between 40 and 50, the message should be:
# Your score is *y*, you are alright together.
#
# Otherwise, the message will just be their score:
# Your score is *z*.

print("The love calculator is calculating your score...")
name1 = input("What is your name\n")
name2 = input("What is your their name\n")

# Don't change the code above

words = ("TRUE", "LOVE")
scorePerLetter = {}

for word in words:
    for letter in word:
        scorePerLetter[letter] = scorePerLetter.get(letter, 0) + 1

bothNames = name1.upper() + name2.upper()

score = 0
for letter in bothNames:
    score += scorePerLetter.get(letter, 0)

prefix = f"Your score is *{score}*, you go together like "

if 10 > score > 90:
    suffix = "coke and mentos"
elif 40 > score > 50:
    suffix = "rain and umbrella"
else:
    suffix = "banana and chocolate"

print(prefix + suffix)
