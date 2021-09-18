from tkinter import *

def bt1_Click():
 x=int(et_weight.get())
 y=int(et_height.get())
 y=y/100
 z=float(x/(y*y))
 t_BMI.set(f'{z:.4f}')
 bt2_Click(z)

def bt2_Click(c):
    if c<18.7:
     t_Status.set(f'Underweight')
     lb8 = Label(root, text='', textvariable=t_Status,bg='white').grid(row=8,column=2,padx=(0,65))
    elif c<24.9:
     t_Status.set(f'Normal')
     lb8 = Label(root, text='', textvariable=t_Status,bg='green').grid(row=8,column=2,padx=(0,65))
    elif c<29.9:
     t_Status.set(f'Overweight')
     lb8 = Label(root, text='', textvariable=t_Status,bg='yellow').grid(row=8,column=2,padx=(0,65))
    else :
     t_Status.set(f'Obese')
     lb8 = Label(root, text='', textvariable=t_Status,bg='red').grid(row=8,column=2,padx=(0,65))
     
root = Tk()
root.geometry('280x350')
root.resizable(False, False)
root.title('Body-Mass Index(BMI)')
root.option_add('*font','Calibri 16')
root.configure(bg = 'lightblue')
et_weight = StringVar()
et_height = StringVar()
t_BMI = StringVar()
t_Status = StringVar()

lb1 = Label(root, text='Weight',bg = 'lightblue').grid(row=1, column=1,padx=(0,10))
lb2 = Label(root, text='Height',bg = 'lightblue').grid(row=2, column=1,padx=(0,10))
lb3 = Label(root, text='',bg = 'lightblue').grid(row=0, column=0)
et1 = Entry(root, textvariable=et_weight, width=9).grid(row=1, column=2,padx=(0,60))
et2 = Entry(root, textvariable=et_height, width=9).grid(row=2, column=2,padx=(0,60))
lb3 = Label(root, text='',bg = 'lightblue').grid(row=3, column=0)
btn1 = Button(root, text='คำนวณค่า', command=bt1_Click).grid(row=4,column=1,columnspan=2,padx=(0,20))
lb3 = Label(root, text='',bg = 'lightblue').grid(row=5, column=0)
lb4 = Label(root, text='ผลการคำนวณ',bg = 'lightblue').grid(row=6, column=1)
lb5 = Label(root, text='BMI      =',bg = 'lightblue').grid(row=7, column=1)
lb6 = Label(root, text='Status   =',bg = 'lightblue').grid(row=8, column=1)
lb7 = Label(root, text='', textvariable=t_BMI,bg = 'lightblue').grid(row=7,column=2,padx=(0,65))
lb8 = Label(root, text='', textvariable=t_Status,bg = 'lightblue').grid(row=8,column=2,padx=(0,65))

t_BMI.set("n/a")
t_Status.set("n/a")

root.mainloop()