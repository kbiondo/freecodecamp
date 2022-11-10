import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}
  return choices

def check_win(player, computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock": 
    if computer == "paper":
      return "Player fails"
    else:
      return ("player wins")
  elif player == "scissors":
    if computer == "paper":
      return ("player wins!")
    else:
      return ("player fails")
  elif player == "paper":
    if computer == "rock":
      return ("player wins!")
    else:
      return ("player fails")

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
#print(choices)
print(result)

#check_win(get_choices())
#check_win("paper", "rock")