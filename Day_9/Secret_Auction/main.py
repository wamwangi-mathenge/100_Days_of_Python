from logo import logo

print(logo)
print("Welcome to the Secret Auction Program")

bidders = {}
def add_bid(name, bid):
    bidders[name] = bid
    print(bidders)

continue_bid = True
while continue_bid:

    name = input("What is your name? ")
    bid = input("What is your bid? $")

    add_bid(name, bid)
    
    choice = input(("Are there any other bidders? Type 'yes' or 'no'. "))
    if choice == "no":
        continue_bid = False
        print("Bids Closed")
