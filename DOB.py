from tkinter import *
from tkcalendar import Calendar
def cal():
    dt_window = Tk()
    top = Toplevel()
    top.title("DOB-Date Picker")
    top.configure()

    def print_sel():
        print(cal.selection_get())
        top.destroy()

    cal = Calendar(top,font=('Bahnschrift SemiBold', 15,"bold"),
                              selectmode='day', year=2000, month=1, day=1,
                              foreground='black',background='cyan')
    cal.pack(fill="both", expand=True)
    Button(top, text="OK", command=print_sel).pack()
    
    dt_window.withdraw()
    dt_window.mainloop()
    return cal
