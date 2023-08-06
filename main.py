## Import and upload data to database

## import packages
import pandas as pd
import os
import sys
import utils as ut

def gen_table():
    ### Create table
    qr = "CREATE TABLE IF NOT EXISTS employee (id serial PRIMARY KEY, \
            firstname text NOT NULL, \
            age INT, \
            politicalView text);"
    db = "week8"

    ut.create_table(qr, db)
    print("Created employee table.")


def prepate_data(ready_data=True):
    print("Data preparation starting ...") 

    if ready_data == True:
        main_dir = r"D:\Documents\python\repo\Introduction_Python"
        # sys.path.append(r"D:\Documents\python\repo\week8_repo") # add folder to path

        ### IMPORT
        df = pd.read_excel(main_dir + os.sep + "3_Data_table\data\data.xlsx")

        print("Imported excel data.")
    else: 
        df = ut.gen_data()

        print("Created a random data.")



    return df