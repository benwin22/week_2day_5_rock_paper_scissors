#rules of the game for reference:
#rock breaks scissors = win
#scissors cut paper = win
#paper covers rock = win
# need a player, a computer (ryan said use *random* import)
# need conditionals for each rule of game (1 each for play, 1 each for computer)
#player=rock computer=paper (player lost)
#player=scissors computer=rock (player lost)
#player=paper computer=scissors (player lost)

#computer=rock player=paper (computer lost)
#computer=scissors player=rock (computer lost)
#computer=paper player=scissors (computer lost)
# has to end
#has to say thanks


import random

player_move = input("Make your move (rock, paper, scissors, or quit):")
type_move = ["rock", "paper", "scissors", "quit"]
computer_move = random.choice(type_move)
print(f" player chose {player_move}, computer chose {computer_move}")

if player_move == computer_move:
    print("Same answer! Go again!")
elif player_move == "rock":
    if computer_move == "paper":
        print("paper covers rock. You lost")
elif player_move == "scissors":
    if computer_move == "rock":
        print("paper covers rock. You lost")
elif player_move == "paper":
    if computer_move == "scissors":
        print("paper covers rock. You lost")
elif computer_move == "rock":
    if player_move == "paper":
        print("paper covers rock. You won")
elif computer_move == "scissors":
    if player_move == "rock":
        print("paper covers rock. You won")
elif computer_move == "paper":
    if player_move == "scissors":
        print("paper covers rock. You won")
# when player chooses quit, computer still makes a random choice...
# if random choice for computer == quit, game continues...
# not sure how to fix....
if player_move == "quit":
        print(f"Thanks for playing")
# break
