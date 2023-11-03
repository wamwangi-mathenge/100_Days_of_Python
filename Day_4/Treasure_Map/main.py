line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# A = list[0]
# B = list[1]
# C = list[2]

# 1 = line1
# 2 = line2
# 3 = line3

# B3

# spot_position = map[int(position[1]) - 1]
# print(int(spot_position))

# # print(type(spot_position))

# # if position[0] == "A":
# #     column_position = map[spot_position[0]]
# # elif position[0] == "B":
# #     column_position = map[spot_position[1]]
# # else:
# #     column_position = map[spot_position[2]]
    
# # map[spot_position[column_position]] = "X"


# B3

gross_position = int(position[1]) - 1

if position[0].lower() == "a":
    map[gross_position][0] = "X"
elif position[0].lower() == "b":
    map[gross_position][1] = "X"
else:
    map[gross_position][2] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")