# collection of objects

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print("I am", self.name, "and I am", self.age)

e1 = Employee("Anuj", 23)
# print(e1.name, e1.age)
e2 = Employee("Ritik", 34)
e3 = Employee("Mhesh", 45)

L = [e1,e2,e3]
# for i in L:
#     print(i.name, i.age)
for i in L:
    i.intro()