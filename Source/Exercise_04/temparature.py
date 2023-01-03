conversion_Celsius = -273.15
conversion_Fahrenheit = -459.67

kelvin = [70, 160, 253, 388, 100, 50, 600, 35, 60, 99]
print(f"below are the Celsius values equivalent to kelvin")
for item in kelvin:
  Celsius = conversion_Celsius + item
    
  print(Celsius)

  
print(f"below are the Fahrenheit values equivalent to kelvin")
for item in kelvin:
  Fahrenheit = (item * 1.8) + conversion_Fahrenheit
    
  print(Fahrenheit)