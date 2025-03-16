### Rock Paper scissors Game
import random

user_choice=int(input("Enter input as 0 , 1 ,2 --> 0 for Rock, 1 for paper, 2 for Scissors.: "))
if user_choice > random.randint(0,2) or user_choice < 0:
    print("You have given wrong Input\npls give 1 or 1 or 2")
else:
    computer_choice=random.randint(0,2)

    print(f"Your choice is: {user_choice}")
    print(f"Computer choice is: {computer_choice}")

    if user_choice == computer_choice:
        print("It's Draw")
    elif user_choice==0 and computer_choice==2:
        print("You win")
    elif user_choice==2 and computer_choice==0:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win")
    elif computer_choice > user_choice:
        print("You Lose")
