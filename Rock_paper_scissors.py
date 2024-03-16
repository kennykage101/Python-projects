rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors."))
if human_choice > 2 or human_choice < 0:
    print("You typed an invalid number. Try again")
else:
    print(choices[human_choice])
    computer_choice = random.randint(0,len(choices) - 1)
    print(f"Computer chose:\n{choices[computer_choice]}")
    

if human_choice == computer_choice:
    print("There is a draw")
elif human_choice == 0 and computer_choice == 1:
    print("You lose")
elif human_choice == 0 and computer_choice == 2:
    print("You win")
elif human_choice == 1 and computer_choice == 0:
    print("You win")
elif human_choice == 1 and computer_choice == 2:
    print("You lose")
elif human_choice == 2 and computer_choice == 0:
    print("You lose")
elif human_choice == 2 and computer_choice == 1:
    print("You win")
