from logo import logo
import os

print(logo)
print("Welcome to the Secret Auction Program")
continue_bid = True
bidders = {}

def find_highest_bid(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while continue_bid:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders[name] = bid
    # print(bidders)
    # find_highest_bid(bidders)
    
    choice = input(("Are there any other bidders? Type 'yes' or 'no'. "))
    clear_screen()
    if choice == "no":
        continue_bid = False
        print("Bids Closed!!")
        find_highest_bid(bidders)

