import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def play_rps():
    playagain = True

    while playagain:
        playerchoice = input("\nEnter your choice:\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        try:
            player = int(playerchoice)
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        if player < 1 or player > 3:
            print("You must enter 1, 2, or 3.")
            continue

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou choose " + str(RPS(player)).replace('RPS.','') + ".")
        print("Python choose " + str(RPS(computer)).replace('RPS.','') + ",\n")

        if player == 1 and computer  == 3:    
            print("😁 You Wins Bad Ass !")
        elif player == 2 and computer  == 1:    
            print("😁 You Wins Bad Ass !")
        elif player == 3 and computer  == 2:    
            print("😁 You Wins Bad Ass !")
        elif player == computer:
            print("😐 Shit! Tie Game")
        else:
            print("🐍😃🐍 Python Wins Bad Ass !")
        
        playagain_input = input("\nPlay again?\nY for Yes or \nQ to Quit \n\n")
        if playagain_input.lower() == "y":
            playagain = True
        else:
            print("\n✨🎈🎉🎆🎇🧨🎊")
            print("Thank you for playing!\n") 
            playagain = False  

if __name__ == "__main__":
    play_rps()
        .