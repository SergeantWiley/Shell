import random

index = {"Rock": 0,"Paper": 1, "Scissors": 2}
inverse_index = {0: "Rock", 1: "Paper", 2: "Scissors"}
computer = random.randint(0,2)
player = input("Enter one of Rock, Paper, or Scissors: ")
player = index[player]
if player == computer:
    print("Draw")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 0 and computer == 1:
    print("You lose")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 0 and computer == 2:
    print("You win")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 1 and computer == 2:
    print("You lose")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 1 and computer == 0:
    print("You win")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 2 and computer == 0:
    print("You lose")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])
elif player == 2 and computer == 1:
    print("You win")
    print("Computer picked:", inverse_index[computer])
    print("You picked:", inverse_index[player])

