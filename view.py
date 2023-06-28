from tkinter import *
from main import *

tk = Tk()

canvas = Canvas(tk, width=200, height=10)
canvas.pack()

label = Label(text="Try to guess the number!")
label.pack()

input_field = Entry()
input_field.pack()


def answer_check(x):
    label = Label(text=guess(int(x)))
    label.pack()


check_btn = Button(tk, text="Guess", command=lambda: answer_check(input_field.get()))
check_btn.pack()

tk.mainloop()
