#Find the Highest Paid Salary of Job Titles From the Following Tables

#Table 1:
#Worker
#worker_id: int
# first_name:varchar
# last_name:varchar
# salary:int
# joining_date:datetime
# department:varchar

#Table 2:
#Title
# worker_ref_id:int
# worker_title:varchar
# affected_from:datetime

#Library Imports
import pandas as pd
import numpy as np

#Solution
#Renames the columns, aligns column names for the merge
title_worker_id = title.rename(columns={"worker_ref_id": "worker_id"}) 

#Merges the tables together
merged_df = pd.merge(worker, title_worker_id, on="worker_id")

#Matches the max salary, fines the title of that match and renames it
max_salary = merged_df[merged_df["salary"] == merged_df["salary"].max()][
    ["worker_title"]
].rename(columns={"worker_title": "best_paid_title"})

#Stores the result
result = max_salary


