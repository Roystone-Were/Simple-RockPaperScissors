print("WELCOME TO THE ROCK PAPER SCISSORS GAME")

player1 = input("Player1 make you move ")
player2 = input("Player2 make you move ")


if player1 == player2:
    print(f"Its a DRAW you\nYOU BOTH PLAYED {player2}")
    
#Rock Conditions
elif player1 == "rock":
    if player2 == "scissors":
        print(f"Player1 Wins he played {player1}")
    elif player2 == "paper":
        print(f"Player2 Wins he played {player2}")
        
#Paper Conditions
elif player1 == "paper":
    if player2 == "scissors":
        print(f"Player2 Wins he played {player2}")
    elif player2 == "rock":
        print(f"Player1 Wins he played {player1}")
        
#Scissors Conditions
elif player1 == "scissors":
    if player2 == "rock":
        print(f"player2 Wins he played {player2}")
    elif player2 == "paper":
        print(f"Player1 Wins he played {player1}")

#else
else: 
    print("ENTER CORRECT ARGUMENT")
    