from tkinter import *
from quiz_brain import QuizBrain, check_answer


THEME_COLOR = "#375362"
WIDTH = 480
HEIGHT = 360

scores = QuizBrain()
scores.check_answer(0, 0)


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, width=WIDTH, height=HEIGHT)
        self.window.title("Trivia Game")
        self.lbl_score = Label(
            text=f"Score: {scores}", bg=THEME_COLOR, fg="white", font=("Arial 20"))
        self.lbl_score.grid(column=1, row=0, columnspan=2)
        self.lbl_text = Label(text="")
        self.window.mainloop()
