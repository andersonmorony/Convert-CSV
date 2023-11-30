from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Tk
from tkinter.filedialog import askopenfile
import csv
import pandas as pd


root = Tk()

class Funcs():
    def upload_file(self):
        try:
            ### read csv file
            file_path = askopenfile(mode='r', filetypes=[('Image Files', '*csv')]) 

            ### Save csv data in a variable
            df = pd.read_csv(file_path.name)
            self.dataframe_csv = df

            ### upload filename label
            self.filename.set(file_path.name)

            ### read csv
            self.read_csv()
        except FileNotFoundError as error:
            print(f"Log: FileNotFoundError - {error}")
        except AttributeError as error:
            print(f"Log: AttributeError - {error}")
    def show_csv_data(self, data):
        isFirstTime = True
        quantity_row = Variable()
        rows = IntVar()
        for row in data:
            newValue = rows.get() + 1
            rows.set(newValue)
            if isFirstTime:
                self.listaCli = ttk.Treeview(self.frame_1, height=3, columns=row)
                self.listaCli.heading("#0", text="")
                self.listaCli.column("#0", width=0)
                index = 1
                for value in row:
                    self.listaCli.heading(f"#{index}", text=value.capitalize(), command=lambda column = value: self.orderBy_column(column))
                    index+= 1
                self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.50)
                isFirstTime = False 
            else:
                self.listaCli.insert("", END, values=row)
        

        # Add Scroll
        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.50)

    def convert_to_excel(self):
        try:
            df = self.dataframe_csv
            with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
                resultExcelFile = pd.ExcelWriter(file.name)
                df.to_excel(resultExcelFile, index=False)
                resultExcelFile.close()

        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
    def verify_duplicate_item(self):
        df = pd.read_csv(self.file_path.get())
    def orderBy_column(self, column):
        df = self.dataframe_csv
        df_sorted = df.sort_values(by=[f'{column}'], ignore_index=True)

        ### Clean treen before insert new values
        self.clean_treeview()
        
        tree = self.tree
        counter = len(df)
        df_col = df_sorted.columns.values
        tree["columns"]=(df_col)
        tree.column("#0", width=0)
        for x in range(len(df_col)):
            tree.column(x)
            tree.heading(x, text=df_col[x].capitalize(), command=lambda column = df_col[x]: self.orderBy_column(column))

        for i in range(counter):
            tree.insert('', END, values=df_sorted.iloc[i,:].tolist())

        tree.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.50)
    def read_csv(self):
        df = pd.DataFrame(self.dataframe_csv)
        self.tree = ttk.Treeview(self.frame_1)
        counter = len(df)
        df_col = df.columns.values
        self.tree["columns"]=(df_col)
        self.tree.column("#0", width=0)
        for x in range(len(df_col)):
            self.tree.column(x, width=100)
            self.tree.heading(x, text=df_col[x].capitalize(), command=lambda column = df_col[x]: self.orderBy_column(column))

        for i in range(counter):
            self.tree.insert('', END, values=df.iloc[i,:].tolist())
        
        self.tree.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.50)
        
        # Add Scrool
        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.tree.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0.1, relwidth=0.04, relheight=0.50)

        # Add Label with information
        row_count = df.shape[0]  # Returns number of rows
        col_count = df.shape[1]  # Returns number of columns
        self.quantity_row.set(f"{col_count} column and {row_count} rows was loaded.")

        # Show Button in side frame
        self.showButtons.set(True)  
        self.widgets_frame_menu()
    def clean_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        

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
    def widgets_frame_menu(self):
        if self.showButtons.get():
            self.lb_title_side_menu = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="Convert you\n CSV to:", font=('verdana', 8, 'bold'))
            self.lb_title_side_menu.place(relx=0.025, rely=0.28, relwidth=.95, relheight=0.15)

            self.btn_save_was_excel = Button(self.side_menu, text="Excel", bg="#f2f2f2", cursor="hand2", command=self.convert_to_excel )
            self.btn_save_was_excel.place(relx=0.05, rely=0.4, relwidth=.9, relheight=0.05)
                
            self.btn_save_was_excel = Button(self.side_menu, text="PDF", bg="#f2f2f2", cursor="hand2" )
            self.btn_save_was_excel.place(relx=0.05, rely=0.46, relwidth=.9, relheight=0.05)

        self.lb_version = Label(self.side_menu, fg="#f2f2f2", bg="#444444", text="V1.0", font=('verdana', 8, 'bold'))
        self.lb_version.place(relx=0, rely=0.88, relwidth=1, relheight=0.15)
    def variable(self):
        self.showButtons = BooleanVar()
        self.file_path = StringVar()
        self.quantity_row = StringVar()
        self.dataframe_csv = []
    
Application()