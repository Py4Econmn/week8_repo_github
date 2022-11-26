import utils as ut

class Employee(): 

    def __init__(self, firstname, age=None, politicalView=None):
        self.firstname = firstname
        self.age = age
        self.politicalView = politicalView

    ## CRUD operations - create, read, update, delete API 
    def add_me(self): 
        values = (self.firstname, self.age,self.politicalView)
        ut.insert_into_table(values, "employee", "week8")

    def delete_me(self):
        ut.delete_from_table("firstname", self.firstname, "employee", "week8")
    
    def read_me(self):
        df = ut.read_table("firstname", self.firstname, "employee", "week8")
        print(df)

    def update_me(self,set_key, set_value):
        ut.update_table(set_key, set_value, 'firstname', self.__dict__['firstname'], "employee", "week8")





