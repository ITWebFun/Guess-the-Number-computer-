from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()


def guess():
    print("smth")


label = Label(text="Try to guess the number!")
label.pack()

input_field = Entry()

check_btn = Button(tk, text="Guess", command=guess)
check_btn.pack()
