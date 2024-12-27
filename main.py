from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.title("CALCULATOR")
operetor = ""
root.geometry("720x520")
root.resizable(False, False)
root.configure(bg="#17161b")

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm Your Exit")
    if iExit > 0:
        root.destroy()
        return

def scientificclick():
    root.geometry("720x520")
    root.title("Scientific Tool")

def standardclick():
    root.geometry("350x520")
    root.title("Calculator")

def equal():
    global operetor
    try:
        sumup = str(eval(operetor))
        text_Input.set(sumup)
    except:
        text_Input.set("Error")
    operetor = ""

def btnsin():
    global operetor
    try:
        result = str(math.sin(math.radians(float(operetor))))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btncos():
    global operetor
    try:
        result = str(math.cos(math.radians(float(operetor))))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btntan():
    global operetor
    try:
        result = str(math.tan(math.radians(float(operetor))))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btnlog():
    global operetor
    try:
        result = str(math.log10(float(operetor)))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btnln():
    global operetor
    try:
        result = str(math.log(float(operetor)))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btnexp():
    global operetor
    try:
        result = str(math.exp(float(operetor)))
        text_Input.set(result)
    except:
        text_Input.set("Error")
    operetor = ""

def btnpi():
    global operetor
    operetor = str(math.pi)
    text_Input.set(operetor)

def btnClick(value):
    global operetor
    operetor = operetor + str(value)
    text_Input.set(operetor)

def clearbtn():
    global operetor
    operetor = ""
    text_Input.set("")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=iExit)
filemenu.add_command(label="Standard", command=standardclick)
filemenu.add_command(label="Scientific", command=scientificclick)

filemenu_Edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=filemenu_Edit)
filemenu_Edit.add_command(label="Cut")
filemenu_Edit.add_command(label="Paste")
filemenu_Edit.add_command(label="Delete")

filemenu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=filemenu_help)
root.config(menu=menubar)

text_Input = StringVar()
textdisplay = Entry(root, font=("DS-Digital", 20, "bold"), textvariable=text_Input, justify="right", bg="#2b2d32", fg="white", width="22", bd="20").grid(columnspan=6)

# Standard buttons
btn7 = Button(root, padx=20, pady=2, text="7", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(7)).place(x=0, y=80)
btn8 = Button(root, padx=20, pady=2, text="8", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(8)).place(x=90, y=80)
btn9 = Button(root, padx=20, pady=2, text="9", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(9)).place(x=180, y=80)
btnadd = Button(root, padx=15, pady=2, text="+", font=("arial", 25, "bold"), bg="#2b2d32", fg="white", command=lambda: btnClick("+")).place(x=270, y=80)

btn4 = Button(root, padx=20, pady=2, text="4", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(4)).place(x=0, y=150)
btn5 = Button(root, padx=20, pady=2, text="5", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(5)).place(x=90, y=150)
btn6 = Button(root, padx=20, pady=2, text="6", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(6)).place(x=180, y=150)
btnmines = Button(root, padx=19, pady=2, text="-", font=("arial", 25, "bold"), bg="#2b2d32", fg="white", command=lambda: btnClick("-")).place(x=270, y=150)

btn1 = Button(root, padx=20, pady=2, text="1", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(1)).place(x=0, y=220)
btn2 = Button(root, padx=20, pady=2, text="2", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(2)).place(x=90, y=220)
btn3 = Button(root, padx=20, pady=2, text="3", font=("arial", 25, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(3)).place(x=180, y=220)
btngun = Button(root, padx=18, pady=2, text="*", font=("arial", 25, "bold"), bg="#2b2d32", fg="white", command=lambda: btnClick("*")).place(x=270, y=220)

btn0 = Button(root, padx=24, pady=2, text="0", font=("arial", 20, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(0)).place(x=0, y=290)
btndot = Button(root, padx=27, pady=2, text=".", font=("arial", 20, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(".")).place(x=90, y=290)
btn00 = Button(root, padx=15, pady=2, text="00", font=("arial", 20, "bold"), bg="#1e1e1e", fg="white", command=lambda: btnClick(00)).place(x=180, y=290)
btndevide = Button(root, padx=23, pady=2, text="/", font=("arial", 20, "bold"), bg="#2b2d32", fg="white", command=lambda: btnClick("/")).place(x=270, y=290)

btnc = Button(root, padx=145, pady=2, text="C", font=("arial", 25, "bold"), bg="#2b2d32", fg="white", command=clearbtn).place(x=1, y=440)
btnequal = Button(root, padx=148, pady=2, text="=", font=("arial", 25, "bold"), bg="#2b2d32", fg="white", command=equal).place(x=1, y=360)

# Scientific calculator buttons
btnadd = Button(root, width=6, height=2, text="𝝅", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btnpi).place(x=360, y=80)
btnadd = Button(root, width=6, height=2, text="sin", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btnsin).place(x=450, y=80)
btnadd = Button(root, width=6, height=2, text="cos", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btncos).place(x=540, y=80)
btnadd = Button(root, width=6, height=2, text="tan", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btntan).place(x=630, y=80)

btnadd = Button(root, width=6, height=2, text="log", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btnlog).place(x=360, y=155)
btnadd = Button(root, width=6, height=2, text="ln", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btnln).place(x=450, y=155)
btnadd = Button(root, width=6, height=2, text="exp", font=("arial", 15, "bold"), bg="#1e1e1e", fg="white", command=btnexp).place(x=540, y=155)

# Display title for scientific mode
Display = Label(root, text="Scientific Calculator", font=("arial", 25, "bold"), fg="powder blue", bg="#17161b", width=17, height=1, justify=CENTER).place(x=360, y=5)

root.mainloop()
