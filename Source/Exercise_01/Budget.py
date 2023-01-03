print(" My budget for academic year !")
# budget on monthly basis
a = int(input("total income per month :"))
b = int(input("total grocery expense :"))
c = int(input("rent per month :"))
d = int(input("Other expences :"))
# Total expence per month
e = b + c + d
print(e)
print(f"Total expence per month :", e)
# Available savings after expense per month
f = a-e
print(f"Available savings after expense per month :", f)
# Total expence per year
g = f*12
print(f"Total expence per year :", g)


