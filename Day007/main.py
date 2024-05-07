import random
import os
from time import sleep
from enum import Enum

from hangman_words import word_list
from hangman_art import stages, logo


class GameState(Enum):
    in_progress = 1
    lose = 2
    win = 3


def display_ui(message: str):
    os.system('cls||clear')
    print(stages[lives])
    print(f"{' '.join(player_word)}")
    print(f"\n{message}.")


def display_logo() -> None:
    print(logo)
    sleep(1)


game_state = GameState.in_progress
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1

player_word = []
for _ in range(word_length):
    player_word += "_"

guesses = []
message = f"The solution is {chosen_word}"

display_logo()

while game_state == GameState.in_progress:
    display_ui(message)
    guess = input("Guess a letter: ")

    if not str.isalpha(guess) or len(guess) is not 1:
        message = f"The input {guess} was not a letter"
        continue

    guess = guess.lower()
    if guess in guesses:
        message = f"Letter {guess} have been already selected"
        continue

    guesses.append(guess)
    if guess not in chosen_word:
        message = f"The word does not contains letter {guess}"

        lives -= 1
        if lives == 0:
            game_state = GameState.lose

    else:
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                player_word[position] = letter

        if "_" not in player_word:
            game_state = GameState.win


if game_state == GameState.win:
    display_ui("You win")
else:
    display_ui(f"You lose, the solution was {chosen_word}")
