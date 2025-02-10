from question_model import Question
# from data import question_data
from data import Data
from quiz_brain import QuizBrain

question_bank = []
# for item in question_data:
#     new_question = Question(text=item["text"], answer=item["answer"])
#     question_bank.append(new_question)


_data = Data(url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
question_data = _data.crawl_opentdb()

for item in question_data:
    new_question = Question(text=item["text"], answer=item["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank=question_bank)
while quiz_brain.still_have_questions():
    quiz_brain.next_question()
    if not quiz_brain.still_have_questions():
        print(f"You've completed the quiz.")
        print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
        break
