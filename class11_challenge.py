#Challenge: Make a Rock, Paper, Scissor. Use 2 players

player_one = input("Select Rock, Paper or Scissor: ")
player_two = input("Select Rock, Paper or Scissor: ")

# if player_one == "Rock" and player_two == "Rock":
#     print("This is a draw. Both players selected Rock")
# elif player_one == "Paper" and player_two == "Paper":
#     print("This is a draw. Both players selected Paper")
# elif player_one == "Scissor" and player_two == "Scissor":
#     print("This is a draw. Both players selected Scissor")
# elif player_one == "Rock" and player_two == "Scissor":
#     print("This is a win for player ONE. Player two was killed with a ROCK")
# elif player_one == "Scissor" and player_two == "Rock":
#     print("This is a win for player TWO. Player one was killed with a ROCK")
# elif player_one == "Rock" and player_two == "Paper":
#     print("This is a win for player TWO. Player one was killed with a PAPER")
# elif player_one == "Paper" and player_two == "Rock":
#     print("This is a win for player ONE. Player two was killed with a PAPER")
# elif player_one == "Scissor" and player_two == "Paper":
#     print("This is a win for player ONE. Player two was killed with a SCISSOR")
# elif player_one == "Paper" and player_two == "Scissor":
#     print("This is a win for player ONE. Player one was killed with a SCISSOR")

# if player_one == "Rock":
#     if player_two == "Rock":
#         print("This is a draw. Both players selected Rock")
#     elif player_two == "Paper":
#         print("This is a win for player TWO. Player two was killed with a PAPER")
#     elif player_two == "Scissor":
#         print("This is a win for player ONE. Player two was killed with a ROCK")
# elif player_one == "Paper":
#     if player_two == "Rock":
#         print("This is a win for player ONE. Player two was killed with a PAPER")
#     elif player_two == "Paper":
#         print("This is a draw. Both players selected Paper")
#     elif player_two == "Scissor":
#         print("This is a win for player TWO. Player two was killed with a SCISSOR")
# elif player_one == "Scissor":
#     if player_two == "Rock":
#         print("This is a win for player TWO. Player two was killed with a ROCK")
#     elif player_two == "Paper":
#         print("This is a win for player ONE. Player two was killed with a SCISSOR")
#     elif player_two == "Scissor":
#         print("This is a draw. Both players selected Scissor")

if player_one == player_two:
    print("This is a draw. Both players selected:", player_one)
elif (player_one == "Rock" and player_two == "Scissor") or (player_one == "Scissor" and player_two == "Paper") or (player_one == "Paper" and player_two == "Rock"):
    print("This is a win for player ONE. Player two was killed with a: ", player_one)
else:
    print("This is a win for player TWO. Player two was killed with a: ", player_two)