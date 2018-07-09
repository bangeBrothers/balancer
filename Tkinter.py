from tkinter import *
root = Tk()
win = Canvas(root, width=400, height=500)
root.resizable(False, False)
win.pack()
program_name = Label(root, text='EXPANSE; BALANCER')
program_name.place(x=200, y=10, anchor=N)
program_name.config(font=('Courier', 20))
win.mainloop()