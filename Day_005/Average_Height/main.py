# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total = 0
counter = 0

for height in student_heights:
    # print(height)
    total += int(height)
    counter += 1
    average = round(total / counter)

print(f"total height = {total}")
print(f"number of students = {counter}")
print(f"average height = {average}")