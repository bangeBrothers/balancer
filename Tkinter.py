from tkinter import *
root = Tk()
win = Canvas(root, width=400, height=500)
root.resizable(False, False)
win.pack()


def Button_Function():
    print("fuckgot")


Butt = Button(root, text="Make a fuckgot", command=Button_Function)
Butt.pack()

win.mainloop()