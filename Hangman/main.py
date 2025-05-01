import nltk
from nltk.corpus import words
import random

# nltk.download("words")  # Uncomment this once to download the corpus

# Setup
word_list = words.words()
random_words = random.sample(word_list, 100)
chosen_word = random.choice(random_words).lower()

placeholder = "_" * len(chosen_word)
correct_letters = set()
guessed_letters = set()
lives = 6
LEVELS = list("HANGMAN")
game_over = False

print("Word to guess:", placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        correct_letters.add(guess)
        replaced_word = "".join([letter if letter in correct_letters else "_" for letter in chosen_word])
    else:
        lives -= 1
        replaced_word = "".join([letter if letter in correct_letters else "_" for letter in chosen_word])
        print(f"Incorrect! You have {lives} lives left.")
        print("Progress:", "".join(LEVELS[:len(LEVELS) - lives]))

    print("Current word:", replaced_word)

    if "_" not in replaced_word:
        print("You win!!")
        game_over = True
    elif lives == 0:
        print("Game over! The word was:", chosen_word)
        game_over = True
