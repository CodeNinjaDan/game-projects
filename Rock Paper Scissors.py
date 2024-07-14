import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper or 's' for scissors\n: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
      return "It's a draw!"
    
    if is_win(user, computer):
       return "You won!"
    
    # optionally use: if is_win(computer, user):
    return "You lost!"

def is_win(player, opponent):
   #return True if player wins
   if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') \
       or (player == 'r' and opponent == 's'):
       
       return True
   
print(play())