# This script is used to populate the csv with random events

import csv
import random

csv_path = "./TimeLogGUI/timelog.csv"

names = ['Owen', 'Paul', 'Brian', 'Mack', 'Steve', 'Alison', 'Megan',
        'Corey', 'Tyler', 'Amanda', 'Rebecca', 'Katie', 'Lauren']

time = ['15', '30', '45', '60', '90', '120']

description = ['Computer broken', 'Phone broken', 'Outlook problem', 
                'Teams problem', 'New phone', 'New computer', 'Information Request',
                'Purchase new laptop', 'Purchase new phone', 'Purchase printer',
                'Replace printer toner', 'Excel issue', 'OneDrive issue']

days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

location = ['Volpe', 'MGH', 'Main Office', 'Beth Israel', 'WSL5', 'Comm Pier', 'Amazon',
            'SPD', 'SPO', 'Marketing', 'Accounting']
year = 2022

incidents = []

# get random date
def get_date():
    # get date
    d = days[random.randint(0, len(days)-1)]
    mo = months[random.randint(0, len(months)-1)]
    if mo == '2' and (d == '30' or d == '29'):
        d = '28'
    date = f"{mo}/{d}/{year}"
    return date

def get_user():
    return names[random.randint(0, len(names)-1)]

# get random time
def get_time():
    return time[random.randint(0, len(time)-1)]

def get_des():
    return description[random.randint(0, len(description)-1)]

def get_loc():
    return location[random.randint(0, len(location)-1)]

# append rows to file
with open(csv_path, 'a', newline='') as f:
    for row in incidents:
        # write row
        csv.writer(f).writerow(row)
        print('Appending to file...')

# create new events and add them to an array
for i in range(100):
    incidents.append([get_date(), get_time(), get_user(), get_des(), get_loc()])

with open(csv_path, 'a', newline='') as f:
    for i in range(len(incidents)):
        # write row
        csv.writer(f).writerow(incidents[i])
        #print('Appending to file...')

