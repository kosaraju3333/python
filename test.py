name = input("Enter Your Name it should be 5 letter name only:")
def name_game():
    if len(name) > 4: 
        count = 0
        score = 0
        chances = 5
        while (count <= 4):
            char = input("Enter any char to check it is in your name or not: ")
            if char in name:
                print(f"{char} char is presented in your name")
                score = score + 1
            else:
                print(f"{char} char is not presented in your name")
            count = count + 1
            chances = chances - 1
            print(f"You have {chances} more chances only...")
        print(f"Your Score is : {score}")
    else:
        print("Name length is more than 5. It should be equal or less than 5")


if __name__=="__main__":
    name_game()
