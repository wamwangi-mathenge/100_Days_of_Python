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

# Use a while loop to allow the user to conduct many calculations

def calculator():
    num1 = int(input("What's the first number?: "))


    # Use a for loop to loop through "operations" and print out each of the symbols

    for key in operations:
        print(key)
        
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation: ")

        num2 = int(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: " )
        if choice == 'y':
            num1 = answer
        else:
            continue_calculation = False
            # Recursion => Call the very first function and start a new calculation
            # WARNING: Make sure that there is a condition before a function can call itself to avoid an infinite loop
            calculator()
            
            
calculator()