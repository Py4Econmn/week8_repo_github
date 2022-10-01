import main 
import utils as ut

main.gen_table()
df = main.prepate_data()

for index, row in df.iterrows():

    try:
        db_name = "week8"
        table_name = "employee"
        values = (row["firstName"], row["age"], row["politicalView"])
        ut.insert_into_table(values,table_name,db_name)
        print("Add row {}.".format(index))
    except:
        print("Couldn't add new row")

print("Finished populating employee table. Done!")