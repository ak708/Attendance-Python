from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

preview = Tk()
preview.withdraw()

def open_pic():
    global picture
    filename = filedialog.askopenfilename(initialdir = "/",filetypes=[("Pictures", "*.jpg"),("Pictures", "*.bmp"),("Pictures", "*.jpeg"),("Pictures", "*.png")])
    picture = ImageTk.PhotoImage(Image.open(filename))

    top = Toplevel()
    top.title("Student ID Photo Preview")
    ww = 550
    wh = 500
    sw = top.winfo_screenwidth()
    sh = top.winfo_screenheight()
    x = (sw/2) - (ww/2)
    y = (sh/2) - (wh/2)
    top.geometry('%dx%d+%d+%d' % (ww, wh, x, y))
    top.configure()

    lbl = Label(top,image = picture).pack()

    top.after(2000,lambda:top.destroy())
    top.mainloop()
    return filename
