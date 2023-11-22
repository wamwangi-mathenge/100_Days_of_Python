from logo import logo

print(logo)
print("Welcome to the Secret Auction Program")

bidders = {}

name = input("What is your name? ")
bid = input("What is your bid? $")

# bidders[name] = bid
# print(bidders)

def add_bid(name, bid):
    bidders[name] = bid
    print(bidders)
    
add_bid(name, bid)
