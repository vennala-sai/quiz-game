from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict in question_data:
    question_bank.append(Question(dict["text"], dict["answer"]))

quiz_controller = QuizBrain(question_bank)

score = 0
total_asked = 0

while quiz_controller.still_has_questions():
    new_q = quiz_controller.next_question()

    answer = input(f"Q{quiz_controller.question_number} {new_q.text} (True or False)?: ").capitalize()
    if answer == new_q.answer:
        print("You got it right!!!")
        score += 1
        print(f"Current score: {score}\n")
    elif answer == "Exit" or answer == "End" or answer == "Break":
        break
    else:
        print("You got it wrong! :(")
        print(f"Current score: {score}\n")
print(f"Total score is {(score/quiz_controller.question_number) * 100}%. That is {score}/{quiz_controller.question_number} questions asked.")
print("-----Game Over-----\n")