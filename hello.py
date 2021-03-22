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

print(mymodule.isprime(7))
print(mymodule.isprime(14))
print(mymodule.isprime(6037))
