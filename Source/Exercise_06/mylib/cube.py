cube_text = "Yo, time to cube stuff!"
def cube(x):
 return x*x*x
#print(cube(2))
#print(f"This module is called {__name__}")

if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
else:
 print(f"This module is called {__name__} and is being called by another script")
