# Goal: Make a Python GUI app that can be used to track my working time and incidents.
#  - App should have options for Time (minutes), name, description, jobsite/location.

import tkinter as tk
from tkinter import ttk, messagebox
from numpy import sum
from tkcalendar import DateEntry
import csv
import pandas as pd
from pathlib import Path

CSV_DIRECTORY = 'C:/Temp/TimeLog/'
CSV_FILE_PATH = 'C:/Temp/TimeLog/TimeLog.csv'

class MainWindow(tk.Frame):
    def __init__(self, container): # class constructor
        super().__init__(container) #calls the constructor of the Tk parent class. gives us access to the methods of the superclass Tk().
        
        self.font_style = ("Helvetica", 16)
        self.headers = ['date', 'time_spent', 'affected_user', 'description', 'location']
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        # create 5 rows
        for i in range(0,6):
            self.rowconfigure(i, weight=2)

        self.date_label = ttk.Label(self, text='Date:', font=self.font_style)
        self.date_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        self.date_entry = DateEntry(self)
        self.date_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # time spent label and entry
        self.time_spent_label = ttk.Label(self, text="Time (mins):", font=self.font_style)
        self.time_spent_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.time_spent_entry = ttk.Entry(self, font=self.font_style)
        self.time_spent_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # name label and entry
        self.affected_user_label = ttk.Label(self, text="Affected User:", font=self.font_style)
        self.affected_user_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.affected_user_entry = ttk.Entry(self, font=self.font_style)
        self.affected_user_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        # description label and entry
        self.description_label = ttk.Label(self, text="Description:", font=self.font_style)
        self.description_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        self.description_entry = ttk.Entry(self, font=self.font_style)
        self.description_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        # location label and entry
        self.location_label = ttk.Label(self, text='Location:', font=self.font_style)
        self.location_label.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

        self.location_entry = ttk.Entry(self, font=self.font_style)
        self.location_entry.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

        # submit button
        self.submit_button = ttk.Button(self, text='Submit', command=self.submit) # submit_button
        self.submit_button.grid(column=2, row=5, padx=5, pady=5)

        # view log button
        self.view_log = ttk.Button(self, text='View Log', command=self.open_log)
        self.view_log.grid(column=0, row=5, padx=5, pady=5)

        # timesheet button
        self.timesheet_button = ttk.Button(self, text="Timesheet", command=self.timesheet)
        self.timesheet_button.grid(column=1, row=5, padx=5, pady=5)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def submit(self):
        date = self.date_entry.get()
        time = self.time_spent_entry.get()
        user = self.affected_user_entry.get()
        des = self.description_entry.get()
        loc = self.location_entry.get()
        
        # verify all fields were entered
        if(date and time.isnumeric() and user and des and loc):
            self.save_to_file([date, time, user, des, loc]) # save entries to file
            self.clear_entries() # clear entry fields after data is saved

        else:
            if time.isnumeric() == False: # if time_spent is not an integer produce error
                messagebox.showinfo(
                    title='Error',
                    message='Time spent must be a whole number (i.e. 15, 30, 60, etc.)'
                )
            else:
                # if any field is blank present an error
                messagebox.showinfo(
                    title='Error',
                    message='All fields must be entered before submitting'
                )
    
    # clear the entry fields
    def clear_entries(self):
        self.time_spent_entry.delete(0, 'end')
        self.affected_user_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.location_entry.delete(0, 'end')

    # used to open new LogWindow frame
    def open_log(self):
        LogWindow(self)

    # used to open timesheet frame
    def timesheet(self):
        Timesheet(self)

    # used to save text from entries to csv file
    def save_to_file(self, row):

        # try to write to the file. if it does not exist create it and write data
        try:
            # append rows to file
            with open(CSV_FILE_PATH, 'a', newline='') as f:
                # write row
                csv.writer(f).writerow(row)
                print('Appending to file...')

        except FileNotFoundError:
            Path(CSV_DIRECTORY).mkdir(parents=True, exist_ok=True) # create the directory if it does not exist.
            print('File does not exist, creating and writing headers...')

            # write headers and entries to new file
            with open(CSV_FILE_PATH, 'w', newline='') as f:
                csv.writer(f).writerow(self.headers)
                csv.writer(f).writerow(row)


