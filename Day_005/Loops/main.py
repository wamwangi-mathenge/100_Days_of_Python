# For Loop

# Iterating over a list using a For Loop
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    # print(fruit)
    print(f"{fruit} pie")
    
print("-----------------------")
    
# Range Function
for number in range(1, 11):
    print(number)
    
print("--------------------------")
    
# To change the increment value
for number2 in range(1, 20, 3):
    print(number2)
    
print("------------------------")

# Increment the values from 1 to 100
total = 0
for number3 in range(1, 101):
    total+=number3
    
print(total)