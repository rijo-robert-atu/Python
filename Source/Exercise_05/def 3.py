def calculate_circumference(radius):
   """
   Calculate the circumference of a circle based on its radius 
   """
   return 2 * 3.14 * radius

# get a radius value as a string
r = input("Provide a radius value:")
# convert it to a float
r_float = float(r)
# Call the function and create the variable for the rturn value
a = calculate_circumference(r_float)
print(a)