class LogWindow(tk.Toplevel):
    def __init__(self, container): # class constructor
        super().__init__(container) #calls the constructor of the Tk parent class. gives us access to the methods of the superclass Tk().

        self.title("Log")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(0, 0)
        
        # get the csv file
        self.tree = self.create_tree_widget()
    
    # create the tree widget displaying log data
    def create_tree_widget(self):
        columns = ['date', 'time_spent', 'affected_user', 'description', 'location']
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('date', text='Date')
        tree.heading('time_spent', text='Time Spent')
        tree.heading('affected_user', text='Affected User')
        tree.heading('description', text='Description')
        tree.heading('location', text='Location')

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # populate the treeview with data from the csv
        with open(CSV_FILE_PATH, newline='') as f:
            read = csv.DictReader(f, delimiter=',')
            for row in read:
                date = row['date']
                time = row['time_spent']
                user = row['affected_user']
                des = row['description']
                loc = row['location']
                
                tree.insert('', 0, values=(date, time, user, des, loc))
        
        # if the tree element is double clicked open up a window that shows its info
        tree.bind('<Double-1>', self.item_selected)

        return tree

    # function for displaying a specific item in the tree
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            messagebox.showinfo(title='Information', message= \
                f'Date: {record[0]}\nTime: {record[1]} (mins)\nUser: {record[2]}\nDescription: {record[3]}\nLocation: {record[4]}')

class Timesheet(tk.Toplevel):
    def __init__(self, container): # class constructor
        super().__init__(container)

        # function to configure the grid
        self.rowcol()

        # get the start date
        self.start_date_label = ttk.Label(self, text='Start Date:')
        self.start_date_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

        self.start_date = DateEntry(self)
        self.start_date.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

        self.end_date_label = ttk.Label(self, text='End Date:')
        self.end_date_label.grid(column=2, row=0, padx=5, pady=5, sticky=tk.E)

        self.end_date = DateEntry(self)
        self.end_date.grid(column=3, row=0, padx=5, pady=5, sticky=tk.W)

        self.go = ttk.Button(self, text='Go', command=self.calculate_time)
        self.go.grid(column=4, row=0, padx=5, pady=5)

    # configure rows and columns
    def rowcol(self):
        col = 5
        for i in range(col):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=20)

    def calculate_time(self):
        try:
            timelog = pd.read_csv(CSV_FILE_PATH)
        except pd.errors.EmptyDataError as e:
            messagebox.showerror(
                title="Error",
                message=f"Error loading data from file...\n\nTimeLog.csv file is empty. \n\nResolutions: \
                    \n 1.Delete the TimeLog from (C:\\temp) and re-enter incidents\
                    \n 2.Contact Owen for assistance."
            )
        except FileNotFoundError:
            messagebox.showerror(
                title="Error",
                message="Timesheet file does not exist or contains no entries."
            )

        try:
            # clean data, drop unneeded columns, sort by date
            timelog['date'] = timelog['date'].astype('datetime64') # set column to datetime dtype
            timelog['time_spent'] = timelog['time_spent'].astype('int64')
            timelog = timelog[timelog.date.between(self.start_date.get(), self.end_date.get())].reset_index(drop=True) # create new temp df with only the dates required
            timelog = timelog.drop(columns=['affected_user', 'description'])
            timelog = timelog.sort_values(by=['date'])

            # create pivot table out of queried data
            timelog['location'] = timelog['location'].str.upper() # make all items uppercase so that case doesnt matter.
            table = timelog.pivot_table(index=['location'], columns=['date'], values=['time_spent'], aggfunc=sum, fill_value=0)
            # To add totals...: margins=True, margins_name='Totals'
            
            # add pivot table data to a Text widget and display it
            textvar = tk.Text(self, height=40, width=200, spacing1=5)
            textvar.insert(tk.END, table)
            textvar.grid(row=1, column=0, columnspan=5, sticky=tk.NSEW, padx=5, pady=5, ipadx=5, ipady=5)
        except KeyError:
            messagebox.showerror(
                title="Error",
                message="Error loading data from file. Headers in CSV file are not configured correctly. Contact Owen for assistance"
            )

    
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