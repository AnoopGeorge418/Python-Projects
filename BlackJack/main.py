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
            bid_amount = 1000
            bank = 0            
            print(f"Bid amount is '{bid_amount}' and Bank total is '${bank}'")
            card_selection()
        elif all_in_bid == 'n':
            amount = input("Enter the amount you want to bid or or 'exit': ")
            clear_bid = input("Do you want to clear the bid amount? Type 'y' or 'n' or 'exit': ").lower()
            if clear_bid == 'y':
                bid_amount = 0 
                print(f"Bid amount is '{bid_amount}' and Bank total is '${bank}'")
            elif clear_bid == 'exit':
                game_ended(player_name)  
            else:
                bid_amount = float(amount)
                if bid_amount > bank:
                    print(f"Insufficient amount! Please Try Again!")
                elif bid_amount <= bank:
                    bank -= bid_amount
                    print(f"Bid amount is '{bid_amount}' and Bank total is '${bank}'")
                    card_selection()
                elif amount == 'exit':
                    game_ended(player_name)            
        elif all_in_bid == 'exit':
            game_ended(player_name)
                
        
def card_selection():
    cards = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "A": None,
        "J": 11,
        "Q": 12,
        "k": 13,
    }      
    
    random_card = random.choice(list(cards.keys()))
    if random_card == "A":
        value_for_A = input("Choose a Value for 'A' (1 or 11): ")
        return value_for_A
    
    return cards(random_card)
    
    
def user_card_game():
    TARGET = 21
    current_score = 0
    
    random_card = card_selection()
    current_score += random_card
    print(f"Your card Score: {current_score}")
    
    while True:
        hit_or_stand = input("Do you want to 'Hit' or 'Stand'? ").lower()
        
        if hit_or_stand == 'hit':
            new_value = card_selection()
            current_score += new_value
            print(f"You drew {new_value}. Your card Score: {current_score}")

            if current_score == TARGET:
                print("You win")
                break
            elif current_score > TARGET or current_score < TARGET:
                print("You Lose!")
                break
        elif hit_or_stand == "stand":
            current_score = random_card
            print(f"Your card Score: {current_score}")
    
    
    
    
def computer_card_game():
    random_Card = card_selection()
    print(random_card)
    
    
    
    
    
    
    
    
    
    
def game_ended(player_name):
    print(f"Exiting the Game!! I'll wait for you'r return '{player_name}'")
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
