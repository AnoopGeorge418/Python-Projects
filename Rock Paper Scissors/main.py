# Rock Paper Scissors - Simple Game that follows some rules against a player
# Rules:
    # 1. Rock wins against scissors.
    # 2. Scissors win against paper.
    # 3. Paper wins against rock.

import random

# list of choices
choices = ['Rock', 'Paper', 'Scissors']

# Welcome Note
print('Welcome to Rock Paper Scissors Game.')

# Asks for user input to make choice
user_choice = input("Make your choice: R(Rock), S(Scissors), P(Paper) ").capitalize()

# r or rock -> Rock
# p or paper -> Paper
# s or scissors -> Scissors
# else Invalid choice
if user_choice == 'R' or user_choice == 'Rock':
    user_choice = 'Rock'
    print(f'Your Choice: {user_choice}')
elif user_choice == 'P' or user_choice == 'Paper':
    user_choice = 'Paper'
    print(f'Your Choice: {user_choice}')
elif user_choice == 'S' or user_choice == 'Scissors':
    user_choice = 'Scissors'
    print(f'Your Choice: {user_choice}')
else:
    print("Invalid choice! Make sure to choose from R(Rock), S(Scissors), P(Paper).")

# Computer choice
computer_choice = random.choice(choices)
print(f'Computer Choice: {computer_choice}')

# Determine the winner
if user_choice == computer_choice:
    print("It's a Tie!!")
elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
     (user_choice == 'Scissors' and computer_choice == 'Paper') or \
     (user_choice == 'Paper' and computer_choice == 'Rock'):
        print('Huray....You Win!!')
else:
    print('You Lose.. Try again!')