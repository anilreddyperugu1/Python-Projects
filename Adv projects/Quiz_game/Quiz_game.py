import python_quiz_questions
from Practice.Functions.Quiz_game.python_quiz_questions import questions, answers

print("""***********************************\nWelcome to the quiz game\n***********************************""")

score = 0
def check_answer(guess,answer):
    if guess == answer:
        return True
    else:
        return False


for i in range(len(python_quiz_questions.questions)):
    print(questions[i]["text"])
    for j in answers[i]:
        print(j)

    guess = input("Enter your option: ").upper()
    is_correct = check_answer(guess, questions[i]["answer"])
    if is_correct:
        print("Correct answer")
        score += 1
        print(f"score = {score}")
    else:
        print("Wrong answer")
        print(f"The correct answer is {questions[i]["answer"]}")


print(f"Your have got {score} score")
print(f"Total percentage = {(score/len(questions))*100}%")




