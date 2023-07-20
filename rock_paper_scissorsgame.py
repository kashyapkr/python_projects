import random

exit=False
user_points=0
comp_points=0
while exit == False:
    options=["rock","paper","scissor"]
    user_input=input("\nChoose rock,paper,scissor or exit")
    comp_input= random.choice(options)

    if user_input=='exit':
        print("Game Ended")
        print(f"Your score:{str(user_points)} ",end=' ')
        print(f"Computer score:{str(comp_points)}",end=" ")
        if user_points > comp_points:
            print("\nYou won the game")
        elif user_points < comp_points:
            print("\nYou lost the game")
        else:
            print("\nITS A TIE")
        exit=True
        break

    if user_input=="rock":
         if comp_input=="rock":
             print("You entered rock")
             print("Computer input is rock\n")
             print("Its a tie\n")
         elif comp_input == "paper":
             print("You entered rock")
             print("Computer input is paper\n")
             print("Computer wins\n")
             comp_points+=1
         elif comp_input == "scissor":
             print("You entered rock")
             print("Computer input is Scissor\n")
             print("You won\n")
             user_points+=1
    elif user_input=="paper":
         if comp_input=="rock":
             print("You entered paper")
             print("Computer input is rock\n")
             print("You won\n")
             user_points+=1
         elif comp_input == "paper":
             print("You entered paper")
             print("Computer input is paper\n")
             print("Its a tie\n")

         elif comp_input == "scissor":
             print("You entered paper")
             print("Computer input is Scissor\n")
             print("Computer won\n")
             comp_points+=1
    elif user_input == "scissor":
        if comp_input == "rock":
            print("You entered scissor")
            print("Computer input is rock\n")
            print("Computer Won\n")
            comp_points += 1
        elif comp_input == "paper":
            print("You entered scissor")
            print("Computer input is paper\n")
            print("You Won\n")
            user_points+=1

        elif comp_input == "scissor":
            print("You entered scissor")
            print("Computer input is Scissor\n")
            print("Its a tie\n")


    else :
         print("\n INVALID")

