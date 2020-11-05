from tkinter import *
import sys

def verify(event):
    if entry.get() == '123':
        l_window.deiconify()
        top.destroy()

l_window = Tk()
top = Toplevel()

top.title("Login-PIN Protected Database")
top.geometry('400x100')

ws = top.winfo_screenwidth()
hs = top.winfo_screenheight()
x = (ws/2) - (400/2)
y = (hs/2) - (100/2)
top.geometry('%dx%d+%d+%d' % (400, 100, x, y))
top.configure()

l_lbl = Label(top, text='Enter PIN : ', font=('Bahnschrift SemiBold', 15, "bold"))
entry = Entry(top, bg='white', show="*")
entry.bind('<Return>', verify)

l_lbl.pack()
entry.pack()
# l_button.pack()

l_window.title('main')
l_window.geometry('10x10')

l_window.withdraw()
l_window.mainloop()
