class Person:
    def __init__ (self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My Id number is {}".format(self.idnumber))

class Employee(Person):
    def __init__(self, name, idnumber, salary, designation):
        self.salary = salary
        self.designation = designation

        Person.__init__(self, name,idnumber)

    def details(self):
         print("My name is {}".format(self.name))
         print("My Id number is {}".format(self.idnumber))
         print("My salary is {}".format(self.salary))
         print("My designation is {}".format(self.designation))
class Manager(Employee):
    def __init__(self, name, idnumber, salary, designation, tenure):
        self.tenure = tenure

        Employee.__init__(self, name,idnumber, salary, designation)

    def details(self):
         print("My name is {}".format(self.name))
         print("My Id number is {}".format(self.idnumber))
         print("My salary is {}".format(self.salary))
         print("My designation is {}".format(self.designation))
         print("Tenure is {}".format(self.tenure))

        

p = Person("Anuj Pal", 2301)
p.display()
p.details()

print("--------------------------------")
e = Employee("Yogesh", 2102, 10000, "Cloud")
e.details()
print("--------------------------------")

m = Manager("Ashish",1102, 20000, "CEO", "5 year")
m.details()


  
