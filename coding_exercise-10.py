### This Program will calculate Love calculator
name_1=input("Enter Name-1: ")
name_2=input("Enter Name-2: ")

names=name_1+name_2
names=names.lower()
#TREU LOVE

t=names.count("t")
r=names.count("r")
u=names.count("u")
e=names.count("e")

true=t + r + u + e

l=names.count("l")
o=names.count("o")
v=names.count("v")
e=names.count("e")

love= l + o + v + e

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} and you go together like code and mentos")
elif ( love_score >= 40 ) and ( love_score <= 50 ):
    print(f"Your score is {love_score} and you are alright together")
else:
    print(f"your score is {love_score}")