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

# Write your code below this line 👇

import random
listofchoices = [rock, paper, scissors]
choice = -1
while choice not in [0,1,2]:
    try:
        choice= int(input("what do you choose? 0 for rock, 1 for paper, 2 for scissors"))
    except ValueError:
        print("Invalid input. Please enter 0,1 or 2")
print(f'your choice {listofchoices[choice]}')

computerchoice = random.randint(0,2)
print(f'computer chose {listofchoices[computerchoice]}')

current_situation = [choice, computerchoice]
wins = [(1,0), (2,1), (0,2)]
if choice == computerchoice:
    print("It's a draw!")
elif (choice, computerchoice) in wins:
    print("you win!")
else:
    print("computer wins!")