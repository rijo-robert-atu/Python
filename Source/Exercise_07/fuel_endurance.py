"""
fuel_endurance.py
By: Rijo Robert
Date: 16OCT22
"""
try:
    
  fuel = int(input("Fuel value : "))
  fuel_consumption = int(input("Fuel Consumption : "))
  endurance = fuel / fuel_consumption  
  print(f"Endurance :{endurance}")

except ZeroDivisionError as err:
  print(f"Fuel consumption can't be 0, Error : {err}"