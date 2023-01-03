def double_number(n:int)->int:
   """
   simple function to double a number
   """
  
my_number = [1,2,3,4,5]
result = map(double_number, my_number)
print(list(result))
for item in map(double_number, my_number):
  print(item)