from tkinter import *
import DOB
import sys
import verification
#-----------------------------------------------------------------------
window = Tk()
window.title("ATTENDANCE WINDOW - STUDENT DATABASE SYSTEM")
# window.attributes('-fullscreen','True')
window.geometry('720x500')
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (720/2)
y = (hs/2) - (500/2)
window.geometry('%dx%d+%d+%d' % (720, 500, x, y))
window.configure(bg="lavender")
#-----------------------------------------------------------------------
message = Label(window, text="ATTENDANCE MANAGEMENT SYSTEM",bg="lavender",font=('Bahnschrift', 30,"bold","underline")).pack()

message1 = Label(window, text="FACIAL RECOGNITION",bg="lavender",font=('Bahnschrift SemiBold', 25))
message1.place(x=200, y=100)
cap =Button(window, text="RECOGNISE FOR ATTENDANCE",bg="pale green"  ,fg="black"  ,width=30  ,height=2, activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 13,"bold"))
cap.place(x=225, y=175)
#---------------------------------------------------
message2 = Label(window, text="MANUAL ATTENDANCE",bg="lavender",font=('Bahnschrift SemiBold', 25))
message2.place(x=200, y=300)

lbl6 =Label(window, text="USN No :",bg="lavender",font=('Bahnschrift', 20))
lbl6.place(x=150, y=375)
txt6=Entry(window,width=10,font=('Bahnschrift Light', 20))
txt6.place(x=270, y=375)

cap =Button(window, text="MARK ATTENDANCE",command=verification.verification,bg="pale green",fg="black",activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 13,"bold"))
cap.place(x=445, y=375)
#--------------------------------------------------
db =Button(window, text="SHOW DATABASE",width=75,bg="tomato",fg="white",activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 13,"bold"))
db.place(x=20, y=450)
#--------------------------------------------------
mainloop()
window.mainloop()

def collect_attendance():
    col1=[txt6]
    return col1