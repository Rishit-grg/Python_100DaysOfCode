from data import *
from quiz_brain import *

#  list of questionformat object
question_bank = []
for i in question_data:
    add_ques = QuestionFormat(i["text"], i["answer"])
    question_bank.append(add_ques)

quiz = QuizBrain(question_bank)
# prompt the user
while not quiz.quit():
    u_input = input(quiz.ask_new())
    print(quiz.check_ans(u_input))

print("Quiz over")
print (quiz.score_out())