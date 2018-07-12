from tkinter import *
root = Tk()

# Config for window properties
windowName = "Meridian Balancer"
windowIcon = "icon.ico"
# Config for main menu properties
menuWidth = 400
menuHeight = 400

# Config for main menu header properties
menuHeader = "EXPANSE BALANCER"
programVersion = "0.1"

# Config for main menu context properties

# Define main menu canvas height and width, as well as icon and title
win = Canvas(root, width=menuWidth, height=menuHeight, bg='white')
root.resizable(False, False)
root.title(windowName)
root.iconbitmap(windowIcon)
win.pack()

# Build main menu header
program_name = Label(root, text='EXPANSE BALANCER', font=('Courier', 20), bg='white')
program_name.place(x=200, y=10, anchor=N)
version_text = Label(root, text=('Version', programVersion), font=('Courier', 10), bg='white')
version_text.place(x=200, y=40, anchor=N)

# Define functions of context menu buttons? @galv
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


# Define program functions
def Kill_Main():
    print("funk")


def Revive_Main():
    print("FunY")

# Build main menu context labels
##ship_context_label = Label(root, text=('SHIPS', programVersion), font=('Courier', 18), bg='white')
##ship_context_label(x=100, y=100, anchor=N)

# Build main menu context buttons

## Build view ship button
view_ship_button = Button(root, width=25, height=1, text='VIEW', command=View_Ships)
view_ship_button.place(x=275, y=115, anchor=CENTER)

## Build add ship button
add_ship_button = Button(root, width=25, height=1, text='ADD', command=Add_Ships)
add_ship_button.place(x=275, y=155, anchor=CENTER)

## Build view weapons button
view_weapons_button = Button(root, width=25, height=1, text='VIEW', command=View_Weapons)
view_weapons_button.place(x=275, y=195, anchor=CENTER)

## Build add weapons button
add_weapons_button = Button(root, width=25, height=1, text='ADD', command=Add_Weapons)
add_weapons_button.place(x=275, y=235, anchor=CENTER)

# Basically runs the code
win.mainloop()
