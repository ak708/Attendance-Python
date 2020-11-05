import sqlite3 as lite
import attendance_gui as ag
import datetime as dt



def attendance_mark():
    def check_table():
    conn1=lite.connect("facerec.db")
    cursor=conn1.cursor()
    stmt = "SHOW TABLES LIKE 'attendance'"
    cursor.execute(stmt)
    result = cursor.fetchone()
    if result:
        # there is a table named "attendance"
        return True
    else:
        # there are no tables named "attendance"
        cursor.execute("""create table attendance 
                usn char(6),
                time time,
                date date;
                """)
        return False
    check_table()
    usn1=ag.collect_attendance()
    conn= lite.connect("facerec.db")
    cursor = conn.cursor()
    timedis=dt.datetime.now()
    tstr=timedis.strftime("%H:%M:%S")
    dstr=timedis.strftime("%d/%m/%Y")
    cursor.execute("INSERT into attendance values(:usn,:time,:date);
                    {
                        "usn":usn1,"time":tstr,"date":dstr
                    }
                    ")
    ag.txt6.delete(0, END)
    conn.commit()
    conn.close()
