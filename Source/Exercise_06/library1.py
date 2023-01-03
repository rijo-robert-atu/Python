import math
print("input length of the two short triangle sides:")
a = float(input("a:"))
b = float(input("b:"))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))