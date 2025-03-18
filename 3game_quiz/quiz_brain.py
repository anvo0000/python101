# https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
# https://www.w3schools.com/html/html_entities.asp
# use html.unescape() to remove HTML Entities &gt; &lt;
import html
from question_model import Question

class QuizBrain():
    def __init__(self, question_bank:list):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        self.current_question = Question(None, None)

    def next_question(self):
        self.current_question = self.question_list[self.question_number] # included question_text, question_answer
        question_text = html.unescape(self.current_question.question_text) # use html.unescape() to remove HTML Entities &gt; &lt;
        self.question_number += 1
        q_text = f"Q.{self.question_number}: {question_text}"
        return q_text


    def still_have_questions(self):
        return self.question_number < len(self.question_list)  # short form of True/False
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self,user_answer):
        correct_answer = self.current_question.question_answer
        result = None
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            result = True
        else:
            print("That's wrong!")
            result = False
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}. \n\n")
        return result



