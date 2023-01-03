"""
directory_utilities.py
By: Rijo Robert
Date: 16OCT22
"""
import os, platform
# Define global variables
current_working_directory = None
def detect_os()->str:
 # Detect the OS in use
 return platform.system()
def detect_working_directory()->str:
 # Returns the directory this script was run from
 return os.getcwd()
if (__name__ == '__main__'):
 print(f"This module executes as a standalone script")

 # Check the OS in use, lower case
 my_os = detect_os()
 my_os = my_os.lower()

 # Parse the response, only check for Windows and Linux
 if my_os == "windows":
   print("Your system is Windows")
 elif my_os == "linux":
   print("Your system is Linux")
 else:
   print(f"Cannot continue, unidentified system = {my_os}")
   sys.exit()
 # Get the current working directory
 current_working_directory = detect_working_directory()
 print(f"You are coding in: {current_working_directory}")
else:
 print(f"This module is called {__name__} and is being called by another script")
 
try:
    
  fuel = int(input("Fuel value : "))
  fuel_consumption = int(input("Fuel Consumption : "))
  endurance = fuel / fuel_consumption  
  print(f"Endurance :{endurance}")

except ZeroDivisionError as err:
  print(f"Fuel consumption can't be 0, Error : {err}")