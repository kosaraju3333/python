### Hangman Game
import random
print("Let's Play Hangman Game")
print("Guess the FRUIT name")
print("You have only 6 lives so try to guess the word within 6 attempts! Good Luck !!")
computer_fruits=["APPLE", "Banana", "Watermelon", "Orange", "Grapes", "Mango", "Guava", "Pineapple", "Kiwi", "Pear", "Pumpkin", "Papaya", "Plum"]

fruit_list=list(random.choice(computer_fruits).lower())

fruit_dummy=[]
for i in fruit_list:
    fruit_dummy.append(i)

user_array =[]
for i in range(len(fruit_list)):
    user_array.append("_")
print(user_array)

life_count=0
while True:
    for i in range(0,len(fruit_list)):
        char=input("Guess a letter: ")
        if char in fruit_dummy:
            ### Find the index of char in fruit array
            fruit_dummy_index = fruit_dummy.index(char)
            user_array[fruit_dummy_index]=char
            fruit_dummy[fruit_dummy_index]="ZERO"
            print(user_array)

            if user_array == fruit_list:
                print("You WIN")
                exit()
        else:
            print(f"You guessed {char} is not present in the word. So you lose a life")
            print(user_array)
            life_count=life_count+1
            if  life_count == 1:
                print(f"life's left: 5")
                print("""
                +_______+
                |       |
                O       |                
                |       | 
                        |        
                        |       
                        |        
             ===========|""")

            elif life_count == 2:
                print(f"life's left: 4")
                print("""
                +_______+
                |       |
                O       |                
               /|       | 
                        |        
                        |       
                        |        
             ===========|""")
            elif life_count == 3:
                print(f"life's left: 3")

                print("""
                +_______+
                |       |
                O       |                
               /|\\     | 
                        |        
                        |       
                        |        
             ===========|""")
            elif life_count == 4:
                print(f"life's left: 2")
                print("""
                +_______+
                |       |
                O       |                
               /|\\     | 
                |       | 
                        |       
                        |        
             ===========|""")
            elif life_count == 5:
                print(f"life's left: 1")
                print("""
                +_______+
                |       |
                O       |                
               /|\\     | 
                |       |        
               /        |       
                        |        
             ===========|""")
            else:
                print(f"life's left: 0")
                print(f"You LOSE the game")
                print("""
                +_______+
                |       |
                O       |                
               /|\\     | 
                |       |        
               / \\     |       
                        |        
             ===========|""")
                fruit_str=""
                for var in fruit_list:
                    fruit_str=fruit_str+var
                print(f"Answer is: {fruit_str}")
                exit()


