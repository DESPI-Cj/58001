from tkinter import *
window = Tk()
window.geometry("700x700")
window.title("Midterm Exam Problem 2")

class GUI:
    def __init__(self, win):
        self.Title = Label(text = "My Full Name")
        self.Title.place(x=310, y=100)

        self.gn = Label(text = "Enter Given Name:")
        self.gn.place(x=100,y=150)
        self.gne = Entry()
        self.gne.place(x=250, y=150)

        self.mn = Label(text="Enter Middle Name:")
        self.mn.place(x=99, y=180)
        self.mne = Entry()
        self.mne.place(x=250, y=180)

        self.ln = Label(text="Enter Last Name:")
        self.ln.place(x=99, y=210)
        self.lne = Entry()
        self.lne.place(x=250, y=210)

        self.fn = Label(text="My Full Name is")
        self.fn.place(x=99, y=250)
        self.fne = Entry(width=30)
        self.fne.place(x=250, y=250)

        self.button = Button(text = "Show Full Name")
        self.button.place(x=200, y=300)
        self.button.bind("<Button-1>", self.display)

    def display(self, display):
        self.fne.delete(0,'end')
        full_name = (str(self.gne.get())+" "+ str(self.mne.get())+" "+ str(self.lne.get()))
        self.fne.insert(END, str(full_name))




mywin = GUI(window)
window.mainloop()