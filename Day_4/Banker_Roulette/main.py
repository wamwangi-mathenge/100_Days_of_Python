import random
names_string = input()
names = names_string.split(", ")

print(names)

# random_number = random.randrange(len(names))
# random_name = names[random_number]
# # print(random_name)

# print(f"{random_name} is going to buy the meal today!")

list_length = len(names)

random_number = random.randint(0, list_length - 1)
# print(random_number)
# print(names[random_number])
random_name = names[random_number]
print(f"{random_name} is going to buy the meal today!")