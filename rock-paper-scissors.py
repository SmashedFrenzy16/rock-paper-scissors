from tkinter import *
import random

root = Tk()

listofoutcomes = ["Computer: Rock", "Computer: Paper", "Computer: Scissors"]

choice = random.choice(listofoutcomes)


def execute1():
    label = Label(root, text="You: Rock |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)


def execute2():
    label = Label(root, text="You: Paper |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)


def execute3():
    label = Label(root, text="You: Scissors |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)

button1 = Button(root, text="Rock", command=execute1)
button2 = Button(root, text="Paper", command=execute2)
button3 = Button(root, text="Scissors", command=execute3)

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)


root.mainloop()
