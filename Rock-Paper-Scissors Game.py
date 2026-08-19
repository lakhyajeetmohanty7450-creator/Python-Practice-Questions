# Write a Python program to create a console-based Rock-Paper-Scissors game where the user plays against the computer.

import random

lst = ["Rock","Paper","Scissor"]
computer = random.choice(lst)
def Rock_Paper_Scissors():
    computer = random.choice(lst)
    choose = input("Your chosse: ")

    if choose == "Rock" and  computer == "Paper":
        print("computer win")
    elif choose == "Paper" and computer == "Scissor":
        print("compyter win")
    elif choose == "Scissor" and computer == "Rock":
        print("compter win")
    elif choose == computer:
        print("DRAW")
    else:
        print("You win")


Rock_Paper_Scissors()

