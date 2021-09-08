import pandas as pd
all_jobs = pd.read_csv("jobs.csv")
class Jobs:

    def print_all_jobs():
        print(all_jobs.to_string())

    def print_specific_jobs(category):
        if category == "Pending" or category == "Ongoing" or category == "Complete":
            pending_tasks = all_jobs[all_jobs['Job Status'].str.match(category)]
            print(pending_tasks.to_string())

def main_menu():
    print(chr(27) + "[2J")
    print("         M A I N   M E N U         ")
    print("-----------------------------------")
    print("Type the number next to each option \n in order to select it. \n \n")
    print("Help(1)  Search by Status(2)    See all Jobs(3)")
    user_selection = input("Select your option: \n \n")
    if user_selection == 1 or user_selection == "1":
        print("Main menu help")
    elif user_selection == 2 or user_selection == "2":
        print("Please select one of the following: \n")
        print("Pending(1)   Ongoing(2)   Complete(3) \n")
        status_selection = input()
        options = ["Pending","Ongoing","Complete"]
        status_selection = int(status_selection) - 1
        Jobs.print_specific_jobs(options[status_selection])

main_menu()
Jobs.print_all_jobs()
user_selection = input("Select job status")
Jobs.print_specific_jobs(user_selection)
