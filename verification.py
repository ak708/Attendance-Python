from tkinter import *
import sys
def verification():
    def verify_pin(event):
        if v_entry.get() == '123':
            msg = Label(top, text='Attendance has been marked',fg="green" ,font=('Bahnschrift',14,"italic")).pack()
            top.after(1000, top.destroy)
        elif v_entry.get() !='123':
            msg1 = Label(top, text='Incorrect PIN',fg="green" ,font=('Bahnschrift',14,"italic"))
            msg1.place(x=140, y=50)
            msg1.after(1000, msg1.destroy)

    v_window = Tk()
    top = Toplevel()

    top.title("Manual Attendance Verification")
    top.geometry('400x100')
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    x = (ws/2) - (400/2)
    y = (hs/2) - (100/2)
    top.geometry('%dx%d+%d+%d' % (400, 100, x, y))
    top.configure()

    v_lbl = Label(top, text='Enter PIN for verification : ',font=('Bahnschrift SemiBold', 15, "bold"))
    v_entry = Entry(top, bg='white',width=8, show="*")
    v_entry.bind('<Return>', verify_pin)

    v_lbl.pack()
    v_entry.pack()

    v_window.withdraw()
    v_window.mainloop()
