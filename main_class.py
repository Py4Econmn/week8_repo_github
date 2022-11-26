from my_class import Employee
import main 

main.gen_table()
df = main.prepate_data()

for index, row in df.iterrows():

    try:
        Person = Employee(row["firstName"], row["age"], row["politicalView"])
        Person.add_me()
        print("Add row {}.".format(index))
    except:
        print("Couldn't add new row")

print("Finished populating employee table. Done!")


# Other CRUD operations

# READ
Chimgee = Employee("Chimeg")
Chimgee.read_me() #

# UPDATE
Kherlen = Employee("Kherlen")
Kherlen.update_me('age',32) 

# DELETE
Kherlen.delete_me()