from tkinter import *

app = Tk()
app.title("Fufux IDE v0.01-alpha - for Python")
app.geometry("1280x720")
app.configure(bg="#292D34")
app.resizable(False, False)

icon = PhotoImage(file="img/logo.png")
app.iconphoto(False, icon)

editor = Text(app, font="Consolas 14")
editor.place(x=64, y=0, width=256*3, height=720)
editor.configure(bg="#393D44")

app.mainloop()
