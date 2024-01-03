class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        return q
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False