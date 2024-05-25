class Car:
    def __init__(self, modelname, year, type):
        self.modelname = modelname
        self.year = year
        self.type = type

    def display(self):
        print(self.modelname, self.year, self.type)


c1= Car("G-Wagon |", 2023, "| Petrol")
c2 = Car("Audi |", 2020, "| Diesel")
c1.display()
c2.display()