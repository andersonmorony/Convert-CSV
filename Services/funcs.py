from tkinter import *
from tkinter import ttk, messagebox 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from Services.pdfFunction import dataframe_to_pdf
import pandas as pd
from threading import Thread
import sys
import json
sys.path.append('Services')

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
    def convert_to_excel(self):
        try:
            df = self.dataframe_csv
            with filedialog.asksaveasfile(mode='w', defaultextension=".xlsx") as file:
                resultExcelFile = pd.ExcelWriter(file.name)
                df.to_excel(resultExcelFile, index=False)
                resultExcelFile.close()
            
            messagebox.showinfo("Success", "Your file has been successfully converted and saved. 🔄💾") 

        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
    def verify_duplicate_item(self):
        df = pd.read_csv(self.file_path.get())
    def orderBy_column(self, column):
        df = self.dataframe_csv
        df_sorted = self.orderBy(df, column)
        self.dataframe_csv = df_sorted

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
        self.scroolLista.place(relx=0.95, rely=0.1, relwidth=0.04, relheight=0.50)

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
    def save_pdf(self):
        self.loading.set("loading...")
        try:
            with filedialog.asksaveasfile(mode='w', defaultextension=".pdf") as file:
                page_size = self.dataframe_csv.shape[0]
                param = (1, 1) if page_size < 50 else (round(page_size / 50), 1)
                Thread(target=dataframe_to_pdf(self.dataframe_csv, file.name, param)).start()
            self.loading.set("")
            messagebox.showinfo("Success", "Your file has been successfully converted and saved. 🔄💾")
        except TypeError as error:
            self.loading.set("")
            print(error)
    def orderBy(self, df, column):
        try:
            return df.sort_values(by=[f'{column}'], ignore_index=True) 
        except KeyError as error:
            return f"Key not found"
    def save_Json(self):
        try:
            self.loading.set("loading...")
            with filedialog.asksaveasfile(mode='w', defaultextension=".json") as file:
                self.dataframe_csv.to_json(file.name, orient='records')
                self.loading.set("")
                messagebox.showinfo("Success", "Your file has been successfully converted and saved. 🔄💾") 
        except TypeError as error:
            self.loading.set("")
            print(error)
