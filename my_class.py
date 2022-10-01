class Employee(): 

    def __init__(self, firstname, age, politicalView):
        self.firstname = firstname
        self.age = age
        self.politicalView = politicalView

    def add_me(self):
        values = (self.firstname, self.age,self.politicalView)
        insert_into_table(values, "employee", "week8")

    def delete_me(self):
        delete_from_table("firstname", self.firstname, "employee", "week8")


# readme
# update me


