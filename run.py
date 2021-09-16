import pandas as pd
import datetime
import sys
from colorama import Fore
from csv import writer

# Dictionary for all available job statuses - constant variable

STATUSES = {
    "1": "Pending",
    "2": "Ongoing",
    "3": "Complete"
}

# Dictionary for all available job priorities - constant variable

PRIORITIES = {
    "1": "Low",
    "2": "Medium",
    "3": "High"
}

# Dictionary for yes or no questions - constant variable

OPTIONS = {
    "1": "Yes",
    "2": "No"
}


class Job:
    """
    A class to help set up task records:
        Properties:
            status: Pending - The job has been posted and not started. Ongoing - The job has been started. Complete - The job is finished.  #  noqa
            description: String 1 - 30 characters long to prevent wrapping to next line on console  #  noqa
            priority: Low, Medium or High priority. Helps the use to decide what order to do jobs  #  noqa
            due_date: The date the task is due, must be in the future or equal to current date   #  noqa
        Methods:
            get_status: user input to select status from STATUSES
            get_description: user input to set description
            get_priority: user input to select priority from PRIORITIES
            due_date: user input to get due date in DD/MM/YYYY format
            __init__: function to either accept incoming values and assign to properites or create new object based on user input  #  noqa
            __str__: default string display
            to_array: [place items into an ary based on status, description, priority, due_date]  #  noqa
    """

    def __init__(self, status=None, description=None, priority=None, due_date=None):  # noqa
        if status and status in STATUSES:
            self.status = STATUSES[status]
        else:
            self.status = self.get_status()
        if description and len(description) <= 30 and len(description) > 0:
            self.description = description
        else:
            self.description = self.get_description()
        if priority and priority in PRIORITIES:
            self.priority = priority
        else:
            self.priority = self.get_priority()
        if due_date:
            self.due_date = due_date
        else:
            self.due_date = self.get_due_date()

    def __str__(self):
        return f"Description: %s\nStatus: %s\nPriority: %s\nDue Date: %s" % (self.description, self.status, self.priority, self.due_date)  # noqa

    def get_status(self):
        user_selection = None
        while user_selection not in STATUSES:
            for key in STATUSES:
                print(key, ' - ', STATUSES[key])
            user_selection = input(
                "What status would you like to select?\n").strip()
        return STATUSES[user_selection]

    def get_description(self):
        user_selection = None
        while user_selection is None:
            user_selection = input("Please enter a description. 30 Characters or less.\n").strip().capitalize()  # noqa
            if len(user_selection) >= 4 or len(user_selection) <= 50:
                pass
            else:
                print("Please type a valid description")
                user_selection = None
        return user_selection

    def get_priority(self):
        user_selection = None
        while user_selection not in PRIORITIES:
            for key in PRIORITIES:
                print(key, ' - ', PRIORITIES[key])
            user_selection = input("What is the priority for this job?\n").strip()  # noqa
        return PRIORITIES[user_selection]

    def get_due_date(self):
        due_date = None
        while not due_date:
            due_date = input("Please enter a due date in form dd/mm/yyyy:\n").strip()  # noqa
            try:
                dd = datetime.datetime.strptime(due_date, '%d/%m/%Y')
                if dd.date() < datetime.datetime.now().date():
                    print("Date cannot be in the past")
                    due_date = None

            except ValueError:
                print("Invalid Date Format.")
                due_date = None
        return due_date

    def to_array(self):
        return[self.status, self.description, self.priority, self.due_date]

    def to_csv(self):
        new_job = self.to_array()
        with open("jobs.csv", 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(new_job)


def view_due_jobs():
    '''
    view_due_jobs: Function to show the user all jobs due on the current date.
    Prints these jobs in red as a warning that they are due.
    '''
    all_jobs = get_all_jobs()
    now = datetime.datetime.now()
    date_formatted = now.strftime("%d/%m/%Y")
    specified_tasks = all_jobs[all_jobs['Due Date'].str.match(date_formatted)]
    print(" Tasks due or overdue \n")
    print(f"{Fore.RED}{specified_tasks} \033[39m \n")
    return_to_menu()


def print_all_jobs():
    '''
    print_all_jobs: Function to show the user in the terminal all jobs in the jobs.csv file  #  noqa
    '''
    all_jobs = get_all_jobs()
    print('####################')
    print('# PRINT ALL JOBS')
    print('####################\n')
    print(all_jobs.to_string())
    return_to_menu()


def print_specific_jobs():
    '''
    print_specific_jobs: Function to print specific jobs based upon the job status.  #  noqa
    '''
    all_jobs = get_all_jobs()
    status = None
    while status not in STATUSES:
        print("Please select a status:\n")
        for key in STATUSES:
            print(key, ' - ', STATUSES[key])
        status = input("\n").strip()
    category = STATUSES[status]
    if category == "Pending" or category == "Ongoing" or category == "Complete":  # noqa
        specified_tasks = all_jobs[all_jobs['Job Status'].str.match(category)]  # noqa
        print(specified_tasks.to_string())
    else:
        print(" Error - Job status entered is unrecognised. \n Would you like to try again?\n")  # noqa
        user_selection = yes_no_questions()
        if user_selection == "Yes":
            status_selector()
        else:
            return_to_menu()
    return_to_menu()


def delete_specific_job():
    '''
    delete_specific_job: Function to delete specific job by utilizing the job_selection function.  #  noqa
    Removes the job from the dataframe and then writes the amended dataframe over jobs.csv   #  noqa
    '''
    all_jobs = get_all_jobs()
    print('####################')
    print('DELETE JOB')
    print('####################\n')
    index_selected = job_selection()
    print(all_jobs.iloc[[index_selected]])
    print(" Is this the row that you would like to delete?\n")
    user_selection = yes_no_questions()
    if user_selection == "Yes":
        print(" Deleting row...")
        new_data = all_jobs.drop(index_selected)
        new_data.to_csv("jobs.csv", index=False)
        print(" Deleted row successfully")
        all_jobs = pd.read_csv("jobs.csv")
        print(all_jobs.to_string())
        return_to_menu()
    else:
        print("Failed to delete row.")
        return_to_menu()


def job_selection():
    '''
    job_selection: Used to display all jobs to a user and return the user's selection.     #  noqa
    Checks to ensure the user's selection is within the all_jobs dataframe.  #  noqa
    '''
    all_jobs = get_all_jobs()
    print(" Please see all jobs below:")
    print(all_jobs.to_string())
    print("\n Please select the row you want to select using the number to the far left of the row.\n")  # noqa
    user_selection = input()
    index_selected = int(user_selection)
    if (all_jobs.index == user_selection).any() is False:
        print(" Please select a valid index.")
        job_selection()
    return index_selected


def return_to_menu():
    '''
    return_to_menu: Displays a message to the user, waits for the user to press enter and runs the main_menu() function.  #  noqa
    '''
    print("Press Enter to return to the main menu.")
    input()
    main_menu()


def yes_no_questions():
    '''
    yes_no_questions: Used to return a yes or no answer from the user. Created to reduce repetition.  #  noqa
    Utilises the OPTIONS constant variable for options. Only allows the user to progress if they choose a valid option  #  noqa
    '''
    user_selection = None
    while user_selection not in OPTIONS:
        print("Please select from the following options:")
        for key in OPTIONS:
            print(key, ' - ', OPTIONS[key])
        user_selection = input("\n").strip()
    return OPTIONS[user_selection]


def update_status():
    '''
    update_status: Utilizes the job_selection function to select a specific job and then updates the status based on the STATUSES constant variable.  #  noqa
    Makes the change in the all_jobs dataframe and then writes over the jobs.csv file using the amended dataframe.  #  noqa
    '''
    all_jobs = get_all_jobs()
    job_index = job_selection()
    user_selection = None
    while user_selection not in STATUSES:
        for key in STATUSES:
            print(key, ' - ', STATUSES[key])
        user_selection = input("What status would you like to select?\n").strip()  # noqa
    all_jobs.at[job_index, 'Job Status'] = STATUSES[user_selection]  # noqa
    all_jobs.to_csv('jobs.csv', index=False)
    return_to_menu()


def help_function():
    '''
    help_function: Used to display information to the user regarding how the program works and its use.  #  noqa
    '''
    print(chr(27) + "[2J")
    print("####################")
    print("HELP MENU")
    print("####################\n")
    print(" Project Terminal is a project management application.\n This software is designed to help you keep track of what tasks need to be completed.")  # noqa
    print(" Occasionally you will be asked for input.\n Typically, the software is looking for either a number correlating to an option on the screen or for a keyword such as 'Pending'.")  # noqa
    print(" On the main menu, the options presented to you will do the following:")  # noqa
    print("\n 1 - Bring up this helpful menu explaining the program.")  # noqa
    print("\n 2 - Search by status. You can find Jobs that are Pending, Ongoing or Complete specifically.\n The software presents these in a tidy table for you to use.")  # noqa
    print("\n 3 - See all Jobs. From here, you can see every job that has been created.")  # noqa
    print("\n 4 - Add a new Job. Here, you can follow the instructions to create a new Job. Please be aware that dates are in the UK format ie DD/MM/YYYY.")  # noqa
    print("Press enter to continue to the next page.")
    input()
    print(chr(27) + "[2J")
    print(" 5 - View all the jobs that are due today.")
    print("\n 6 - Delete a specific job from all jobs. This can be used to clear out old Complete jobs or delete any job for any reason.")  # noqa
    print("\n 7 - Update the status of any specific job. This is used to progress a job from Pending to Ongoing, Ongoing to Complete. You can revert a job to previous statuses if need be.")  # noqa
    print("\n 0 - Close the program. This ends the program in the terminal. \n")
    return_to_menu()


def get_all_jobs():
    '''
    get_all_jobs: Function to return a dataframe from the jobs.csv file.
    This is used very regularly to ensure that the user is always utilizing the most recent and up to date version of the file.  #  noqa
    This ensures no erroneous changes from differences between what the user sees and what's actually in the csv.  #  noqa
    '''
    all_jobs = pd.read_csv("jobs.csv")
    return all_jobs


def main_menu():
    '''
    main_menu: Displays the main menu to the user using a constant variable called MENUS.  #  noqa
    Then based on user decision directs them to the function or functions they need to use.  #  noqa
    '''
    MENUS = {
        "1": "Help",
        "2": "Search By Status",
        "3": "See All Jobs",
        "4": "Add New Job",
        "5": "View Due Jobs",
        "6": "Delete a Job",
        "7": "Update Status",
        "0": "exit",
    }
    print(chr(27) + "[2J")
    print("########################################")
    print("           M A I N   M E N U         ")
    print("########################################")
    user_selection = None
    while user_selection not in MENUS:
        for key in MENUS:
            print(key, ' - ', MENUS[key])
        user_selection = input("What would you like to do?\n").strip()  # noqa
    if user_selection == 1 or user_selection == "1":
        help_function()
    elif user_selection == 2 or user_selection == "2":
        print_specific_jobs()
    elif user_selection == 3 or user_selection == "3":
        print_all_jobs()
    elif user_selection == 4 or user_selection == "4":
        new_job = Job()
        new_job.to_csv()
    elif user_selection == 5 or user_selection == "5":
        view_due_jobs()
    elif user_selection == 6 or user_selection == "6":
        delete_specific_job()
    elif user_selection == 7 or user_selection == "7":
        update_status()
    elif user_selection == 0:
        print("Are you sure you would like to exit?")
        answer = yes_no_questions()
        if answer == "Yes":
            print("Thank you for using Project Terminal! Goodbye!")
            sys.exit(0)
        else:
            return_to_menu()


print("###############################\n")
print("P R O J E C T \nT E R M I N A L\n")
print("###############################")
while True:
    main_menu()
