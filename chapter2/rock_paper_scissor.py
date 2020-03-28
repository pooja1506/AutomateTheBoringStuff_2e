import random , sys
print('rock','paper','scissor')

#To keep the track of winning , losses and ties
wins=0
losses=0
ties=0

while True:
    print("Enter - r , p , s , q")
    playerMove = input()
    if playerMove == 'q':
        sys.exit()
    if playerMove=='r' or playerMove=='p' or playerMove=='s':
        break #break out through player input loop

    #Display what the player choose
    if playerMove == 'r':
        print("rock versus")
    elif playerMove == 's':
        print("scissor versus")
    elif playerMove == 'p':
        print("paper versus")

#Display what computer choose

randomNumber = random.randint(1,3)
if randomNumber == 1 :
    computerMove = 'r'
    print("rock")
elif randomNumber == 2:
    computerMove = 's'
    print("scissor")
elif randomNumber == 3:
    computerMove = 'p'
    print("paper")


# Display and record the win/loss/tie:
if playerMove == computerMove:
    print('It is a tie!')
    ties = ties + 1
elif playerMove == 'r' and computerMove == 's':
    print('You win!')
    wins = wins + 1
elif playerMove == 'p' and computerMove == 'r':
    print('You win!')
    wins = wins + 1
elif playerMove == 's' and computerMove == 'p':
    print('You win!')
    wins = wins + 1
elif playerMove == 'r' and computerMove == 'p':
    print('You lose!')
    losses = losses + 1
elif playerMove == 'p' and computerMove == 's':
    print('You lose!')
    losses = losses + 1
elif playerMove == 's' and computerMove == 'r':
    print('You lose!')
    losses = losses + 1

print(losses)
print(wins)
print(ties)
