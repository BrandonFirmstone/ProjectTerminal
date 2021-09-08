import pandas as pd
all_jobs = pd.read_csv("jobs.csv")
class Jobs:
    def __init__(self, all_jobs):
        self.all_jobs = all_jobs

    def print_all_jobs():
        print(all_jobs.to_string())

    def print_specific_jobs(category):
        if category == "Pending":
            pending_tasks = all_jobs[all_jobs['Job Status'].str.match('Pending')]
            print(pending_tasks.to_string())

Jobs.print_all_jobs()
Jobs.print_specific_jobs("Pending")