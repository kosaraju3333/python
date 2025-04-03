## Guess The NUmber #####
import random
easy_attempts_left=10
hard_attempts_left=5
easy_attempts_used=0
hard_attempts_used=0
def easy_level(number):
    guess_number=int(input("Make a guess: "))
    if computer_number == guess_number:
        print("Your Guess is Right...")
        exit()
    elif guess_number < number:
        print("You guess is too low")
        global easy_attempts_used
        easy_attempts_used = easy_attempts_used + 1
    elif guess_number > number:
        print("You guess is too high")
        # global easy_attempts_used
        easy_attempts_used = easy_attempts_used + 1

def hard_level(number):
    guess_number=int(input("Make a guess: "))
    if computer_number == guess_number:
        print("Your Guess is Right...")
        exit()
    elif guess_number < number:
        print("You guess is too low")
        global hard_attempts_used
        hard_attempts_used = hard_attempts_used + 1
    elif guess_number > number:
        print("You guess is too high")
        # global easy_attempts_used
        hard_attempts_used = hard_attempts_used + 1

print("Guess The Number Game")
print("Let me think of a number between 1 to 50")
computer_number=random.randint(1,50)
game_level=input("Choose level of difficulty ...Type 'easy' or 'hard': ").lower()
if game_level == 'easy':
    easy_game_on  = True
    while easy_game_on:
        print(f"You have {easy_attempts_left - easy_attempts_used} attempts remaining to guess the number!")
        easy_level(computer_number)
        print("Guess again..")
        if easy_attempts_used == 10:
            print("You are out of guess.. You lose!!")
            easy_game_on = False
elif game_level == 'hard':
    hard_game_on = True
    while hard_game_on:
        print(f"You have {hard_attempts_left - hard_attempts_used} attempts remaining to guess the number!")
        hard_level(computer_number)
        print("Guess again..")
        if hard_attempts_used == 5:
            print("You are out of guess... You lose!!")
            hard_game_on = False

else:
    print("Pls provide valid game level 'Easy' or 'Hard'..")



