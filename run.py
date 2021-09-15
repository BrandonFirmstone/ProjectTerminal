import pandas as pd
import datetime
import sys
from colorama import Fore
from csv import writer

all_jobs = pd.read_csv("jobs.csv")
STATUSES = {
    "1": "Pending",
    "2": "Ongoing",
    "3": "Complete"
}

PRIORITIES = {
    "1": "Low",
    "2": "Medium",
    "3": "High"
}

class Job:
    """
    A class to help set up task records:
        Properties:
            status: Pending - The job has been posted and not started. Ongoing - The job has been started. Complete - The job is finished. 
            description: String 1 - 30 characters long to prevent wrapping to next line on console
            priority: Low, Medium or High priority. Helps the use to decide what order to do jobs
            due_date: The date the task is due, must be in the future or equal to current date
        Methods:
            get_status: user input to select status from STATUSES
            get_description: user input to set description
            get_priority: user input to select priority from PRIORITIES
            due_date: user input to get due date in DD/MM/YYYY format
            __init__: function to either accept incoming values and assign to properites or create new object based on user input
            __str__: default string display
            to_array: [place items into an ary based on status, description, priority, due_date]
    """
    def __init__(self, status=None, description=None, priority=None, due_date=None):
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
        return f"Description: %s\nStatus: %s\nPriority: %s\nDue Date: %s" % (self.description, self.status, self.priority, self.due_date)

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
            user_selection = input("Please enter a description. 30 Characters or less.\n").strip().capitalize()
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
            user_selection = input("What is the priority for this job?\n").strip()
        return PRIORITIES[user_selection]

    def get_due_date(self):
        due_date = None
        while not due_date:
            due_date = input("Please enter a due date in form dd/mm/yyyy:\n").strip()
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

class SearchAndDestroy:

    def print_all_jobs(self):

        all_jobs = pd.read_csv("jobs.csv")
        print(all_jobs.to_string())
        print(" Type anything to return to main menu")
        user_selection = input()
        main_menu()

    def print_specific_jobs(self, category):

        all_jobs = pd.read_csv("jobs.csv")
        if category == "Pending" or category == "Ongoing" or category == "Complete":
            specified_tasks = all_jobs[all_jobs['Job Status'].str.match(
                category)]
            print(specified_tasks.to_string())
        else:
            print(" Error - Job status entered is unrecognised. \n Would you like to try again(1) or return to the main menu?(2)\n")
            user_selection = input()
            if user_selection == 1 or user_selection == "1":
                status_selector()
            else:
                main_menu()

    def delete_specific_job(self):

        all_jobs = pd.read_csv("jobs.csv")
        print(" Please see all jobs below:")
        print(all_jobs.to_string())
        print("\n Please select the row you want to delete using the number to the far left of the row.\n")
        user_selection = input()
        index_selected = int(user_selection)
        if (all_jobs.index == user_selection).any() is False:
            print(" Please select a valid index.")
            main_menu()
        else:
            print(all_jobs.iloc[[index_selected]])
            print(
                " Is this the row that you would like to delete?\n Type Y for Yes, N for No.")
            user_selection = input().capitalize()
            if user_selection == "Y":
                print(" Deleting row...")
                new_data = all_jobs.drop(index_selected)
                new_data.to_csv("jobs.csv", index=False)
                print(" Deleted row successfully")
                all_jobs = pd.read_csv("jobs.csv")
                print(all_jobs.to_string())
                print("Press enter to continue")
                user_selection = input()
                main_menu()
            else:
                print("Failed to delete row. Press enter to go to main menu")
                user_selection = input()
                main_menu()

    def update_status(self):

        all_jobs = pd.read_csv("jobs.csv")
        print("Showing Pending and Ongoing tasks. Please note once a Job has gone to Complete it cannot be changed.\n")
        print("Press enter to continue...\n")
        user_selection = input()
        not_completed_jobs = all_jobs[(
            all_jobs['Job Status'] == 'Pending') + (all_jobs['Job Status'] == 'Ongoing')]
        print(not_completed_jobs)
        print("Press enter to continue...\n")
        user_selection = input()
        print("Please select a job you would like to update by using the index on the far left of each row.")
        user_selection = input()
        index_selected = int(user_selection)
        if (all_jobs.index == user_selection).any() is False:
            print("Please select a valid index.")
            Jobs.update_status()
        else:
            print(all_jobs.loc[[index_selected]])
            print("Is this the job you would like to update? Type Y for yes, N for No")
            user_selection = input().capitalize()
            if user_selection == "Y":
                print("Y accepted")
                row_to_update = all_jobs.iloc[[index_selected]]
                print(row_to_update)
                print()
                while True:
                    if "Pending" in row_to_update.values:
                        print(
                            "Would you like to update from Pending to Ongoing or Complete?\n")
                        user_selection = input().capitalize()
                        while True:
                            if user_selection == "Ongoing" or user_selection == "Complete":
                                print(f"Updating to {user_selection}...")
                                all_jobs.set_value(
                                    index_selected, "Job Status", user_selection)
                                all_jobs.to_csv("jobs.csv", index=False)
                                print("Changes made successfully")
                                break
                            else:
                                print("Error, unexpected input. Please try again")
                        break
                    else:
                        print("Update status to Complete? Y/N")
                        user_selection = input()
                        if user_selection == "Y":
                            print("Updating to complete..")
                            all_jobs.set_value(
                                index_selected, "Job Status", "Complete")
                            all_jobs.to_csv("jobs.csv", index=False)
                        else:
                            print("Cancelling operation")
                            break
            else:
                print("An exception has occurred")
                jobs.update_status()
        main_menu()


