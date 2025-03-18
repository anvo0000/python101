from question_model import Question
from quiz_brain import QuizBrain
import data
from game_ui import QuizInterface
question_bank = []

question_data = data.question_data
for item in question_data:
    new_question = Question(text=item["question"], answer=item["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank=question_bank)
quiz_ui = QuizInterface(quiz_brain)

# while quiz_brain.still_have_questions():
#     quiz_brain.next_question()
#     if not quiz_brain.still_have_questions():
#         print(f"You've completed the quiz.")
#         print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
#         break
