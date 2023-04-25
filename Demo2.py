from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("Grid Manager")

entry00 = Entry(window, bd=2, justify="center")
entry00.grid(row=0,column=0)
entry00.insert(0,"row 0 column 0",)

entry10 = Entry(window, bd=2, justify="center")
entry10.grid(row=0,column=1)
entry10.insert(0,"row 0 column 1",)

entry20 = Entry(window, bd=2, justify="center")
entry20.grid(row=0,column=2)
entry20.insert(0,"row 0 column 2",)

entry01 = Entry(window, bd=2, justify="center")
entry01.grid(row=1,column=0)
entry01.insert(0,"row 1 column 0",)

entry11 = Entry(window, bd=2, justify="center")
entry11.grid(row=1,column=1)
entry11.insert(0,"row 1 column 1",)

entry12 = Entry(window, bd=2, justify="center")
entry12.grid(row=1,column=2)
entry12.insert(0,"row 1 column 2",)

entry20 = Entry(window, bd=2, justify="center")
entry20.grid(row=2,column=0)
entry20.insert(0,"row 2 column 0",)

entry21 = Entry(window, bd=2, justify="center")
entry21.grid(row=2,column=1)
entry21.insert(0,"row 2 column 1",)

entry22 = Entry(window, bd=2, justify="center")
entry22.grid(row=2,column=2)
entry22.insert(0,"row 2 column 2",)

entry20 = Entry(window, bd=2, justify="center")
entry20.grid(row=2,column=0)
entry20.insert(0,"row 2 column 0",)

entry21 = Entry(window, bd=2, justify="center")
entry21.grid(row=2,column=1)
entry21.insert(0,"row 2 column 1",)

entry22 = Entry(window, bd=2, justify="center")
entry22.grid(row=2,column=2)
entry22.insert(0,"row 2 column 2",)

entry30 = Entry(window, bd=2, justify="center")
entry30.grid(row=3,column=0)
entry30.insert(0,"row 3 column 0",)

entry31 = Entry(window, bd=2, justify="center")
entry31.grid(row=3,column=1)
entry31.insert(0,"row 3 column 1",)

entry32 = Entry(window, bd=2, justify="center")
entry32.grid(row=3,column=2)
entry32.insert(0,"row 3 column 2",)
window.mainloop()
