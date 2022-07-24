import csv
import random

csv_path = "C:/Users/cpawl/Desktop/Projects/WorkTimeLog/TimeLogGUI/TimeLogGUI/timelog.csv"

names = ['Owen', 'Paul', 'Brian', 'Mack', 'Steve', 'Alison', 'Megan']
time = ['15', '30', '45', '60', '90', '120']
description = ['Computer broken', 'Phone broken', 'Outlook problem', 
                'Teams problem', 'New phone', 'New computer']
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
location = ['Volpe', 'MGH', 'Main Office', 'Beth Israel', 'WSL5', 'Comm Pier']
year = 2022

incidents = []

# get random date
def get_date():
    # get date
    d = days[random.randint(0, len(days))]
    mo = months[random.randint(0, len(months))]
    date = f"{mo}/{d}/{year}"
    return date

def get_user():
    return names[random.randint(0, len(names))]

# get random time
def get_time():
    return time[random.randint(0, len(time))]

def get_des():
    return description[random.randint(0, len(description))]

def get_loc():
    return location[random.randint(0, len(location))]

# append rows to file
with open(csv_path, 'a', newline='') as f:
    for row in incidents:
        # write row
        csv.writer(f).writerow(row)
        print('Appending to file...')

for i in range(10):
    incidents.append([get_date(), get_user(), get_time(), ])

