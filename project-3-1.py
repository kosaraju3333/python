import random
print("Let's Play Hangman Game")
print("Guess the FRUIT name")
print("You have only 6 lives so try to guess the word within 6 attempts! Good Luck !!")
words_list=["APPLE", "Banana"]
chosen_word=random.choice(words_list).lower()
print(chosen_word)
display_word=[]
for i in range(0,len(chosen_word)):
    #display_word+='_'
    display_word.append("_")
print(display_word)
lives=6
game_over=False
while not game_over:
    guessed_letter=input("Enter the Guess Letter: ").lower()
    for position in range(0,len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display_word[position] = guessed_letter
    print(display_word)
    if guessed_letter not in chosen_word:
        lives = lives -1
        if lives == 0:
            game_over = True
            print("You Lose...!!!")
    if '_' not in display_word:
        game_over = True
        print("You WIN")

