# Functions with Multiple Inputs

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome to {location}")
    
# Calling the function using Positional Arguments
greet_with("Brian", "London")
greet_with("Maxine", "Paris")

print("-------------------------------------")

# Calling the function using Keyword Arguments
greet_with(name="Joe", location="Washington")
greet_with(name="Vladimir", location="Moscow")