def status_selector():
    jobs = Jobs()
    print(" Please select one of the following: \n")
    print(" Pending(1)   Ongoing(2)   Complete(3) \n")
    status_selection = input()
    options = ["Pending", "Ongoing", "Complete"]
    status_selection = int(status_selection) - 1
    jobs.print_specific_jobs(options[status_selection])


def help_function():

    print(chr(27) + "[2J")
    print("              H E L P              ")
    print("-----------------------------------")
    print(" Project Terminal is a project management application.\n This software is designed to help you keep track of what tasks need to be completed.")
    print(" Occasionally you will be asked for input.\n Typically, the software is looking for either a number correlating to an option on the screen or for a keyword such as 'Pending'.")
    print(" On the main menu, the options presented to you will do the following:")
    print("\n 1 - Bring up this helpful menu explaining the program.")
    print("\n 2 - Search by status. You can find Jobs that are Pending, Ongoing or Complete specifically.\n The software presents these in a tidy table for you to use.")
    print("\n 3 - See all Jobs. From here, you can see every job that has been created.")
    print("\n 4 - Add a new Job. Here, you can follow the instructions to create a new Job. Please be aware that dates are in the UK format ie DD/MM/YYYY.")
    print("Press any key to return to the main menu.")
    user_selection = input()
    main_menu()


def main_menu():
    MENUS = {
        "1": "Help",
        "2": "Search By Status",
        "3": "See All Jobs",
        "4": "Add New Job",
        "5": "View Jobs by Due Date",
        "6": "Delete a Job",
        "7": "Update Status",
        "0": "exit",
    }
    jobs = Jobs()
    all_jobs = pd.read_csv("jobs.csv")
    print(chr(27) + "[2J")
    print("   P R O J E C T  T E R M I N A L  \n")
    print("         M A I N   M E N U         ")
    print("-----------------------------------")
    user_selection = None
    while user_selection not in MENUS:
        for key in MENUS:
            print(key, ' - ', MENUS[key])
        user_selection = input("What would you like to do?\n").strip()
    if user_selection == 1 or user_selection == "1":
        help_function()
    elif user_selection == 2 or user_selection == "2":
        status_selector()
    elif user_selection == 3 or user_selection == "3":
        jobs.print_all_jobs()
    elif user_selection == 4 or user_selection == "4":
        jobs.create_new_job()
    elif user_selection == 5 or user_selection == "5":
        jobs.view_due_jobs()
    elif user_selection == 6 or user_selection == "6":
        jobs.delete_specific_job()
    elif user_selection == 7 or user_selection == "7":
        jobs.update_status()
    elif user_selection == "exit":
        print("Are you sure? Type 1 to return to the main menu, 2 to exit the program.")  # noqa
        user_selection = input()
        if user_selection == "1":
            main_menu()
        elif user_selection == "2":
            print("Thank you for using Project Terminal! Goodbye!")
            sys.exit(0)
        else:
            print("Unexpected input, returning to main menu.")
            main_menu()


while True:
    main_menu()
