from tkinter import *
from controller import *

tk = Tk()

canvas = Canvas(tk, width=200, height=10)
canvas.pack()

label = Label(text="Try to guess the number between 1 and 15!")
label.pack()

input_field = Entry()
input_field.pack()


def answer_check(x):
    label = Label(text=guess(int(x)))
    label.pack()


check_btn = Button(tk, text="Guess", command=lambda: answer_check(input_field.get()))
check_btn.pack()

tk.mainloop()
