from quiz_database import question_bank
from quiz_database import options


print("*************************************")
print("Welcome to My Quiz Game")

score = 0

def check_answer(user_answer, actual_answer):
    if user_answer==actual_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("********************************")
    print(question_bank[question_num]["text"])
    # print(question_num["text"])
    for i in options[question_num]:
        print(i)

    user_input=input("Enter your answer(A/B/C/D....): ").upper()
    correct_answer= question_bank[question_num]["answer"]

    is_correct=check_answer(user_input,correct_answer)

    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        print(f"Correct Answer is : {correct_answer}")
    print(f"Your Current score is {score}/{question_num + 1}")


    # print(correct_answer)
    # if user_input == correct_answer:
    #     print("Correct Answer")
    #     score += 1
    # else:
    #     print("Wrong Answer")
    #     print(f"Correct Answer is : {correct_answer}")
    # print(f"Your Current score is {score}/{question_num + 1}")

print(f"You have given {score} correct answers")
score_percentage=(score/(len(question_bank)) * 100)
print(f"your score is {score_percentage} %")


