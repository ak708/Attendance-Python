import sqlite3 as sql
import DOB
import add_gui
import attendance_gui as att
import dropdownmenu as dpm
import Login_window as linw
import verification as veri
import edit_gui
import camera

collected=add_gui.collected()
usn=collected[0]
roll_no=collected[1]
name=collected[2]
dob= collected[3]
male= collected[4]
female= collected[5]
address=collected[6]
fathers_name=collected[7]
phone_no=collected[8]


conn= sql.connect("facerec.db")
cursor = conn.cursor
if int(male)==1 and int(female)==0:
    gender="male"
elif int(male)==0 and int(female)==1:

cursor.execute("""create table student 
                usn char(6),
                roll_no char(6),
                name varchar(30),
                dob date,
                """)
date=DOB.cal()





