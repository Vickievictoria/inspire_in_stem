#!/usr/bin/python
####################
# name: Victoria
#file: operations.py
#date: 6/6/2022
######################

from tkinter import *

window=Tk()
window.title("Welcome to my app")
window.configure(bg="white")#background color
window.geometry("400x400")
f_name=Label(window,text="First Name",font=("Ariel",20))
s_name=Label(window,text="Second Name",font=("Ariel",20))

f_name.grid(column=30,row=30)
s_name.grid(column=30,row=60)
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg="green")
    #msg=Label(top.text="Welcome to the pop up",font=("aerial").place(x=150,y=150))

btn=Button(window,text="Click Here",bg="yellow",fg="grey")
btn.grid(column=120,row=150)


fname_box=Entry(window,width=30)
fname_box.grid(column=120,row=30)
sname_box=Entry(window,width=30)
sname_box.grid(column=120,row=60)

#digital and analog clock
#my clock 
#show time 
#tkinter library andfigma
#ktinker designer






window.mainloop()