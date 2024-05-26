class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    # def __init__(self, name):
    #     self.name = name


def greet(customer):
    print(id(customer))
    if customer.gender == "Male":
      print("Hello,", customer.name, "Sir")
    else:
        print("Hello,", customer.name, "Mam")

     

cust = Customer("Anuj", "Female")
# print(cust.name)

print(id(cust))
greet(cust)