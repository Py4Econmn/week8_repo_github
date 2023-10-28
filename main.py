from employee_class import Employee
import utils as ut

# Make sure week8 database exists
ut.gen_table()
df = ut.prepate_data(ready_data=False)

# Database CRUD operations in Python
# CREATE
for index, row in df.iterrows():

    try:
        Person = Employee(row["firstName"], row["age"], row["politicalView"])
        Person.add_me()
        print("Add row {}.".format(index))
    except:
        print("Couldn't add new row")

print("Finished populating employee table with random data. Done!")


df1 = ut.prepate_data(ready_data=True)

for index, row in df1.iterrows():

    try:
        Person = Employee(row["firstName"], row["age"], row["politicalView"])
        Person.add_me()
        print("Add row {}.".format(index))
    except:
        print("Couldn't add new row")

print("Finished populating employee table with excel data. Done!")

# single add
Bold = Employee("Bold", "27", "left")
Bold.add_me()
print("Add row {}.".format("Bold"))

# Other CRUD operations
# READ
Chimgee = Employee("Chimeg")
Chimgee.read_me() #

# UPDATE
Kherlen = Employee("Kherlen")
Kherlen.update_me('age',32) 

Kheegii = Employee("Kherlen")
Kheegii.read_me() #

# DELETE
Kherlen.delete_me()