import pandas as pd
import datetime, sys
from colorama import Fore
from csv import writer

all_jobs = pd.read_csv("jobs.csv")


class Jobs:


    def print_all_jobs():


        all_jobs = pd.read_csv("jobs.csv")
        print(all_jobs.to_string())
        print(" Type anything to return to main menu")
        user_selection = input()
        main_menu()


    def print_specific_jobs(self,category):


        all_jobs = pd.read_csv("jobs.csv")
        if category == "Pending" or category == "Ongoing" or category == "Complete":
            specified_tasks = all_jobs[all_jobs['Job Status'].str.match(category)]
            print(specified_tasks.to_string())
        else:
            print(" Error - Job status entered is unrecognised. \n Would you like to try again(1) or return to the main menu?(2)\n")
            user_selection = input()
            if user_selection == 1 or user_selection == "1":
                status_selector()
            else:
                main_menu()


    def create_new_job():


        all_jobs = pd.read_csv("jobs.csv")
        new_job = []
        print(" First, please enter the initial status.")
        print(" Choose from Pending, Ongoing or Complete.\n")
        user_selection = input().capitalize()
        if user_selection == "Pending" or user_selection == "Ongoing" or user_selection == "Complete":
            new_job.append(user_selection)
        else:
            print(" Error - unexpected input. You entered " + user_selection + ". Please try again.")
            Jobs.create_new_job()
        print(" Please give the job a description.\n Please keep the description short, as it may cause errors displaying it.\n")
        user_selection = input()
        print(" You have typed " + user_selection + ".\n Is this correct? Type Y for yes, N for no.\n")
        user_confirmation = input().capitalize()
        if user_confirmation == "Y":
            new_job.append(user_selection)
        else:
            Jobs.create_new_job()
        print(" Please choose a priority. Please choose from Low, Medium or High.\n")
        user_selection = input().capitalize()
        if user_selection == "Low" or user_selection == "Medium" or user_selection == "High":
            new_job.append(user_selection)
        else:
            Jobs.create_new_job()
        print(" Select a due date. This should be formatted like DD/MM/YYYY.")
        user_selection = input()
        now = datetime.datetime.now()
        check_year = int(str(user_selection[6] + user_selection[7] + user_selection[8] + user_selection[9]))
        check_month = int(str(user_selection[3] + user_selection[4]))
        current_month = now.month
        current_year = now.year
        print(check_year)
        print(check_month)
        print(now.year)
        print(now.month)
        if user_selection[0] >= "4":
            print(" Date is invalid. Please try again.")
        elif user_selection[2] != "/" or user_selection[5] != "/":
            print(" Date is invalid. Please try again.")
        elif user_selection[0] == "3" and user_selection[1] >= "1":
            print(" Day in date is greater than 31. Please try again.")
        elif check_year < current_year or (check_month < current_month and check_year == current_year):
            print(" Date is in the past.")
        else:
            new_job.append(user_selection)
        print(*new_job)
        print(" Is this correct? Please type Y for yes or N for no.\n")
        user_selection = input().capitalize()
        if user_selection == "Y":
            with open("jobs.csv", 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(new_job)
            print(" Successfully added to Jobs")
            main_menu()
        else:
            Jobs.create_new_job()
        
        
    def view_due_jobs():


        all_jobs = pd.read_csv("jobs.csv")
        now = datetime.datetime.now()
        date_formatted = now.strftime("%d/%m/%Y")
        pending_jobs = all_jobs[((all_jobs['Job Status'] == 'Pending') & (all_jobs['Job Status'] == 'Ongoing')) & (all_jobs['Due Date'] == date_formatted)]
        specified_tasks = all_jobs[all_jobs['Due Date'].str.match(date_formatted)]
        print(" Tasks due today \n")
        print(f"{Fore.RED}{specified_tasks} \033[39m \n")
        print(" Press enter to continue")
        user_selection = input()
        main_menu()
    

    def delete_specific_job():


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
            print(" Is this the row that you would like to delete?\n Type Y for Yes, N for No.")
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
    

    def update_status():


        all_jobs = pd.read_csv("jobs.csv")
        print("Showing Pending and Ongoing tasks. Please note once a Job has gone to Complete it cannot be changed.\n")
        print("Press enter to continue...\n")
        user_selection = input()
        not_completed_jobs = all_jobs[(all_jobs['Job Status'] == 'Pending') + (all_jobs['Job Status'] == 'Ongoing')]
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
                print(all_jobs[index_selected].loc[all_jobs["Job Status"] == "Pending"])
                while True:
                    if (row_to_update['Job Status'] == 'Pending').any() is True: 
                        print("Would you like to update from Pending to Ongoing or Complete?\n")
                        user_selection = input().capitalize()
                        while True:
                            if user_selection == "Pending" or user_selection == "Ongoing":
                                print(f"Updating to {user_selection}...")
                                all_jobs.set_value(index_selected, "Job Status", user_selection)
                                all_jobs.to_csv("jobs.csv", index=False)
                                print("Changes made successfully")
                                break
                            else:
                                print("Error, unexpected input. Please try again")
                        break
                    else:
                        print("Please try again.")
                        Jobs.update_status()
            else:
                print("An exception has occurred")
                Jobs.update_status()
        main_menu()


def status_selector():


    print(" Please select one of the following: \n")
    print(" Pending(1)   Ongoing(2)   Complete(3) \n")
    status_selection = input()
    options = ["Pending", "Ongoing", "Complete"]
    status_selection = int(status_selection) - 1
    Jobs.print_specific_jobs(options[status_selection])


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


    all_jobs = pd.read_csv("jobs.csv")
    print(chr(27) + "[2J")
    print("   P R O J E C T  T E R M I N A L  \n")
    print("         M A I N   M E N U         ")
    print("-----------------------------------")
    print(" Type the number next to each option \n in order to select it. \n \n")
    print(" Help(1)  Search by Status(2)    See all Jobs(3)")
    print(" Add a new Job(4)   View Jobs Due Today(5)    Delete a specific job(6)")
    print(" Update a job's Status(7)")
    print(" To exit the program, simply type 'exit'")
    user_selection = input("Select your option: \n \n")

    if user_selection == 1 or user_selection == "1":
        help_function()
    elif user_selection == 2 or user_selection == "2":
        status_selector()
    elif user_selection == 3 or user_selection == "3":
        Jobs.print_all_jobs()
    elif user_selection == 4 or user_selection == "4":
        Jobs.create_new_job()
    elif user_selection == 5 or user_selection == "5":
        Jobs.view_due_jobs()
    elif user_selection == 6 or user_selection == "6":
        Jobs.delete_specific_job()
    elif user_selection == 7 or user_selection == "7":
        Jobs.update_status()
    elif user_selection == "exit":
        print("Are you sure? Type 1 to return to the main menu, 2 to exit the program.")
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


