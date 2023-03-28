from tkinter import*
window = Tk()
window.geometry("1000x500+10+10")
window.title("My first GUI")

btn1 = Button(text="Yamete!", fg="blue", bg=("red"))
btn1.place(x=500, y=250)
txtfld = Entry(window, border=1)
txtfld.place(x=200, y=100)

window.mainloop()
