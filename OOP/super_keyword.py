class Phone:

    def __init__(self, price, brand, model):
        self.price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a Phone")

class Smartphone(Phone):

    def buy(self):
        print("Buying a Smartphone")
        super().buy()    # access the parent class method or constructor



s = Smartphone(10000, "Moto", 2023)
s.buy()
print(s.model, s.brand)
