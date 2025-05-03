import sys
import os

print("Welcome to Secret Auction!!")

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while continue_bidding:
    name = input("What is your name? ").title()
    price = int(input("What is your bid?: $ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    if should_continue.lower() == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen