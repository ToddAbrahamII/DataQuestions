#Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments.
#Output just the absolute difference in salaries.

#Table 1: db_employee
# id:int
# first_name:varchar
# last_name:varchar
# salary:int
# department_id:int

#Table 2: db_dept
# id:int
# department:varchar

#import libraries
import pandas as pd

#Solution
#Join the tables together
merge_df = pd.merge(db_employee, db_dept, left_on="department_id", right_on="id")
#Selects the department of engineering
eng_df = merge_df[merge_df["department"] == "engineering"]

#Finds the max salary in engineering
max_eng_df = eng_df[eng_df["salary"] == eng_df["salary"].max()]
eng_val = max_eng_df["salary"].reset_index(name="eng_salary")

#Select the department of marketing
mkt_df = merge_df[merge_df["department"] == "marketing"]

#Find the max salary in marketing
max_mkt_df = mkt_df[mkt_df["salary"] == mkt_df["salary"].max()]
mkt_val = max_mkt_df["salary"].reset_index(name="mkt_salary")

#Calculate the difference  and returns absolute value
salary_difference = abs(pd.DataFrame(eng_val["eng_salary"] - mkt_val["mkt_salary"]))

#formats column
salary_difference.columns = ["salary_difference"]
#Result
result = salary_difference