import math as m
import sys
import mymodule

print("Hello World")
print(m.pi)
print(sys.version)

iseven = 55

a = mymodule.iseven(3)
print(a)
print(mymodule.iseven(2))

x = 5
if x < 10:
    print("toto")
elif x < 20:
    print("titi")
else:
    print("tutu")

for i in range(18, 2, -2):
    print(i)
