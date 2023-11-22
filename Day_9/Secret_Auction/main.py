from logo import logo

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

while continue_bid:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders[name] = bid
    # print(bidders)
    # find_highest_bid(bidders)
    
    choice = input(("Are there any other bidders? Type 'yes' or 'no'. "))
    if choice == "no":
        continue_bid = False
        print("Bids Closed!!")
        find_highest_bid(bidders)

