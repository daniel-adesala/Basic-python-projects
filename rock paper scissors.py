#Rock, Paper, Scissors
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
options = [Rock, Paper, Scissors]
user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_number = random.randint(0, 2)

user_choice = options[user_number]
computer_choice = options[computer_number]

if user_number > 2 or user_number < 0:
    print("Invalid choice. Game Over!")
else:
    print(f"""
You chose:
{user_choice}
              
computer chose:
{computer_choice}
              
          """)
    if user_choice == computer_choice:
        print("it's a draw!!")
    elif user_number == 0 and computer_number == 2:
        print("You win!!")
    elif user_number == 2 and computer_number == 0:
        print("Computer wins!!")
    elif user_number == 2 and computer_number == 1:
        print("You win!!")
    elif user_number == 1 and computer_number == 2:
        print("Computer wins!!")
    elif user_number == 0 and computer_number == 1:
        print("Computer wins!!")
    elif user_number == 1 and computer_number == 0:
        print("You win!!")
