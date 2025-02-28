class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"name : {self.name}")
        print(f"salary : {self.salary}")
e1=Employee("arjun",2000)
e1.display()
e2=Employee("diva",3000)
e2.display()
def combined():
    c_sal=e1.salary+e2.salary
    c_name=e1.name+" "+e2.name
    print(f"combine salary of {c_name} is {c_sal} ")
combined()
