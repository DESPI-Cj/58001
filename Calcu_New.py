from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")


class Calculator():
    def __init__(self, win):
        self.result = Entry()
        self.result.grid(row=0, column=0)

        self.b1 = Button(text="1")
        self.b1.grid(row=1, column=0)
        self.b1.bind('<Button-1>', self.one)

        self.b2 = Button(text="2")
        self.b2.grid(row=1, column=1)
        self.b2.bind('<Button-1>', self.two)

        self.add = Button(text="+")
        self.add.grid(row=1, column=2)
        self.add.bind('<Button-1>', self.addition)

        self.resb = Button(text="=")
        self.resb.grid(row=1, column=3)
        self.resb.bind('<Button-1>', self.resultbutton)

        self.clr = Button(text="clear")
        self.clr.grid(row=1, column=4)
        self.clr.bind('<Button-1>', self.clear)

        self.value = 0
        self.operation = "none"


    def one(self, event):
        self.result.insert(1, "1")

    def two(self, event):
        self.result.insert(1, "2")

    def addition(self, event):
        self.value += int(self.result.get())
        self.result.delete(0, 'end')
        self.operation = "add"
        print(self.value)

    def resultbutton(self, event):
        if self.operation == "add":
            self.value += int(self.result.get())
        self.result.delete(0, END)
        self.result.insert(0, str(self.value))
        print(self.value)


    def clear(self, event):
        self.value = 0
        self.result.delete(0, 'end')


mywin = Calculator(window)
window.mainloop()

