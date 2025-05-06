import sys
import random
from art import text2art

def game_started(player_name):
    """This function game_started is responsible for bidding amount 

    Args:
        player_name (str): prompts user name
    """
    
    bank = 1000
    bid_amount = 0 
    print(f"You have total of '${bank}' in your bank account!")
    
    while True: 
        all_in_bid = input("Do you want to bid everything in your bank? Type 'y' or 'n' or 'exit': ").lower()
        if all_in_bid == 'y':
            bid_amount = bank
            bank = 0            
            print(f"Bid amount is '{bid_amount}' and Bank total is '${bank}'")
            user_card_game(player_name)
        elif all_in_bid == 'n':
            amount = input("Enter the amount you want to bid or 'exit': ").lower()
            if amount == 'exit':
                game_ended(player_name)
            if not amount.isdigit():
                print("Invalid amount. Try again.")
                continue
            bid_amount = float(amount)
            if bid_amount > bank:
                print(f"Insufficient amount! Please Try Again!")
            else:
                bank -= bid_amount
                print(f"Bid amount is '{bid_amount}' and Bank total is '${bank}'")
                user_card_game(player_name)
                break
        elif all_in_bid == 'exit':
            game_ended(player_name)
        else:
            print("Invalid input. Try again.")
                
        
def card_selection(is_player=True):
    cards = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10, "A": None, "J": 10,
        "Q": 10, "K": 10
    }

    random_card = random.choice(list(cards.keys()))
    if random_card == "A":
        if is_player:
            while True:
                value_for_A = input("Choose a Value for 'A' (1 or 11): ")
                if value_for_A in ["1", "11"]:
                    return int(value_for_A)
                else:
                    print("Please choose either 1 or 11.")
        else:
            return 11 
    return cards[random_card]
    
    
def user_card_game(player_name):
    TARGET = 21
    current_score = 0

    random_value = card_selection()
    current_score += random_value
    print(f"Your card Score: {current_score}")

    while True:
        hit_or_stand = input("Do you want to 'Hit' or 'Stand'? ").lower()

        if hit_or_stand == 'hit':
            new_value = card_selection()
            current_score += new_value
            print(f"You drew {new_value}. Your card Score: {current_score}")

            if current_score > TARGET:
                print("You Lose!")
                break
            elif current_score == TARGET:
                print("You win!")
                break
        elif hit_or_stand == "stand":
            print(f"Your final score: {current_score}")
            dealer_score = computer_card_game()
            print(f"Computer's score: {dealer_score}")
            if dealer_score > TARGET or current_score > dealer_score:
                print("You win!")
            elif current_score < dealer_score:
                print("You lose!")
            else:
                print("It's a draw!")
            break
        else:
            print("Invalid input. Please type 'Hit' or 'Stand'.")
    
def computer_card_game():
    TARGET = 21
    current_score = 0
    while current_score < 17:
        new_card = card_selection(is_player=False)
        current_score += new_card
    return current_score

def game_ended(player_name):
    print(f"Exiting the Game!! I'll wait for your return, '{player_name}'")
    sys.exit()

def main():
    print(f'{text2art("BlackJack")}\n')
    print("Welcome To BlackJack: The classic casino game where luck and strategy collide.")
    player_name = input("What is your name? ").capitalize()
    while True:
        play = input(f"Do you want to start the game '{player_name}'? Type 'y' or 'n': ").lower()
        if play == 'y':
            game_started(player_name)
        elif play == 'n':
            game_ended(player_name)
        else:
            print("Make Sure To Type Given Option")


if __name__ == "__main__":
    main()