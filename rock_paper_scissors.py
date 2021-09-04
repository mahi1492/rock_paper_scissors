import random
print("\n\n")

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
game = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))
print(game[user_choice])

print("\n")

computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(game[computer_choice])

if (user_choice == 0 and computer_choice == 2) :
  print("You win")
elif (user_choice == 1 and computer_choice == 0) :
  print("You win")
elif (user_choice == 2 and computer_choice == 1) :
  print("You win")
elif (user_choice == 0 and computer_choice == 0) :
  print("Draw")
elif (user_choice == 1 and computer_choice == 1) :
  print("Draw")
elif (user_choice == 2 and computer_choice == 2) :
  print("Draw")
else :
  print("You lose")
