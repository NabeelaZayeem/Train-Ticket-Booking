import tkinter as tk
from tkinter import *
from subprocess import call
def clickabout():
    call(["python","login_page.py"])
def clickabout1():
    call(["python", "Register_details.py"])
root = tk.Tk()
root.minsize(height=500,width=500)
root.title("RAILWAY TICKET RESERVATION")
def close():
    root.destroy()
    root.quit()
label1 = Label(root,text='Ticket Booking',width=20,bg='white',
               font=('Times_New_Roman',20,'bold')).place(x=90,y=53)
root['bg']='white'
Button(root,text='Login',width=20,bg='brown',fg='white',command=clickabout).place(x=180,y=130)
Button(root,text='Register',width=20,bg='brown',fg='white',command=clickabout1).place(x=180,y=180)
Button(root,text='Exit',width=20,bg='brown',fg='white',command=close).place(x=180,y=230)

root.mainloop()
