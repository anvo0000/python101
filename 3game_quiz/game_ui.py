THEME_COLOR = "#375362"
TEXT_FONT = ("Arial", 20, "italic")

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        # Score label on the right
        self.score_lbl = Label(text="Score: 0",bg=THEME_COLOR,fg="White")
        self.score_lbl.grid(row=0, column=1)

        # Question Label span in 2 cols
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280, # allow wrap the text
                                                     text="Question's here",
                                                     font=TEXT_FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons True False
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.checked_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.checked_false)
        self.false_button.grid(row=2, column=1)

        # functions
        self.get_next_question()

        # everything have to go before the window.mainloop()
        self.window.mainloop()

    def checked_true(self):
        print(f"True button clicked")
        is_right = self.quiz.check_answer(user_answer="True")
        self.feedback(is_right)

    def checked_false(self):
        print(f"False button clicked")
        is_right = self.quiz.check_answer(user_answer="False")
        self.feedback(is_right)

    def feedback(self, is_right):
        """If user answer correctly, set background to Green, else set Red.
        After 1000 milliseconds, set background back to White, and call next question"""
        if is_right:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="WHITE")
        self.score_lbl.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_have_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quizzer! ")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")


