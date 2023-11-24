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