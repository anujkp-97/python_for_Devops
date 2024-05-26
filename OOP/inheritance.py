class Animal:
    def speak(self):
        print("Animal barking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")
class Cat(Dog):
    def miyau(self):
        print("Cat miau")
class dangerous(Cat, Dog):
    def dang(self):
        print("Dog and Cat are dangerous to human life.")
    def speak(self):
        print("Cat and Dog speak different languages")

d = Dog()
d.bark()
d.speak()
print("------------------------")
c = Cat()
c.bark()
c.miyau()
c.speak()

print("-------------------------")
da = dangerous()
da.dang()
da.speak()