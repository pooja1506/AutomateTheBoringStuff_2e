import random
secret_number = random.randint(1,20)
print("I am thinking that number is between 1 to 20")

#Let the player take 6 guesses

for guessesTaken in range(1,7):
    print("take a guess")
    guess=int(input())


    if guess<secret_number:
        print("your guess is too low")
    elif guess>secret_number:
        print("your guess is too high")
    else:
        break

if guess==secret_number:
    print("you have guessed the right number in " + str(guessesTaken) + " times.")
else:
    print("The number i was thinking of is " + str(secret_number) + "number")