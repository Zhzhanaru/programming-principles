# 1. Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case.
# Use init method to construct some parameters
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
# 2. Define a class named Shape and its subclass 
# Square. The Square class has an init function 
# which takes a length as argument. Both classes 
# have a area function which can print the area of 
# the shape where Shape's area is 0 by default.

# To override a method in the superclass, we can define a method with the same name in the superclass.
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print (aSquare.area())

class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    def area(self):
        return self.length**2


first = Square(3)
print(first.area())
second = Square(33)
print(second.area())
third = Shape(10)
print(third.area())

# 3. Define a class named Rectangle which inherits 
# from Shape class from task 2. Class instance can 
# be constructed by a length and width. The 
# Rectangle class has a method which can compute 
# the area.

# 4. Write the definition of a Point class. Objects 
# from this class should have a

#  a method show to display the coordinates of 
# the point
#  a method move to change these coordinates
#  a method dist that computes the distance between 
# 2 points

#distance: sqrt((x1-x0)^2+(y1-y0)^2)


# 5. Create a bank account class that has 
# attributes owner, balance and two methods 
# deposit and withdraw. Withdrawals may not 
# exceed the available balance. Instantiate 
# your class, make several deposits and 
# withdrawals, and test to make sure the 
# account can't be overdrawn.

# class Account:
#     pass

# 6. Write a program which can filter prime numbers 
# in a list by using filter function. Note: Use 
# lambda to define anonymous functions.