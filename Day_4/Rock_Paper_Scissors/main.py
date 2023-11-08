rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]

# rock beats scissors
# scissors beat paper
# paper beats rock

# rock = 0
# paper = 1
# scissors = 2

user_choice_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice_number > 2 or user_choice_number < 0:
    print("You lose, invalid input")
else:
    print(choices[user_choice_number])

# user_choice = choices[user_choice_number]
# Generate the computer choice which is by random
computer_choice_number = random.randint(0, len(choices) - 1)
computer_choice = choices[computer_choice_number]
print(f"Computer chose: {computer_choice}")

if user_choice_number == computer_choice_number:
    print("It's a draw.")
elif user_choice_number == 0 and computer_choice_number == 1:
    print("You lose, paper beats rock")
elif user_choice_number == 0 and computer_choice_number == 2:
    print("You win, rock beats scissors")
elif user_choice_number == 1 and computer_choice_number == 2:
    print("You lose, scissors beats paper")
elif user_choice_number == 1 and computer_choice_number == 0:
    print("You win, paper beats rock ")
elif user_choice_number == 2 and computer_choice_number == 0:
    print("You lose, rock beats scissors")
elif user_choice_number == 2 and computer_choice_number == 1:
    print("You win, scissors beats paper")
# else:
#     print("You lose, invalid input")