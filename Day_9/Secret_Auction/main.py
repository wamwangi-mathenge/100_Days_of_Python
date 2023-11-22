from logo import logo

print(logo)
print("Welcome to the Secret Auction Program")

bidders = {}
# max_value = 0
# max_key = None
 
        

continue_bid = True
while continue_bid:

    name = input("What is your name? ")
    bid = input("What is your bid? $")

    bidders[name] = bid
    print(bidders)
    
    choice = input(("Are there any other bidders? Type 'yes' or 'no'. "))
    if choice == "no":
        continue_bid = False
        print("Bids Closed")
