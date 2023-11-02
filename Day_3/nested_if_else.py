# Add to the rollercoaster program

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    
    if age > 18:
        print("Pay $12")
    elif age >= 12:
        print("Pay $7")
    else:
        print("Pay $5")
else:
    print("Sorry, you have to grow taller before you can ride")