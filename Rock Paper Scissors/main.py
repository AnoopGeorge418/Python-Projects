import random

choices = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(choices)

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
if user_choice == '0':
    print('Your Choice: Rock')
if user_choice == '1':
    print("Your Choice: Paper")
if user_choice == '2':
    print("Your Choice: Scissors")

print(f'Computer Choice: {computer_choice}')

if (user_choice == '0' and computer_choice == "Scissors") or \
   (user_choice == '1' and computer_choice == 'Rock') or \
   (user_choice == '2' and computer_choice == 'Paper'):
    print("You Won!!")
else:
    print("You Lose!!")