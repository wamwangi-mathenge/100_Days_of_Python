# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# Create a dictionary where the keys are each of these symbols and the values are the names of the functions.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))


# Use a for loop to loop through "operations" and print out each of the symbols

for key in operations:
    print(key)
    
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number? "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")