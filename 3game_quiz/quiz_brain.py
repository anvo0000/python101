class QuizBrain():
    def __init__(self, question_bank:list):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        question_text = self.question_list[self.question_number].question_text
        answer_text = self.question_list[self.question_number].question_answer

        self.question_number += 1
        user_answer_text = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer=user_answer_text, correct_answer=answer_text)

    def still_have_questions(self):
        return self.question_number < len(self.question_list)  # short form of True/False
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self,user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}. \n\n")



