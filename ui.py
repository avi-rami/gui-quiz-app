THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain:THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        # score label
        self.score_label = Label(text="Score: ",bg=THEME_COLOR)
        self.score_label.config(fg="white")
        self.score_label.grid(row=0,column=1)

        # questions
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Trivia Game", font=("Arial", 20, "italic"),width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=60)

        # True/False buttons
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image= self.true_img,command=self.answer_true,highlightthickness=0, highlightcolor=THEME_COLOR, borderwidth=0)
        self.false_button = Button(image= self.false_img,command=self.answer_false,highlightthickness=0, highlightcolor=THEME_COLOR, borderwidth=0)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        current_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=current_question)

    def answer_true(self):
        self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback()

    def answer_false(self):
        self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback()



    def give_feedback(self):
        if self.quiz.scored is False:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")

        if self.quiz.still_has_questions():
            self.window.after(1000,self.get_next_question)
        else:
            self.window.after(1000, self.quiz_complete)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def quiz_complete(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=f"You've reached the end!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}") QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        # score label
        self.score_label = Label(text="Score: ",bg=THEME_COLOR)
        self.score_label.config(fg="white")
        self.score_label.grid(row=0,column=1)

        # questions
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Trivia Game", font=("Arial", 20, "italic"),width=280, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=60)

        # True/False buttons
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image= self.true_img,command=self.answer_true,highlightthickness=0, highlightcolor=THEME_COLOR, borderwidth=0)
        self.false_button = Button(image= self.false_img,command=self.answer_false,highlightthickness=0, highlightcolor=THEME_COLOR, borderwidth=0)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        current_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=current_question)

    def answer_true(self):
        self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback()

    def answer_false(self):
        self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.give_feedback()



    def give_feedback(self):
        if self.quiz.scored is False:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")

        if self.quiz.still_has_questions():
            self.window.after(1000,self.get_next_question)
        else:
            self.window.after(1000, self.quiz_complete)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def quiz_complete(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=f"You've reached the end!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

