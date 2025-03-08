import random as r

choose = ['Rock', 'Paper', 'Scissors']

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
computer_choice = r.randint(0, 2)

print(f"You chose {choose[user_choice]}")
print(f"Computer chose {choose[computer_choice]}")

def game():
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

# Run game
game()