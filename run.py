import pandas as pd
all_jobs = pd.read_csv("jobs.csv")
class Jobs:

    def print_all_jobs():
        print(all_jobs.to_string())
        print("Type anything to return to main menu")
        user_selection = input()
        main_menu()

    def print_specific_jobs(category):
        if category == "Pending" or category == "Ongoing" or category == "Complete":
            pending_tasks = all_jobs[all_jobs['Job Status'].str.match(category)]
            print(pending_tasks.to_string())
        else:
            print("Error - Job status entered is unrecognised. \n Would you like to try again(1) or return to the main menu?(2)\n")
            user_selection = input()
            if user_selection == 1 or user_selection == "1":
                status_selector()
            else:
                main_menu()
        
def status_selector():
    print("Please select one of the following: \n")
    print("Pending(1)   Ongoing(2)   Complete(3) \n")
    status_selection = input()
    options = ["Pending","Ongoing","Complete"]
    status_selection = int(status_selection) - 1
    Jobs.print_specific_jobs(options[status_selection])           

def main_menu():
    print(chr(27) + "[2J")
    print("         M A I N   M E N U         ")
    print("-----------------------------------")
    print("Type the number next to each option \n in order to select it. \n \n")
    print("Help(1)  Search by Status(2)    See all Jobs(3)    Add a new Job(4)")
    user_selection = input("Select your option: \n \n")
    if user_selection == 1 or user_selection == "1":
        print("Main menu help")
    elif user_selection == 2 or user_selection == "2":
        status_selector()
    elif user_selection == 3 or user_selection == "3":
        Jobs.print_all_jobs()
    elif user_selection == 4 or user_selection == "4":
        Jobs.create_new_job()

main_menu()
Jobs.print_all_jobs()
user_selection = input("Select job status")
Jobs.print_specific_jobs(user_selection)
