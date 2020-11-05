import sqlite3 as sql
import DOB
import add_gui
import attendance_gui as att
import dropdownmenu as dpm
import Login_window as linw
import verification as veri
import edit_gui
import camera
from draganddrop import *
import drdppathlink as drdp
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import csv
import sqlite3
def add_sql():
    def check_db():
        conn1=lite.connect("facerec.db")
        cursor=conn1.cursor()
        stmt = "SHOW TABLES LIKE 'attendance'"
        cursor.execute(stmt)
        result = cursor.fetchone()
        if result:
            # there is a table named "students"
            return True
        else:
            # there are no tables named "students"
            cursor.execute("""create table student
                    usn char(6) primary key,
                    roll_no numeric(6),
                    name varchar(30),
                    dob date,
                    gender varchar(6),
                    address varchar(200),
                    fathers_name varchar(30),
                    phone_no varchar(10),
                    image blob;
                    """)
            return False
    check_db()


    #getting data from add_gui.py
    usn=add_gui.txt.get()
    roll_no=add_gui.txt1.get()
    name=add_gui.txt2.get()
    dob=add_gui.cal.get()
    male=add_gui.male.get()
    female=add_gui.female.get()
    address=add_gui.txt5.get()
    fathers_name=add_gui.txt6.get()
    phone_no=add_gui.txt7.get()
    imgdir=""
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    
    sys.exit(app.exec_())
    #establishing connection
    conn= lite.connect("facerec.db")
    cursor = conn.cursor()


    #getting attendance time
    timedis=dt.datetime.now()
    tstr=timedis.strftime("%H:%M:%S")
    dstr=timedis.strftime("%d/%m/%Y")


    #getting gender
    if int(male)==1 and int(female)==0:
        gender="male"
    elif int(male)==0 and int(female)==1:
        gender="female"

    dr&dp.Appdemo()
    #inserting entered data
    cursor.execute("INSERT into attendance values(:usn,:roll_no,:name,:dob,:gender,:address,:f_name,:ph_no,:image)
                    {
                        "usn":usn,
                        "roll_no":roll_no,
                        "name":name,
                        "dob":dob,
                        "gender":gender,
                        "address":address,
                        "f_name":f_name,
                        "phone_no":ph_no
                        "image":imgdir
                    }
                    ")


    #clearing input boxes
    add_gui.txt.delete(0, END)
    add_gui.txt1.delete(0, END)
    add_gui.txt2.delete(0, END)
    add_gui.cal.delete(0, END)
    add_gui.male.delete(0, END)
    add_gui.female.delete(0, END)
    add_gui.txt5.delete(0, END)
    add_gui.txt6.delete(0, END)
    add_gui.txt7.delete(0, END)
    conn.commit()
    conn.close()
