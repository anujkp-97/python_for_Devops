class Phone:

    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

        print("Inside the Phone constructor")

    def buy(self):
        print("Buying a Phone")
    

class Smartphone(Phone):

    def buy(self):
        print("Buying a smartphone")
class Samsung:

    def buy(self):
        print("You are buying a Samsung smart phone")


s = Smartphone(2000, "Moto", "50 MP")
s.buy()

p = Phone(2000, "Samsung", "12 MP")
p.buy()

ss = Samsung()
ss.buy()