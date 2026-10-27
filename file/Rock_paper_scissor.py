import random
print("Welcome to the game of Rock, Paper, Scissors")
'''Rules are simple:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock'''
user_score=0
computer_score=0
for i in range(1,10):
    print(f"Round {i}")
    user_inp=input("choose one input among rock paper and scissor:")
    computer_input=random.choice(["rock","paper","scissors"])
    print(f"computer chose {computer_input}")
    if(user_inp==computer_input):
        print("game is draw")
    elif((user_inp=="rock" and computer_input=="scissors") or (user_inp=="scissors" and computer_input=="paper") or (user_inp=="paper" and computer_input=="rock")):
        user_score=user_score+1
        print("user wins and user score is",user_score)
    else:
        computer_score=computer_score+1
        print("computer wins and computer score is",computer_score)
print("Final score of user is",user_score)
print("Final score of computer is",computer_score)
if(user_score>computer_score):
    print("user wins the game")
else:
    print("computer wins the game")
