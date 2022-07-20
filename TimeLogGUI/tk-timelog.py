# Goal: Make a Python GUI app that can be used to track my working time and incidents.
#  - App should have options for Time (minutes), name, description, jobsite/location.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os
from turtle import st

# App class
class App(tk.Tk):
    def __init__(self): # class constructor
        super().__init__() #calls the constructor of the Tk parent class. gives us access to the methods of the superclass Tk().
    
        # background color of window
        self.BG_COLOR = "#949494"

        # Create window
        self.geometry("500x320")
        self.title("Time Log")
        self.resizable(0,0)
        self.configure(bg=self.BG_COLOR)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # create 5 rows
        for i in range(0,5):
            self.rowconfigure(i, weight=2)

        # call function to create widgets
        self.create_widgets()

    # create widgets
    def create_widgets(self):

        # set default font
        font_style = ("Helvetica", 16)

        # create string variables for holding entry
        time_spent = tk.StringVar()
        affected_user = tk.StringVar()
        description = tk.StringVar()
        location = tk.StringVar()

        # time spent label and entry
        time_spent_label = ttk.Label(self, text="Time (mins):", font=font_style, background=self.BG_COLOR)
        time_spent_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        time_spent_entry = ttk.Entry(self, textvariable=time_spent, font=font_style)
        time_spent_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        # name label and entry
        affected_user_label = ttk.Label(self, text="Affected User:", font=font_style, background=self.BG_COLOR)
        affected_user_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        affected_user_entry = ttk.Entry(self, textvariable=affected_user, font=font_style)
        affected_user_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # description label and entry
        description_label = ttk.Label(self, text="Description:", font=font_style, background=self.BG_COLOR)
        description_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        description_entry = ttk.Entry(self, textvariable=description, font=font_style)
        description_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        # location label and entry
        location_label = ttk.Label(self, text='Location:', font=font_style, background=self.BG_COLOR)
        location_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        location_entry = ttk.Entry(self, textvariable=location, font=font_style)
        location_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        # submit button
        submit_button = ttk.Button(
            self, 
            text='Submit',
            command=lambda t=time_spent, u=affected_user, d=description, l=location: self.submit(t,u,d,l)) # submit_button
        #submit_button.state(['disabled']) # button is disabled until all boxes have entries
        submit_button.grid(column=1, row=4, padx=5, pady=5)

        # view log button
        view_log = ttk.Button(self, text='View Log', state='disable')
        view_log.grid(column=0, row=4, padx=5, pady=5)
    
    # process once the submit button is pressed
    def submit(self, time, user, des, loc):
        
        # verify all fields were entered
        if(time.get() and user.get() and des.get() and loc.get()):
            self.save_to_file([time.get(), user.get(), des.get(), loc.get()])
        else:
            # if any field is blank present an error
            messagebox.showinfo(
                title='Error',
                message='All fields must be entered before submitting'
            )

    def save_to_file(self, row):
        # checking if the file exists and is empty
        if self.is_file_empty('./TimeLogGUI/timelog.csv'):
            print('File does not exist, creating and writing headers...')

            # create header arrary
            headers = ['time_spent', 'affected_user', 'description', 'location']

            # write headers to new file
            with open('./TimeLogGUI/timelog.csv', 'w', newline='') as mycsv:
                csv.writer(mycsv).writerow(headers)

        # append rows to file
        with open('./TimeLogGUI/timelog.csv', 'a', newline='') as f:
            # write row
            csv.writer(f).writerow(row)
            print('File is not empty, writing to file...')

    #function used to check if timelog file exists and is empty
    def is_file_empty(self, file_path):
        # Check if file exist and it is empty
        if os.path.exists(file_path): # does the path exist? 
            if os.stat(file_path).st_size == 0: # path exists, is it empty?
                return True # if empty return True
            else:
                return False # if not empty return false
        else:
            return True # if path does not exist return True
    



if __name__ == "__main__":
    app = App()
    app.mainloop()