# Add to the rollercoaster program

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    
    if age > 18:
        bill = 12
        print("Adult Prices are $12")
    elif age >= 12:
        bill = 7
        print("Youth Prices are $7")
    else:
        bill = 5
        print("Child Prices are $5")
        
    want_photo = input("Do you want your photo taken? Y or N ")
    if want_photo == "Y":
        bill+=3
    
    print(f"Your total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")