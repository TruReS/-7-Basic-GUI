from tkinter import *

eps = ""

def press(num):
    global eps
    eps = eps + str(num)
    equ.set(eps)

def equalpress():
    try:
        global eps
        total = str(eval(eps))
        equ.set(total)
        eps = total
 
    except:
        equ.set("Error")
        eps = ""

def clear():
    global eps
    eps = ""
    equ.set("0")
 
cal = Tk()
cal.title("Calculator")
cal.option_add('*font','Calibri 15')
cal.geometry('240x268')
cal.configure(bg = 'black')
cal.resizable(False,False)
equ = StringVar()

et = Entry(cal,textvariable=equ,width=22,borderwidth=10,justify = RIGHT).grid(row=0, column=0,columnspan=4)
button0 = Button(cal, text=' 0 ',width=11,command=lambda: press(0)).grid(row=5, column=0,columnspan=2)
button1 = Button(cal, text=' 1 ',width=5,command=lambda: press(1)).grid(row=4, column=0)
button2 = Button(cal, text=' 2 ',width=5,command=lambda: press(2)).grid(row=4, column=1)
button3 = Button(cal, text=' 3 ',width=5,command=lambda: press(3)).grid(row=4, column=2)
button4 = Button(cal, text=' 4 ',width=5,command=lambda: press(4)).grid(row=3, column=0)
button5 = Button(cal, text=' 5 ',width=5,command=lambda: press(5)).grid(row=3, column=1)
button6 = Button(cal, text=' 6 ',width=5,command=lambda: press(6)).grid(row=3, column=2)
button7 = Button(cal, text=' 7 ',width=5,command=lambda: press(7)).grid(row=2, column=0)
button8 = Button(cal, text=' 8 ',width=5,command=lambda: press(8)).grid(row=2, column=1)
button9 = Button(cal, text=' 9 ',width=5,command=lambda: press(9)).grid(row=2, column=2)

plus = Button(cal, text=' + ',width=5,height=3,command=lambda: press("+"),bg = 'khaki').grid(row=2, column=3,rowspan=2)
minus = Button(cal, text=' - ',width=5,command=lambda: press("-"),bg = 'purple').grid(row=1, column=3)
multiply = Button(cal, text=' * ',width=5,command=lambda: press("*"),bg = 'blue').grid(row=1, column=2)
divide = Button(cal, text=' / ',width=5,command=lambda: press("/"),bg = 'lightblue').grid(row=1, column=1)
equal = Button(cal, text=' EN ',width=5,height=3, command=equalpress,bg = 'lightgreen').grid(row=4, column=3,rowspan=2)
clear = Button(cal, text='clr',width=5,command=clear,bg = 'orange').grid(row=1, column=0)
decimal= Button(cal, text='.',width=5,command=lambda: press('.')).grid(row=5, column=2)

equ.set("0")
cal.mainloop()