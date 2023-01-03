my_string = "global"

def my_function():
  my_string = "enclosing"
  def nested_function():
    my_string = "local"
  print(my_string)
  nested_function()
  return my_string
  
print(my_string)

print(my_function())