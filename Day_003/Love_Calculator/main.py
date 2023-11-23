print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

couple_name = (f"{name1} {name2}").lower()
# print(couple_name)

first_count = 0
first_count+=couple_name.count("t")
first_count+=couple_name.count("r")
first_count+=couple_name.count("u")
first_count+=couple_name.count("e")
# print(first_count)

second_count = 0
second_count+=couple_name.count("l")
second_count+=couple_name.count("o")
second_count+=couple_name.count("v")
second_count+=couple_name.count("e")
# print(second_count)

str_couple_count = str(first_count) + str(second_count)
couple_count = int(str_couple_count)
print(type(couple_count))
# print(f"Your score is {couple_count}")

if couple_count < 10 or couple_count > 90:
    print(f"Your score is {couple_count}, you go together like coke and mentos.")
elif couple_count > 40 and couple_count < 50:
    print(f"Your score is {couple_count}, you are alright together.")
else:
    print(f"Your score is {couple_count}.")