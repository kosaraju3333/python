print("*************************************")
print("Welcome to My Quiz Game")

question_bank=[
    {"text": "The ability of one class to acquire methods and attributes of another class is called ___.", "answer": "A"},
    {"text": "Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "What is the depth of multilevel inheritance in python?", "answer": "C"},
    {"text": "What does MRO stands for?", "answer": "B"}
]

options = [["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
           ["A. Single", "B. Double", "C. Multiple", "D. both A and B"],
           ["A. Multiple Inheritance", "B. MultiLevel Inheritance", "C. Hierarchical inheritance", "D. None of these"],
           ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
           ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order",
            "D. Method Resolution Object"]
           ]

score = 0

def check_answer(user_input,correct_answer):
    if user_input==correct_answer:
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


