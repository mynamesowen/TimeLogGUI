# Goal: Make a Python GUI app that can be used to track my working time and incidents.
#  - App should have options for Time (minutes), name, description, jobsite/location.

#from distutils.log import Log
from sqlite3 import Date
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import csv
import os
import pandas as pd

CSV_FILE_PATH = './TimeLogGUI/timelog.csv'

class MainWindow(tk.Frame):
    def __init__(self, container): # class constructor
        super().__init__(container) #calls the constructor of the Tk parent class. gives us access to the methods of the superclass Tk().
        
        font_style = ("Helvetica", 16)
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        # create 5 rows
        for i in range(0,6):
            self.rowconfigure(i, weight=2)

        self.date_label = ttk.Label(self, text='Date:', font=font_style)
        self.date_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        self.date = DateEntry(self)
        self.date.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # time spent label and entry
        self.time_spent_label = ttk.Label(self, text="Time (mins):", font=font_style)
        self.time_spent_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.time_spent_entry = ttk.Entry(self, font=font_style)
        self.time_spent_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # name label and entry
        self.affected_user_label = ttk.Label(self, text="Affected User:", font=font_style)
        self.affected_user_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.affected_user_entry = ttk.Entry(self, font=font_style)
        self.affected_user_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        # description label and entry
        self.description_label = ttk.Label(self, text="Description:", font=font_style)
        self.description_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        self.description_entry = ttk.Entry(self, font=font_style)
        self.description_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        # location label and entry
        self.location_label = ttk.Label(self, text='Location:', font=font_style)
        self.location_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

        self.location_entry = ttk.Entry(self, font=font_style)
        self.location_entry.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

        # submit button
        submit_button = ttk.Button(
            self, 
            text='Submit',
            command=lambda \
            t=self.time_spent_entry,
            u=self.affected_user_entry,
            d=self.description_entry,
            l=self.location_entry: \
            self.submit(t,u,d,l)
            ) # submit_button
        submit_button.grid(column=1, row=5, padx=5, pady=5)

        # view log button
        view_log = ttk.Button(self, text='View Log', command=self.open_log)
        view_log.grid(column=0, row=5, padx=5, pady=5)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def submit(self, time, user, des, loc):
        
        # verify all fields were entered
        if(time.get() and user.get() and des.get() and loc.get()):
            self.save_to_file([time.get(), user.get(), des.get(), loc.get()])

            # clear entry fields after data is saved
            self.clear_entries([time, user, des, loc])

        else:
            # if any field is blank present an error
            messagebox.showinfo(
                title='Error',
                message='All fields must be entered before submitting'
            )
    
    # clear the entry fields
    def clear_entries(self, entries):
        for i in entries:
            i.delete(0, 'end')

    # used to open new LogWindow frame
    def open_log(self):
        LogWindow(self)

    # used to save text from entries to csv file
    def save_to_file(self, row):
        # checking if the file exists and is empty
        if self.is_file_empty(CSV_FILE_PATH):
            print('File does not exist, creating and writing headers...')

            # create header arrary
            headers = ['time_spent', 'affected_user', 'description', 'location']

            # write headers to new file
            with open(CSV_FILE_PATH, 'w', newline='') as mycsv:
                csv.writer(mycsv).writerow(headers)

        # append rows to file
        with open(CSV_FILE_PATH, 'a', newline='') as f:
            # write row
            csv.writer(f).writerow(row)
            print('Appending to file...')

    # function used to check if timelog file exists and is empty
    # returns True is file is empty or does not exist, else returns false
    def is_file_empty(self, file_path):
        # Check if file exist and it is empty
        if os.path.exists(file_path): # does the path exist? 
            if os.stat(file_path).st_size == 0: # path exists, is it empty?
                return True # if empty return True
            else:
                return False # if not empty return false
        else:
            return True # if path does not exist return True

class LogWindow(tk.Toplevel):
    def __init__(self, container): # class constructor
        super().__init__(container) #calls the constructor of the Tk parent class. gives us access to the methods of the superclass Tk().

        self.title("Log")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(0, 0)
        
        # get the csv file
        self.log = pd.read_csv(CSV_FILE_PATH)
        self.tree = self.create_tree_widget()
    
    # create the tree widget displaying log data
    def create_tree_widget(self):
        columns = ['time_spent', 'affected_user', 'description', 'location']
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('time_spent', text='Time Spent')
        tree.heading('affected_user', text='Affected User')
        tree.heading('description', text='Description')
        tree.heading('location', text='Location')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # populate the treeview with data from the csv
        with open(CSV_FILE_PATH, newline='') as f:
            read = csv.DictReader(f, delimiter=',')
            for row in read:
                time = row['time_spent']
                user = row['affected_user']
                des = row['description']
                loc = row['location']
                
                tree.insert('', 0, values=(time, user, des, loc))
        
        # if the tree element is selected open up a window that shows its info
        tree.bind('<<TreeviewSelect>>', self.item_selected)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            messagebox.showinfo(title='Information', message= \
                f'Time: {record[0]}\n\nUser: {record[1]}\n\nDescription: {record[2]}\n\nLocation: {record[3]}')



    # def read_file(self):
    #     # open file
    #     with open(CSV_FILE_PATH, newline = "") as file:
    #         reader = csv.reader(file)

    #         # r and c tell us where to grid the labels
    #         r = 0
    #         for col in reader:
    #             c = 0
    #             for row in col:
    #                 # i've added some styling
    #                 label = tk.Label(self, text=row, border=1, borderwidth=1)
    #                 label.grid(row = r, column = c, padx=3, pady=3)
    #                 c += 1
    #             r += 1
        

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Time Log GUI')
        self.geometry('500x320')
        self.resizable(False, False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = App()
    MainWindow(app)
    app.mainloop()