height = input()

weight = input()
# print(type(height))
# print(type(weight))
height_squared = float(height)  ** 2
# print(height_squared)
# print(type(height_squared))

bmi = float(weight) / height_squared
print(int(bmi))