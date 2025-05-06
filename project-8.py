from idlelib.pyshell import use_subprocess

import game_art
import game_database
import random

print(game_art.game_logo)
score=0

account_1= random.choice(game_database.data)
print(account_1)
# account_1_followers = account_1['follower_count']
# print(account_1_followers)


account_2= random.choice(game_database.data)
print(account_2)
# account_2_followers = account_2['follower_count']
# print(account_2_followers)

print(f"Compare 1: {account_1['name']}, a {account_1['description']}, from {account_1['country']}")

print(game_art.vs)

print(f"Compare 2: {account_2['name']}, a {account_2['description']}, from {account_2['country']}")
user_guess=int(input("Who has more followers? Type '1' or '2': "))

if user_guess == 1:
    if account_1['follower_count'] > account_2['follower_count']:
        winner = account_1['name']
        score = score +1
elif user_guess == 2:
    if account_2['follower_count'] > account_1['follower_count']:
        winner = account_2['name']

