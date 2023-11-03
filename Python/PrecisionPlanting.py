import pandas as pd

#Load the CSV file into a DataFrame
df = pd.read_csv('/Python/Users-Table 1.csv')

#Check if the DataFrame has at least 1000 rows
if len(df) >= 1000:
    
    # Update the "User_id" column for rows 101 to 1000
    df.loc[100:1000, 'User_ID'] = range(101, 1001)

    # Save the updated DataFrame back to a new CSV file
    df.to_csv('Users-Table-Updated.csv', index=False)

    print("User_ID column updated for rows 101 to 1000.")
else:
    print("The DataFrame doesn't have enough rows for the update.")

