from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from Services.read_csv import read_file, get_file_name
import csv

root = Tk()
root.title("Convert CSV in Table")
root.iconbitmap("Images/ico.ico")


# Function
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*csv')])
    filename.set(get_file_name(file_path.name))

    with open(file_path.name, "rt") as csv_file:
       reader = csv.reader(csv_file)

       data = list(map(lambda x: x, reader))

       for i in range(len(data)):
            for j in range(len(data[0])):
                if i == 0:
                    label = Label(
                        table_content,
                        font=("Arial", 16, ""),
                        width=20
                    )
                else:
                    label = Label(table_content, width=20,  font=("Arial", 16, ""))
                label.grid(row=i, column=j)
                label["text"] = data[i][j]


    if file_path is not None:
        pass


# System size
width = 700
heigth = 500


# Resolution of system
width_screen = root.winfo_screenwidth()
heigth_screen = root.winfo_screenheight()

# Position of windows
posx = width_screen/2 - width/2
posy = heigth_screen/2 - heigth/2

root.geometry("%dx%d+%d+%d" % (width, heigth, posx, posy))

# Frame
s = Style()
s.configure('My.TFrame', background="red")

menu = Frame(root, style='My.TFrame')
menu.place(width=150, height=heigth)
menu.config()

content = Frame(root)
table_content = Frame(root)

# Bind Variable
filename = StringVar()

# Windgets
lb_welcome = Label(menu, text="Welcome!")
lb_openCsv = Label(menu, text="Open CSV")

lb_upload = Label(content, text="Upload CSV File:")
lb_filename = Label(content, textvariable=filename)
btn_upload = Button(content, text="Choose file", command=lambda: open_file())
btn_cancel = Button(content, text="Cancel")

# Grid
menu.grid(row=0, column=0, sticky=(N, W, E, S))
content.grid(row=0, column=1)
table_content.grid(row=1, column=1)

lb_welcome.grid(row=0, column=0)
lb_openCsv.grid(row=3, column=0)

lb_upload.grid(row=1, column=0)
lb_filename.grid(row=1, column=1)
btn_upload.grid(row=1, column=2)
btn_cancel.grid(row=1, column=3)



root.mainloop()
