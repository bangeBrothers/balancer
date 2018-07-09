from tkinter import *
root = Tk()
win = Canvas(root, width=400, height=500)
root.resizable(False, False)
win.pack()
l = Label(root, font=("healsd", 10))
l.place(x=5, y=5, anchor=NW)
win.mainloop()