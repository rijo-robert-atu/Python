"""
Class template by Rijo
Revision History
30OOCT22: Alpha
"""
class MyTemplate():

# Constructor, called whenever an instance of the class is created.
 def __init__(self, attribute1: str, attribute2: bool) -> None:
  print("Constructor ran")
 # Take in an argument and assign it to a meaningful attribute name
  self.attr1 = attribute1
  self.attr2 = attribute2
 
 # Instantiate the class
my_object = MyTemplate("John", True)


print(my_object.attr1)
print(my_object.attr2)
# Check the object and type
print(type(my_object))