import random
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player, make your move!").lower()

if player1 == computer:
    print("It's a draw!")
elif player1 == "rock":
    if computer == "scissors":
        print("Computer picked scissors... You won!")
    elif computer == "paper":
        print("Computer picked paper... You lost!")
elif player1 == "paper":
    if computer == "rock":
        print("Computer picked rock... You won!")
    elif computer == "scissors":
        print("Computer picked scissors... You lost!")
elif player1 == "scissors":
    if computer == "paper":
        print("Computer picked paper... You win!")
    elif computer == "rock":
        print("Computer picked rock... You lost!")
else:
    print("Something went wrong. Please type 'rock', 'paper', or 'scissors'.")