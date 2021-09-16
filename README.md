# Project Terminal

A project management solution using Python and a command line interface.

## Table of contents

Table of contents here

## Project Goals

The aim of this project is to create a text-based command line project management application. Using CSV files as the basis for storing the information, the program should be able to read, write and amend information contained within the spreadsheet. 


## Project Features 

Each task is made up of four pieces of information: 

- Job Status
- Job Description
- Priority
- Due Date

The statuses that the user can choose from include the following:

- Pending - The end user has not accepted or started the job yet.
- Ongoing - The user is at any point between Pending and Complete. The job is not yet finished, but it has started and is being done by the user.
- Complete - The job has been finished.

Then the user can choose a description for their job. This can be anything so long as it isn't more than 50 characters. This is to avoid wrapping onto the next line because of the following maths:

Total characters available in terminal: 80
Longest possible status in characters: 8
Longest possible priority in characters: 6
Date length in characters: 10
Rough total characters available for description: 80 - (10+8+6) = 56

So, to add some leway with the length, I reduced this down to 50 characters. Long enough for a somewhat complicated description.

The next choice for a user is the priority. This can be chosen from the following:

- Low
- Medium
- High

These are used to help the user decide what jobs to do and in what order. Knowing the importance of a job can help to make choosing what to do easier.

The final selection for the user is the due date. This is so that the user knows when the job is due for so that they can plan ahead and ensure that it is completed by that due date. The dates are in the DD/MM/YYYY format. When creating a job, the user has to type in a value that is either the same day or in the future, rather than creating a task with a due date in the past.

The below is how a task is presented to the user:



The way that new jobs are created is through a class called Job. This class includes four methods for job creation:

- get_status
- get_description
- get_priority
- due_date

When initialising a new job, the __init__ method checks that the job has each of the specific pieces of information and calls the four above methods depending on what's missing.

The job class also includes two other methods. to_array and to_csv. They do the following:

- to_array: place items into an ary based on status, description, priority, due_date
- to_csv: Writes specific job to CSV file without overwriting existing content

Then, there are 7 main functions that the user utilises to manipulate and view the date within the jobs.csv spreadsheet. These are:

- view_due_jobs: Prints all jobs that are due on today's date to the terminal. Uses Colorama to colour these in red to highlight that they are due.
- print_all_jobs: Prints all of the jobs within the jobs.csv by using Pandas to create a more user-friendly dataframe.
- print_specific_jobs: Prints all jobs of a particular status that the user chooses.
- delete_specific_job: This is used to delete a job based on it's index within the pandas dataframe. This also amends the spreadsheet to reflect this.
- update_status: This is used so that the user can keep track of their tasks. They can change the status of a specific task to whatever they need to change it to.
- help_function: This help function helps to explain to the user the different options available to them and the ways they can use the program.
- main_menu: The main_menu function is the main way the user chooses what they want to do. From here they can use any of the above functions or exit the program.


## Libraries Used

- Pandas for manipulating spreadsheets
- numpy as Pandas requires this
- pytz for Pandas
- Colorama to highlight tasks due

## Acknowledgements

- https://realpython.com/documenting-python-code/

- https://www.geeksforgeeks.org/print-colors-python-terminal/a

- https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58

- https://www.w3schools.com/python/pandas/default.asp

- https://www.w3schools.com/python/python_classes.asp

- https://realpython.com/python-pep8/#naming-conventions - Naming conventions used

- https://stackoverflow.com/questions/2084508/clear-terminal-in-python

- https://www.statology.org/pandas-to-csv-append/ 

- https://kanoki.org/2019/01/02/pandas-trick-for-the-day-color-code-columns-rows-cells-of-dataframe/

- https://thispointer.com/python-pandas-select-rows-in-dataframe-by-conditions-on-multiple-columns/

- https://www.askpython.com/python-modules/pandas/update-the-value-of-a-row-dataframe