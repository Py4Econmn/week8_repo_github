## Import and upload data to database

## import packages
import pandas as pd
import os
import sys
from my_class import Employee


print("Starting ...") 

main_dir = r"D:\Documents\python\repo\Introduction_Python"


sys.path.append(r"D:\Documents\python\repo\week8_repo") # add folder to path

import utils as ut

### Create table
qr = "CREATE TABLE employee (id serial PRIMARY KEY, \
        firstname text NOT NULL, \
        age INT, \
        politicalView text);"
db = "week8"

ut.create_table(qr, db)

print("Created employee table.")

### IMPORT
df = pd.read_excel(main_dir + os.sep + "3_Data_table\data\data.xlsx")

for index, row in df.iterrows():

    try:
        db_name = "week8"
        table_name = "employee"
        values = (row["id"], row["firstName"], row["age"], row["politicalView"])
        ut.insert_into_table(values,table_name,db_name)
        print("Add row {}.".format(index))
    except:
        print("Couldn't add new row")

print("Finished populating employee table. Done!")


Suren = Employee(11, 'Suren', 15, 'right')
Suren.add_me()
Suren.delete_me()



db_name = "week8"
table_name = "employee"

delete_from_table("firstname","Kherlen", table_name, db_name)


