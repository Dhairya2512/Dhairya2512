class employee:

    def __init__ (self,name,designation):
        self.name=name
        self.designation=designation

class subclass(employee):

    def __init__ (self,name,designation,salary):
        print("Name : ",name," Designation : ",designation," Salary : ",salary)

c=subclass("Dhairya","Web Developer","25000")