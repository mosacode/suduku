from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import tkinter.font as font

root=Tk()

root.geometry('500x500')
root.resizable(True,True)
root.title("suduku!!!")

ent=[]

for i in range(1,10):
    for j in range (1,10):
        ent.append(Entry(root, width=4))
        ent[len(ent)-1].grid(row=i, column=j)


inp=[]

def catcher():
    for i in range(9):
        for j in range (9):
            inp.append(ent[i*9+j].get())



def block_check():
    catcher()


buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
btn_submit = Button(root, text = 'Finish',font=buttonFont, fg = "red", bg = 'brown', width=30, command=block_check())
btn_submit.grid(row = 10, column = 1, columnspan=9)

root.mainloop()

