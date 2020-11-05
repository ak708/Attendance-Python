from tkinter import *
from PIL import *
#Defining option list
OptionList = [1,2,3,4,5,6,7,8,9]

def studentlist():
    pass

app = Tk()
#Font and orientation setup
app.geometry("900x1200")
variable = StringVar(app)
variable.set(OptionList[0])
opt = OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.grid(row=0,column=1)
#Label
labelTest = Label(text="", font=('Helvetica', 12), fg='red')
labelTest.grid(row=1,column=1)
#Function
def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
variable.trace("w", callback)

#USN
lbl1=Label(app,text="USN NO : ", font=("Helvetica",22))
lbl1.grid(row=2,column=1)
msg1=Message(app,text="",font=("Helvetica",14),bg="lightblue")
msg1.grid(row=2,column=2)
#ROLL NO
lbl1=Label(app,text="ROLL NO : ", font=("Helvetica",22))
lbl1.grid(row=3,column=1)
msg2=Message(app,text="",font=("Helvetica",14))
msg2.grid(row=3,column=2)
#USN
lbl1=Label(app,text="NAME : ", font=("Helvetica",22))
lbl1.grid(row=4,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=4,column=2)
#DOB
lbl1=Label(app,text="DOB : ", font=("Helvetica",22))
lbl1.grid(row=5,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=5,column=2)
#GENDER
lbl1=Label(app,text="GENDER : ", font=("Helvetica",22))
lbl1.grid(row=6,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=6,column=2)

lbl1=Label(app,text="ADDRESS : ", font=("Helvetica",22))
lbl1.grid(row=7,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=7,column=2)

lbl1=Label(app,text="FATHER'S NAME : ", font=("Helvetica",22))
lbl1.grid(row=8,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=8,column=2)

lbl1=Label(app,text="MOTHER'S NAME : ", font=("Helvetica",22))
lbl1.grid(row=9,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=9,column=2)

lbl1=Label(app,text="PHONE NUMBER : ", font=("Helvetica",22))
lbl1.grid(row=10,column=1)
msg1=Message(app,text="",font=("Helvetica",14))
msg1.grid(row=10,column=2)

lblimg=Label(image=)

app.mainloop()
