#kharbozeeeeeeeeeeeee
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

##from tkinter import *
##from tkinter import messagebox
##
##root = Tk()
##root.title('suduko.game')
##window = grid(root,row = 8,column = 4,padx = 20,pady = 30)
##def change_frame(frame):
##    frame.tkraise()
##
##suduco_page = Frame(root)
##menu_page = Frame(root)
##
###in label zir fake
##
##hello = Label(root,fg = 'black')
##hello.grid(row = 1,column = 1)
##
##for frame in (suduco_page, menu_page):
##    frame.grid(heghth = 6,wgheit = 7, sticky='news')
##    
##
##easy = Button(menu_page,padx = 30,pady = 12, text='easy', command = lambda:change_frame(suduco_page))
##easy.grid(row = 3,column = 6)
##
##normal = Button(menu_page,padx = 30,pady = 12, text='normal', command = lambda:change_frame(suduco_page))
##normal.grid(row = 1,column = 1)
##
##hard = Button(menu_page,padx = 30,pady = 12, text='hard', command = lambda:change_frame(suduco_page))
##hard.grid(row = 2,column = 2)
##
###
##Button(suduco_page, text='<- back', command = lambda:change_frame(menu_page))

