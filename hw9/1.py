from tkinter import *
import tkinter.messagebox 
root=Tk()
root.geometry("200x200")
def mess():
    tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
but=Button(root,text="Message",width=20, command=mess).place(x=0,y=0)
root.mainloop()