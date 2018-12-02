import random

options = ["Rock", "Paper", "Scissors"]
play = True

player_score = 0
comp_score = 0

while play == True:
    comp_pick = options[random.randint(0, 2)]
    print("The score is " + str(player_score) + " to " + str(comp_score) + "\n")
    player = input("Pick Rock, Paper, Scissors or Stop: \n")
    if player == "Stop":
        play = False
    elif player == comp_pick:
        print("Tie Game")
    elif player == "Rock":
        if comp_pick == "Paper":
            print("You Lose! Paper covers Rock")
            comp_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player == "Paper":
        if comp_pick == "Scissors":
            print("You Lose! Scissors cuts Paper")
            comp_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player == "Scissors":
        if comp_pick == "Rock":
            print("You Lose! Rock smashes Scissors")
            comp_score += 1
        else:
            print("You win!")
            player_score += 1
    else:
        print("Invalid input, check caps")











