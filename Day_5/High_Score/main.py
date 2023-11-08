# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

sorted_scores = sorted(student_scores)
print(sorted_scores)

for score in sorted_scores:
    highest_score = sorted_scores[-1]
    
print(f"The highest score in the class is: {highest_score}")