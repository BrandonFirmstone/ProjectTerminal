# Project Terminal

![image](https://user-images.githubusercontent.com/83018530/133722366-7d9a553a-c52f-4c60-8e40-5cc18cf7fc6f.png)

A project management solution using Python and a command line interface.

Deployed here: https://project-terminal.herokuapp.com/

## Table of contents

Table of contents here

## Project Goals

The aim of this project is to create a text-based command line project management application. Using CSV files as the basis for storing the information, the program should be able to read, write and amend information contained within the spreadsheet. Users will be treated as admins and can run a series of tasks from the main menu where they can see the current jobs and status, update status, add new tasks and delete items or search by status or see jobs that are due. 


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

![job-example](https://user-images.githubusercontent.com/83018530/133683430-379e7ea3-720f-491a-a58d-35b37498f032.png)


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

## Demonstrations of functions
The below are videos recorded of the terminal performing different previously mentioned functions. Note how all the user input is numeric in function to reduce typos, eliminate case sensitivity issues and trailing and leading whitespace is ignored. If a user enters something outside the scope of the options, the screen options reprint.

### Help Menu

![help menu](https://user-images.githubusercontent.com/83018530/133719010-ae2cd56a-82c0-4562-a26b-14da9ac6d32a.gif)


### Search By Status

![search by status](https://user-images.githubusercontent.com/83018530/133719022-639b27cf-697f-4297-b5ca-c897e6a47228.gif)


### Print All Jobs

![see all jobs](https://user-images.githubusercontent.com/83018530/133719046-cfeb30ce-ca03-4c30-a8fc-f9d15da91a9a.gif)


### Add Job

- All jobs need to have a description. These descriptions must be between 5 and 50 characters. If the user types no information into the description, how will they know what the task represents? Over 50 characters and there may be issues with the job row wrapping onto the next line.

![add new job](https://user-images.githubusercontent.com/83018530/133719054-dc687ff7-e48f-426f-aee5-3d0244a0ea38.gif)


### View Due Jobs

![view due jobs](https://user-images.githubusercontent.com/83018530/133719066-bdabce56-b9a9-4e4b-a463-8de34ca07b20.gif)


### Delete Specific Job

![delete a job](https://user-images.githubusercontent.com/83018530/133719072-32c021b8-ec3a-48c3-8bbe-1b07892fe66e.gif)


### Update Status

![update status](https://user-images.githubusercontent.com/83018530/133719076-c0ae158c-809a-4b33-8c13-56bf5200bcd0.gif)

## Data Model
To track items that were in the CVS beter, I created a data model called Job.

### Properties
**status:** Pending - The job has been posted and not started. Ongoing - The job has been started. Complete - The job is finished. description: String 1 - 30 characters long to prevent wrapping to next line on console 
**priority:** Low, Medium or High priority. Helps the use to decide what order to do jobs
**due_date:** The date the task is due, must be in the future or equal to current date  
### Methods:
**get_status:** user input to select status from STATUSES
**get_description:** user input to set description
**get_priority:** user input to select priority from PRIORITIES
**due_date:** user input to get due date in DD/MM/YYYY format
**__init__:** function to either accept incoming values and assign to properites or create new object based on user input 
**__str__:** default string display
**to_array:** [place items into an ary based on status, description, priority, due_date]  
**to_csv:** Writes specific job to CSV file

### Validation Testing
I put my code through pep8online:

![image](https://user-images.githubusercontent.com/83018530/133721068-b55d6030-9d85-4b82-aa28-d2c31ec9632d.png)

## Deployment
### Requirements

There are no requirements in place for a user to use this program. In the future, there should be workplaces, accounts and hierarchys within the program.

To use the program locally, you will need to install the requirements using "pip3 install -r requirements.txt".

### Heroku

I deployed this project to Heroku as the Python backend language would not function correctly on Github Pages.
These are the steps I took to deploy the project to Heroku:

- Log into Heroku and create a new app.

![create a new app](https://user-images.githubusercontent.com/83018530/133721528-4fc35e13-49f1-4725-8833-cc9038285241.PNG

![create-app](https://user-images.githubusercontent.com/83018530/133721568-9e6ebc00-679b-4847-b438-16fe8b93699b.PNG)

- Then I need to add the nodejs buildpack and Python build pack to enable the app to work correctly.

![nodejs buildpack](https://user-images.githubusercontent.com/83018530/133721650-639409f9-855c-4877-a532-be6055109bf9.PNG)

![python buildpack](https://user-images.githubusercontent.com/83018530/133721653-d30b8813-79ca-4d9d-afe8-0df212ae113a.PNG)

![buildpacks after](https://user-images.githubusercontent.com/83018530/133721678-9d06bf4e-8327-40f4-9091-d90aba8d957a.PNG)

- Then, I need to set up the config vars required for the program to run.

![config vars before](https://user-images.githubusercontent.com/83018530/133721721-30f15ffa-6648-4dfc-b30d-5941ea010840.PNG)

![config vars after](https://user-images.githubusercontent.com/83018530/133721739-ceccc59a-6a58-454f-8ccd-299c82675c3c.PNG)

- Now I need to find the Repository from my Github in Heroku. This also means connecting my Github to Heroku.

![deploy-github](https://user-images.githubusercontent.com/83018530/133721833-b88e3851-55a2-41ce-8609-5f230ebf3a4b.PNG)


![deploy-find-repo](https://user-images.githubusercontent.com/83018530/133721786-c645cf44-40dc-4dec-9536-1eb5946fe5f6.PNG)

- Then I can deploy to Heroku.

![deploying](https://user-images.githubusercontent.com/83018530/133721928-f3d57b48-3999-43d0-98f3-4e3c4f6e70d5.PNG)


The deployment is now complete.


## Bugs and Testing

Bugs found while testing are in the github  issues for this repository: [defects](https://github.com/BrandonFirmstone/ProjectTerminal/issues)

Testing is documented in a Project Board in this repository [test cases](https://github.com/BrandonFirmstone/ProjectTerminal/projects/1)

## Libraries Used

- Pandas for manipulating spreadsheets
- numpy as Pandas requires this
- pytz for Pandas
- Colorama to highlight tasks due

## Constraints and other issues

- Because of the terminal's size on the heroku deployed site I cannot create text or text-based graphics with more than 80 characters per line - otherwise the text get's wrapped to the next line.
- Because of how Heroku is connected to Github, the information changed through Heroku is only temporarily saved. Heroku restarts itself and removes any local data periodically. This is because I do not know how to get Heroku to make real-time changed to the CSV file in the Github repository. I believe that even though the CSV file is in essense static, it still shows a minimum viable product and proof of concept. This could be fixed if the project was hosted to a web server or utilizing a database instead of a CSV, it could directly read and write from the file and make the changes immediately. I did not use a database because I currently do not have the knowledge to do so.
- Due to me being based in the UK, the Heroku app is hosted on a European server. This means that elsewhere in the world when they are still on the day before the UK, trying to put in a task of their current date is not allowed because it is seen as being in the past. This is not an issue at the moment because it is a minimum viable product. It shows proof of concept. In the future, there could be seperate servers for different time zones to ensure this doesn't happen.

## Flow Chart

This is a flow chart that I used to help design the program. It might be messy and a little bit difficult to read, but it shows how I tried to structure the program and the flow of logic that it took.

![program flow](https://user-images.githubusercontent.com/83018530/133726646-83113194-bb3f-4d12-81a8-d7d93cf5b48c.png)


## Acknowledgements

- Code Institute Template - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

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
