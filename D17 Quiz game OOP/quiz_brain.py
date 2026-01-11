class QuestionFormat :
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class QuizBrain :
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def ask_new(self):
        current_ques = self.question_list[self.question_num]
        return f"Q. {current_ques.prompt}"


    def check_ans(self,u_input):
        current_ques = self.question_list[self.question_num]
        self.question_num += 1
        if u_input.lower().strip() == current_ques.answer.lower().strip():
            self.score +=1
            return "CORRECT!!!"
        else:
            return "WRONG"
    def quit(self):
        return self.question_num >= len(self.question_list)

    def score_out(self):
        return f"You got {self.score} out of {len(self.question_list)} correct."