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
        self.root.iconbitmap("Images/ico.ico")
        # System size   
        width = 1024
        heigth = 500
        # Resolution of system
        width_screen = self.root.winfo_screenwidth()
        heigth_screen = self.root.winfo_screenheight()
        # Position of windows
        posx = width_screen/2 - width/2
        posy = heigth_screen/2 - heigth/2
        self.root.configure(background= '#eee')
        self.root.geometry("%dx%d+%d+%d" % (width + 100, heigth, posx, posy ))
        self.root.resizable(True, True)
        self.root.minsize(1024, 500)
    def frame(self):
        self.side_menu = Frame(self.root, bd = 4, bg= '#444444', highlightbackground= '#444444', highlightthickness=3 )
        self.side_menu.place(relwidth= 0.1, relheight= 1)
        
        self.frame_1 = Frame(self.root, bd = 4, bg= '#f2f2f2', highlightthickness=3 )
        self.frame_1.place(relx= 0.11, rely=0, relwidth= .88, relheight= 1)
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
        self.lb_information.place(relx= 0.01, rely= 0.60, relheight= 0.05)
        
        ### Add loading label
        self.lb_loafing = Label(self.frame_1, textvariable=self.loading, bd=2, fg='#444444', font=('verdana', 10))
        self.lb_loafing.place(relx= 0.85, rely= 0.95, relwidth=.1, relheight= 0.05)
    def widgets_frame_menu(self):
        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("images/logo.png"))

        # Create a Label Widget to display the text or Image
        self.lb_logo = Label(self.side_menu, image = self.img, bg="#444444", text="Convert")
        self.lb_logo.place(relx=0.025, rely=0.025, relwidth=.95, relheight=0.2)
        
        self.lb_title_side_menu = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="Convert CSV", font=('verdana', 8, 'bold'))
        self.lb_title_side_menu.place(relx=0.025, rely=0.22, relwidth=.95)

        if self.showButtons.get():

            self.lb_title_side_menu = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="Save as:", font=('verdana', 8, 'bold'))
            self.lb_title_side_menu.place(relx=0.025, rely=0.28, relwidth=.95, relheight=0.15)

            self.btn_save_was_excel = Button(self.side_menu, text="Excel", bg="#f2f2f2", cursor="hand2", command=self.convert_to_excel )
            self.btn_save_was_excel.place(relx=0.05, rely=0.4, relwidth=.9, relheight=0.05)
                
            self.btn_save_was_excel = Button(self.side_menu, text="PDF", bg="#f2f2f2", cursor="hand2", command=self.save_pdf )
            self.btn_save_was_excel.place(relx=0.05, rely=0.46, relwidth=.9, relheight=0.05)

        self.lb_version = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="V1.0", font=('verdana', 8, 'bold'))
        self.lb_version.place(relx=0, rely=0.88, relwidth=1, relheight=0.15)
    def variable(self):
        self.showButtons = BooleanVar()
        self.file_path = StringVar()
        self.quantity_row = StringVar()
        self.dataframe_csv = []
        self.loading = StringVar()
    
Application()