import random
def user_guess(x):
    random_number=random.randint(1,x)
    guess=0
    attempt=0
    while guess!= random_number:
        attempt+=1
        guess=int(input(f"Enter a number between 1 and {x}"))
        if guess< random_number:
            print("Sorry, guess a larger number")
        elif guess < random_number:
            print("Sorry, guess a lower number")

    print(f"Yay!Congrats.You have guessed the number {random_number} correctly in {attempt} attempts.")

def computer_guess(x):
    low=1
    high=x
    feedback=' '
    count=0
    while feedback!= 'c':
        count+=1
        if low!=high:
            guess= random.randint(low,high)
        else:
            guess=low
        feedback= input(f"Is the number {guess} too high(H), too low(L) or correct(C)").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Yay! Computer has guessed your number {guess} correctly in {count} attempts")

print("_____Welcome to number guessing game_____\n")
print("Player Guess(press G)? or Computer guessg(press C)?")
res=input().upper()
x=int(input("Enter the highest number upto which the game shall work "))
if res=='G':
    user_guess(x)
elif res=="C":
    computer_guess(x)
else:
    print("Invalid entry")



