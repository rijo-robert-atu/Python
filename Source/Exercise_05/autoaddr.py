def auto_adder(*my_number):
  final_number = 0
  for number in my_number:
    final_number = final_number + number
  return final_number
  
print(auto_adder(12,34,23,66,8,99))