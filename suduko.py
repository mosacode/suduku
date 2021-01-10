from tkinter import *
import tkinter.messagebox
from tkinter import messagebox


root=Tk()

root.geometry('500x500')
root.resizable(True,True)
root.title("suduku!!!")

ent=[]

for i in range(1,10):
    for j in range (1,10):
        ent.append(Entry(root, width=3))
        ent[len(ent)-1].grid(row=i, column=j)



root.mainloop()
