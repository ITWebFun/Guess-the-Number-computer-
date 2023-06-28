from tkinter import *
from controller import *

tk = Tk()

canvas = Canvas(tk, width=200, height=10)
canvas.pack()

rule_label = Label(text="Try to guess the number between 1 and 15!")
rule_label.pack()

input_field = Entry()
input_field.pack()

def answer_check(x):
    answer_label['text'] = guess(int(x))

check_btn = Button(tk, text="Guess", command=lambda: answer_check(input_field.get()))
check_btn.pack()

answer_label = Label(text='')
answer_label.pack()

tk.mainloop()
