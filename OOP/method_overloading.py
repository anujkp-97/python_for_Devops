class Geometry:
    
    def area(self, l, b=0):
       if b==0:
           print("Circle: ", 3.14*l*l)
       else:
           print("Rectangle: ", l*b)
           
    
# Method overloading is not supported in python as the java support so, we used method overloading like this
    
g = Geometry()
g.area(2)
g.area(2,3)

print("-- Operator overloading -- ")
# it is done in the fraction program, adding the two fraction
