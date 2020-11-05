from tkinter import *
import DOB
import camera
import sqlite3 as sql
import DOB
import add_gui
import attendance_gui as att
import dropdownmenu as dpm
import Login_window as linw
import verification as veri
import edit_gui
from draganddrop import *
import drdppathlink as drdp
import sys, os
'''from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap'''
import csv
import sqlite3
import browse
addwindow = Tk()
addwindow.title("ADD WINDOW - STUDENT DATABASE SYSTEM")
# window.attributes('-fullscreen','True')
addwindow.geometry('1280x720')
ws = addwindow.winfo_screenwidth()
hs = addwindow.winfo_screenheight()
x = (ws/2) - (1280/2)
y = (hs/2) - (720/2)
addwindow.geometry('%dx%d+%d+%d' % (1280, 720, x, y))
addwindow.configure(bg="lavender")
#--------------------------------------------------
def picdir():
    imagedir=browse.open_pic()
    return imagedir
#----------------------------------------------
def add_sql():
    def check_db():
        conn1=lite.connect("facerec.db")
        cursor=conn1.cursor()
        stmt = "SHOW TABLES LIKE 'attendance'"
        cursor.execute(stmt)
        result = cursor.fetchone()
        if result:
            # there is a table named "students"
            conn1.commit()
            conn1.close()
        else:
            # there are no tables named "student"
            cursor.execute("""create table student
                    usn char(6) primary key,
                    roll_no numeric(6),
                    name varchar(30),
                    dob date,
                    gender varchar(6),
                    address varchar(200),
                    fathers_name varchar(30),
                    mothers_name varchar(30),
                    phone_no char(10),
                    image blob;
                    """)
            conn1.commit()
            conn1.close()
    check_db()


    #getting data from add_gui.py
    usn=txt.get()
    roll_no=txt1.get()
    name=txt2.get()
    dob=cal.get()
    male=male.get()
    female=female.get()
    address=txt5.get()
    fathers_name=txt6.get()
    phone_no=txt7.get()

    imgdir=picdir()
    '''app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())'''

    #establishing connection
    conn= lite.connect("facerec.db")
    cursor = conn.cursor()


    #getting attendance time
    '''timedis=dt.datetime.now()
    tstr=timedis.strftime("%H:%M:%S")
    dstr=timedis.strftime("%d/%m/%Y")'''
    #getting gender
    if int(male)==1 and int(female)==0:
        gender="male"
    elif int(male)==0 and int(female)==1:
        gender="female"
    #inserting entered data
    #"""cursor.execute("INSERT into attendance values(:usn,:roll_no,:name,:dob,:gender,:address,:f_name,:phone_no,:image)
    #        {
    #                    "usn":usn,
    #                    "roll_no":roll_no,
    #                    "name":name,
    #                    "dob":dob,
    #                    "gender":gender,
    #                    "address":address,
    #                    "f_name":f_name,
    #                    "phone_no":ph_no,
    #                "image":imgdir,
    #            }
    #            ")"""
    cursor.execute("insert into students values(''"+usn+"','"+roll_no+"','"+name+"','"+dob+"','"+male+"','"+female+"','"+address+"','"+fathers_name+"','"+phone_no+"','"+imgdir+");")
    #clearing input boxes
    txt.delete(0, END)
    txt1.delete(0, END)
    txt2.delete(0, END)
    cal.delete(0, END)
    male.delete(0, END)
    female.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    conn.commit()
    conn.close()

#----------------------------------------------------
message = Label(addwindow, text="STUDENT DATABASE SYSTEM",bg="lavender",font=('Bahnschrift', 34, 'bold underline'))
message.place(x=350, y=20)

#usn
lbl = Label(addwindow, text="USN No :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl.place(x=10, y=100)
txt=Entry(addwindow,width=30 ,font=('Bahnschrift Light', 20))
txt.place(x=140, y=100)

#roll no
lbl1 = Label(addwindow, text="Roll No :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl1.place(x=10, y=200)
txt1=Entry(addwindow,width=30 ,font=('Bahnschrift Light', 20))
txt1.place(x=140, y=200)

#name
lbl2 =Label(addwindow, text="Name :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl2.place(x=10, y=300)
txt2 =Entry(addwindow,width=30,font=('Bahnschrift Light', 20))
txt2.place(x=140, y=300)

#DOB
lbl3 =Label(addwindow, text="DOB :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl3.place(x=10, y=400)
cal = Button(addwindow, text="Calendar",command=DOB.cal, bg="white",activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 18,"bold"))
cal.place(x=140, y=400)

#gender radiobuttons
var=IntVar()
lbl4 =Label(addwindow, text="Gender :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl4.place(x=10, y=500)

male = Radiobutton(addwindow, text="Male",bg="lavender",activebackground = "slate gray", variable=var, value="Male",  font=('Bahnschrift SemiBold', 20,"bold"))
male.place(x=140, y=500)

female = Radiobutton(addwindow, text="Female",bg="lavender",activebackground = "slate gray", variable=var, value="Female",  font=('Bahnschrift SemiBold', 20,"bold"))
female.place(x=300, y=500)

#address
lbl5 =Label(addwindow, text="Residential\nAddress :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl5.place(x=620, y=100)
txt5=Entry(addwindow,width=30,font=('Bahnschrift Light', 20))
txt5.place(x=780, y=100)

#father's name
lbl6 =Label(addwindow, text="Father\'s\nName :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl6.place(x=620, y=200)
txt6=Entry(addwindow,width=30,font=('Bahnschrift Light', 20))
txt6.place(x=780, y=200)

#mothers name
lbl6 =Label(addwindow, text="Mother\'s\nName :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl6.place(x=620, y=200)
txt6=Entry(addwindow,width=30,font=('Bahnschrift Light', 20))
txt6.place(x=780, y=200)


#phone no
lbl7 =Label(addwindow, text="Parent\nPh.No :",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl7.place(x=620, y=300)
txt7=Entry(addwindow,width=30,font=('Bahnschrift Light', 20))
txt7.place(x=780, y=300)

#status
lbl8 =Label(addwindow, text="Status : ",bg="lavender",font=('Bahnschrift SemiBold', 20,"bold"))
lbl8.place(x=620, y=400)
message1 =Label(addwindow, text="" ,bg="white",fg="black",width=41,height=2,activebackground = "white" ,font=('Bahnschrift', 15))
message1.place(x=780, y=400)

#clear
clear =Button(addwindow, text="CLEAR INPUT",font=('Bahnschrift SemiBold', 13,"bold"))
clear.place(x=620, y=500)

#capture image
cap =Button(addwindow, text="SELECT IMAGE",bg="cyan"  ,fg="black"  ,width=30  ,height=2, activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 13,"bold"),command=picdir())
cap.place(x=120, y=600)
'''train =Button(addwindow, text="TRAIN IMAGES",bg="cyan"  ,fg="black"  ,width=30  ,height=2, activebackground = "slate gray" ,font=('Bahnschrift SemiBold', 13,"bold"))
train.place(x=520, y=600)'''
add =Button(addwindow, text="ADD RECORD",bg="cyan"  ,fg="black"  ,width=30  ,height=2, activebackground = "slate gray",font=('Bahnschrift SemiBold', 13,"bold"))
add.place(x=920, y=600)

'''def collected():
    collected_list=[txt,txt1,txt2,cal,male,female,txt5,txt6,txt7]
    return collected_list'''
#------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------



addwindow.mainloop()
