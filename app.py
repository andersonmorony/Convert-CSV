import base64
from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image  
from Services.funcs import Funcs

root = Tk()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.variable()
        self.screen()
        self.frame()
        self.widgets_frame1()
        self.widgets_frame_menu()
        root.mainloop()
    def screen(self):
        self.root.title("Convert CSV in Table")
        self.convert_icon_base64()
        # System size   
        width = 1024
        heigth = 500
        # Resolution of system
        width_screen = self.root.winfo_screenwidth()
        heigth_screen = self.root.winfo_screenheight()
        # Position of windows
        posx = width_screen/2 - width/2
        posy = heigth_screen/2 - heigth/2
        self.root.configure(background= '#444444')
        self.root.geometry("%dx%d+%d+%d" % (width + 100, heigth, posx, posy ))
        self.root.resizable(True, True)
        self.root.minsize(1024, 500)
    def frame(self):
        self.side_menu = Frame(self.root, bd = 4, bg= '#444444', highlightbackground= '#444444', highlightthickness=3 )
        self.side_menu.place(relwidth= 0.1, relheight= 1)
        
        self.frame_1 = Frame(self.root, bd = 4, bg= '#f2f2f2', highlightthickness=3 )
        self.frame_1.place(relx= 0.11, rely=0, relwidth= .89, relheight= 1)
    def widgets_frame1(self):
        ### Create label
        self.lb_upload_text = Label(self.frame_1, text= "Upload file:", bd=2, fg='#444444', font=('verdana', 8, 'bold'))
        self.lb_upload_text.place(relx= 0, rely=0.01, relwidth=0.1, relheight= 0.05)

        self.filename = StringVar()
        self.filename.set("No file selected")
        self.lb_filename = Label(self.frame_1, textvariable=self.filename, bd=2, fg='#444444', font=('verdana', 8))
        self.lb_filename.place(relx= 0.1, rely= 0.01, relheight= 0.05)

        ### Create button
        self.btn_upload_file = Button(self.frame_1, command=self.upload_file, text="Select file", cursor="hand2", bd=1, bg="#0066cc", fg="#fbfbfd", font=('verdana', 8, 'bold'))
        self.btn_upload_file.place(relx= 0.4, rely= 0.01, relwidth=0.1, relheight= 0.05)

        
        ### Add information label
        self.lb_information = Label(self.frame_1, textvariable=self.quantity_row, bd=2, fg='#444444', font=('verdana', 8))
        self.lb_information.place(relx= 0.73, rely= 0.60, relheight= 0.05)
        
        ### Add loading label
        self.lb_loafing = Label(self.frame_1, textvariable=self.loading, bd=2, fg='#444444', font=('verdana', 10))
        self.lb_loafing.place(relx= 0.85, rely= 0.95, relwidth=.1, relheight= 0.05)
    def widgets_frame_menu(self):
        # Create an object of tkinter ImageTk
        self.convert_logo_base64()

        # Create a Label Widget to display the text or Image
        self.lb_logo = Label(self.side_menu, image = self.logo, bg="#444444", text="Convert")
        self.lb_logo.place(relx=0.025, rely=0.025, relwidth=.95, relheight=0.2)
        
        self.lb_title_side_menu = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="Convert CSV", font=('verdana', 8, 'bold'))
        self.lb_title_side_menu.place(relx=0.025, rely=0.22, relwidth=.95)

        if self.showButtons.get():

            self.lb_title_side_menu = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="Save as:", font=('verdana', 8, 'bold'))
            self.lb_title_side_menu.place(relx=0.025, rely=0.28, relwidth=.95, relheight=0.15)

            self.btn_save_was_excel = Button(self.side_menu, text="Excel", font=('verdana', 8, 'bold'), bg="#71C598", fg="#fbfbfb", cursor="hand2",bd=1 , highlightbackground="#000", command=self.convert_to_excel )
            self.btn_save_was_excel.place(relx=0.05, rely=0.4, relwidth=.9, relheight=0.05)
                
            self.btn_save_was_excel = Button(self.side_menu, text="PDF", font=('verdana', 8, 'bold'), bg="#EF4823", fg="#fbfbfb", cursor="hand2", bd=1, highlightbackground="#000", command=self.save_pdf )
            self.btn_save_was_excel.place(relx=0.05, rely=0.46, relwidth=.9, relheight=0.05)
            
            self.btn_save_was_json = Button(self.side_menu, text="JSON",font=('verdana', 8, 'bold'), bg="#E6AD0E", fg="#fbfbfb", cursor="hand2", bd=1, highlightbackground="#000", command=self.save_Json )
            self.btn_save_was_json.place(relx=0.05, rely=0.52, relwidth=.9, relheight=0.05)

            self.widgets_orderby()
            self.widgets_btn_functions()

        ### Version
        self.lb_version = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="V1.0", font=('verdana', 8, 'bold'))
        self.lb_version.place(relx=0, rely=0.88, relwidth=1, relheight=0.15)
    def widgets_btn_functions(self):
        self.lb_functions = Label(self.side_menu, text="Functions", bg='#444444',fg="#f2f2f2", font=('verdana', 8, 'bold'))
        self.lb_functions.place(relx=0.05, rely=0.58, relwidth=.9, relheight=0.08)

        self.btn_save_was_json = Button(self.side_menu, text="Remove\nDuplicate", bg="#f2f2f2", cursor="hand2", command=self.remove_duplicate_values )
        self.btn_save_was_json.place(relx=0.05, rely=0.66, relwidth=.9, relheight=0.08)
    def widgets_orderby(self):
        ### Add Radion button to sort column
        self.lb_orderby = Label(self.frame_1, text="Order By:", fg='#444444', font=('verdana', 8, 'bold'))
        self.lb_orderby.place(relx= 0.01, rely= 0.60, relheight= 0.05)

        self.rb_asc = Radiobutton(self.frame_1, text="ASC", variable=self.order_by, value=0, fg='#444444', font=('verdana', 8))
        self.rb_asc.place(relx= 0.1, rely= 0.60, relheight= 0.05)

        self.rb_desc = Radiobutton(self.frame_1, text="DESC", variable=self.order_by, value=1, fg='#444444', font=('verdana', 8))
        self.rb_desc.place(relx= 0.18, rely= 0.60, relheight= 0.05)
    def variable(self):
        self.showButtons = BooleanVar()
        self.file_path = StringVar()
        self.quantity_row = StringVar()
        self.dataframe_csv = []
        self.loading = StringVar()
        self.order_by = IntVar()
    def convert_icon_base64(self):
        ##The Base64 icon version as a string
        icon = \
        """iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAAD
/klEQVR4nO2Z2U8TQRjAG+LxH9BZRUFE1KqJig8ouAu0CnjG4oEnggREoiAgKCBFIQZFqeBtxKPd
A/TBxAeiCRFiYnxQMWK2eDwaX9QHY/RBHvzMDLC0dmna7oWRSb7s5NvOzPfb75jZrck00SbaRAui
JUxGiKk1I6bPjJhfiGJAqVAU/dxkMkWYtG4Wi2UKouhnahjtJ4hp1xwCP3lNjNcLwoyYvtHF6DIc
Tkrmk4egb2oG4R3zOJyUzje2J2htILwX8dazHr6Y8/AfWJH/zXkECFa859tUUKQ9hByAW+TzQjF6
LABW5LWHkAPgRP5ZuADTZ6RJ87n6We0h5ABYUfgULkDCyixpvnxHlfYQagPk1lSEutmNLwBXPwfL
bduChjCNN4ARiNzaI5BAb/bJCTlhBzpSxx1AKJWK8/A/FUGYEf0VT4SvxgAIWH6wbzuSwgKgqJR0
hGgeXw0EAFYUBkxqNSMAOI8A/xdAZGRyLKLoHkQxg4GqhNW+B9xveJ+FChuPQVR04OoSrCRlZENr
97XQAcwU3RvsIs6HV3wAFi3boIrxaAQic3sYAEG+OmrtAUQxZK8IGSDQbqh1DnBj5IKqALf63LBh
byHMiLHBgoT1UNLikBYuaz0B8xevJWNnz0uHnWWlxEsOthni5mdAzc3T0m+r25sgOtYGNe1N+gKk
2ff4ubruzhmSD9OjUv3uNd51QtXVU6SfaN0qGZlo3Up0FZca9ANo7Gz5gvXxCzJJhTh41kGebD13
FsovNpAxS5Ps4HrDwbmuy1DcVEs8gI/OcywZ5H7T/TY48+AC6eOxd16z+gEUnDj2Deu3FBX7LXr+
ka8H4hdmwv6Gaun+rvLDRI/Db31uAenvqijTNwcCAZAcaDsJliXrfEOos4Xcu9R7HaZFpZAqFRWd
RvpYpytA4z3nZ6zH4dDafRUOO+tJGOAkvfLkBmSXHCKewIuu3Z1P5iioPyoZZsvKkea2bc4xpgpZ
7TmySYzDRa6W4yQeMazO3Tw6xt1sDMDtVy7YmLcfZs6yDpVR51AZxXp74QGIiVtFxs5duIZsbN6G
4Xfg5auzYUX6dtI3BOBf2MgG1ToKGHWUeGy04WhYktfsUHScNvDJpxLj28I5TgfKBb1ygPtL/hmA
neWlZJPDV8UAcp/XtQRw9bPStyJ8SlUD4KXkBcRUYAitAFz9LOyrq5Q8vozJUg4QSdHVRiVxXm2l
coDhfyif6m184qpt5BOkCgBDENgTZop+odbfrPJlM42ETd7xSj/jFQL4NlYUnuteRkXho2oAbg9f
qjuARzitGoADHBGcR2jgRP679obzP1mRv9D1vmuqagDeIKzIRnPvuFgtRBgQYnp6eiYFMuIPbCUB
Y5l7NbkAAAAASUVORK5CYII="""
        img=base64.b64decode(icon)
        img=PhotoImage(data=img) 
        self.root.wm_iconphoto(True, img)
    def convert_logo_base64(self):
        icon = \
        """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
6zJoh/0LaL4rtr6Qt8AAAAAASUVORK5CYII="""
        img=base64.b64decode(icon)
        self.logo = ImageTk.PhotoImage(data=img)

Application()