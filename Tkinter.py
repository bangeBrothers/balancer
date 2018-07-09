from tkinter import *
root = Tk()
win = Canvas(root, width=400, height=500, bg='white')
root.resizable(False, False)
win.pack()
program_name = Label(root, text='EXPANSE BALANCER', font=('Courier', 20), bg='white')
program_name.place(x=200, y=10, anchor=N)
version_text = Label(root, text='Version 0.1', font=('Courier', 10), bg='white')
version_text.place(x=200, y=40, anchor=N)


def View_Ships():
    vsroot = Tk()
    vswin = Canvas(vsroot, width=600, height=300, bg='white')


def Add_Ships():
    asroot = Tk()
    aswin = Canvas(asroot, width=600, height=300, bg='white')


def View_Weapons():
    vwroot = Tk()
    vwwin = Canvas(vwroot, width=600, height=300, bg='white')


def Add_Weapons():
    awroot = Tk()
    awwin = Canvas(awroot, width=600, height=300, bg='white')


view_ship_button = Button(root, width=10, height=1, text='VIEW', command=View_Ships)
view_ship_button.place(x=275, y=115, anchor=CENTER)

def Kill_Main():
    print("funk")

def Revive_Main():
    print("FunY")


win.mainloop()
