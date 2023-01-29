# TimeLogGUI


## What is it?

This desktop GUI application was built using Python 3.10.5 and the Tkinter library. It's purpose is to track the amount of time spent on resolving service requests and incidents during my time as an Information Systems Engineer at Turner Construction.

## Why is it useful?

My responsibilities as an Information Systems Engineer require me to assist users across multiple jobsites, cities, and states. Whenever I spend time working with a user or working on a specific jobsite I need to track what I did and how much time I spent. When I submit my bi-weekly timesheet all this time must be input so that each respective location is charged for the amount of work I completed.

Before I created this application it was quite difficult to find an efficient method of tracking the time I spent servicing a specific location over the course of two weeks. The two methods I used before this were handwriting in a notebook and keeping a running Excel document. Neither proved effective as I found myself spending nearly two hours every day timesheets were due going through my logs and calculating all my time. After the development of this tool I can gladly say I only spend ten to fifteen minutes completing my timesheet. This tool decreased the amount of time I spent completing my timesheet by over 85%!! Most of the hard work is now done for me. Now all I have to do is input each service request and incident into the TimeLogGUI so the data can be saved and referred to later.


## How does it work?

Upon launching the executable located at `/TimeLogGUI/TimeLogGUI/dist/TimeLogGUI` the below window appears.

![image](https://user-images.githubusercontent.com/22778729/191253811-8eabbc6d-e89f-406d-94b6-e01b09e5c65e.png)

- ***Date*** - the date field contains a drop down menu which displays a calendar. I select the day in which the particular service event takes place.
- ***Time (mins)*** - the time spent, in minutes, on the request.
- ***Affected User*** - the name of the user I spent the time helping.
- ***Description*** - a brief summary of the work performed.
- ***Location*** - the jobsite the affected user is located (EX: Jobsite A, Jobsite B, etc.).

All of this data is saved in a CSV file in the `C:\Temp` directory of my Windows 10 machine.

Clicking the ***View Log*** button opens a new windows that displays all submitted events in a tabular format.

![image](https://user-images.githubusercontent.com/22778729/191296862-6c6b8290-df32-444c-993e-f75616052493.png)

Clicking the ***Timesheet*** button opens a window that prompts you for a start date and end date. The window will then display the sum time spent for each job, arranging them in a pivot table with the location on the Y-axis and the date on the X-axis.

![image](https://user-images.githubusercontent.com/22778729/191297320-d3dce909-1b12-4974-9881-9debcfb53733.png)

With all of this information available to me I can complete my timesheet with ease and save myself a lot of time!

## How can this application be improved?

The first thing I would improve is the way each event is saved. In this version each service event is saved to a .csv file that is saved in the `C:\Temp` folder. This is not an ideal way to store data and can become an issue in many different ways. The file could be deleted or the data can be skewed if the user includes a comma in any of the fields. I am working towards creating an updated version of this tool that uses `sqlite3` to store data instead of the current method.

Alongside the implementation of storing events using SQL, I aim to add a feature that allows me to edit events or delete events after they are submitted. Currently the only way to do this is to open the csv file and edit/remove directly. This is inefficent and unsafe for many reasons and can cause more problems than it would solve.

Finally, I am attempting to build the next version of this application using PyQt6 instead of Tkinter. Tkinter is a dated library and PyQt6 provides many more GUI features that could be useful. Learning development with Qt would be far more beneficial for someone learning software development and engineering, and can also be translated into C++ which is the native Qt language.


