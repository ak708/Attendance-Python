from tkinter import *
import DOB

window = Tk()
window.title("EDIT WINDOW - STUDENT DATABASE SYSTEM")
# window.attributes('-fullscreen','True')
window.geometry('1280x720')
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (1280/2)
y = (hs/2) - (720/2)
window.geometry('%dx%d+%d+%d' % (1280, 720, x, y))
window.configure()
#---------------------------------------------------
message = Label(window, text="STUDENT DATABASE SYSTEM",font=('Bahnschrift', 34, 'bold underline'))
message.place(x=350, y=20)
#---------------------------------------------------
lbl = Label(window, text="USN No :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl.place(x=10, y=100)
txt=Entry(window,width=30 ,font=('Bahnschrift Light', 20))
txt.place(x=140, y=100)

lbl1 = Label(window, text="Roll No :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl1.place(x=10, y=200)
txt1=Entry(window,width=30 ,font=('Bahnschrift Light', 20))
txt1.place(x=140, y=200)

lbl2 =Label(window, text="Name :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl2.place(x=10, y=300)
txt2 =Entry(window,width=30,font=('Bahnschrift Light', 20))
txt2.place(x=140, y=300)

lbl3 =Label(window, text="DOB :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl3.place(x=10, y=400)
cal = Button(window, text="Calender",command=DOB.cal, bg="azure",activebackground = "Red" ,font=('Bahnschrift SemiBold', 18,"bold"))
cal.place(x=140, y=400)

var=IntVar()
lbl4 =Label(window, text="Gender :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl4.place(x=10, y=500)
male = Radiobutton(window, text="Male", variable=var, value="Male",  font=('Bahnschrift SemiBold', 20,"bold"))
male.place(x=140, y=500)
female = Radiobutton(window, text="Female", variable=var, value="Female",  font=('Bahnschrift SemiBold', 20,"bold"))
female.place(x=300, y=500)

lbl5 =Label(window, text="Residential\nAddress :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl5.place(x=620, y=100)
txt5=Entry(window,width=30,font=('Bahnschrift Light', 20))
txt5.place(x=780, y=100)
# message =Label(window, text="" ,bg="white"  ,fg="black"  ,width=41  ,height=5, activebackground = "white" ,font=('Bahnschrift', 15))
# message.place(x=780, y=137)

lbl6 =Label(window, text="Father\'s\nName :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl6.place(x=620, y=190)
txt6=Entry(window,width=30,font=('Bahnschrift Light', 20))
txt6.place(x=780, y=210)

lbl6 =Label(window, text="Mother\'s\nName :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl6.place(x=620, y=290)
txt6=Entry(window,width=30,font=('Bahnschrift Light', 20))
txt6.place(x=780, y=310)

lbl7 =Label(window, text="Parent\nPh.No :",font=('Bahnschrift SemiBold', 20,"bold"))
lbl7.place(x=620, y=400)
txt7=Entry(window,width=30,font=('Bahnschrift Light', 20))
txt7.place(x=780, y=400)

lbl8 =Label(window, text="Status : ",font=('Bahnschrift SemiBold', 20,"bold"))
lbl8.place(x=620, y=500)
message =Label(window, text="" ,bg="white",fg="black",width=41,height=2,activebackground = "white" ,font=('Bahnschrift', 15))
message.place(x=780, y=500)

clear =Button(window, text="CLEAR INPUT",font=('Bahnschrift SemiBold', 13,"bold"))
clear.place(x=770, y=610)
add =Button(window, text="SAVE CHANGES",bg="cyan"  ,fg="black"  ,width=30  ,height=2, activebackground = "Red" ,font=('Bahnschrift SemiBold', 13,"bold"))
add.place(x=920, y=600)

mainloop()
window.mainloop()
