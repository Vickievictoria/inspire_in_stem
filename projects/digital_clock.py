#!/usr/bin/python

####################
# name: Victoria
#file: operations.py
#date: 6/6/2022
######################

from tkinter import *
from tkinter.ttk import *
from time import strftime 

#creating a window
window = Tk()
window.title('Digital clock')

def time():
    string = strftime('%H :%M : %S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(window, font = ('calibri', 30 , 'bold'),
            background = 'blue',
            foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()