# Import the random module.
import random
import my_module

# random_integer = random.randint(1, 10) # (1, 10) represents the range

# print(random_integer)

# print(my_module.pi)

# Generating a random float
random_float = random.random()
print(random_float) # Generates a random float between 0 and 1


# Generate a random float between 0 and 5
random_float_05 = random.random() * 5
print(random_float_05)
