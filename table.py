from tkinter import *
from  tkinter import ttk

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))
   
Label(text="OPA").pack()
Label(text="OPA2").pack(side = LEFT, fill = BOTH)
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()