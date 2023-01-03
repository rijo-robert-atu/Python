"""
Simple Class by RIJO, by convention, use camel case to name classes
"""
# Create a class
from msilib.schema import Class


class RijoClass():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
  print("Running constructor for RijoClass")
 # Create attributes and set initial values
  self.message = my_greeting
 def my_method(self):
  print(self.message)
my_class1 = RijoClass("Morning Rijo!")
my_class1.my_method()
print(type(my_class1))

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

Class2 = Person("Rijo", 28)

print(Class2.name)
print(Class2.age)
print(type(Class2))
