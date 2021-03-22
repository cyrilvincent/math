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
res = mymodule.isprime(6037)

l1 = list(range(1000))
res = mymodule.filtereven(l1)
print(res)
res = mymodule.filterprime(l1)
print(res)

res = mymodule.filter(lambda x: mymodule.isprime(x) == 0, l1)
print(res)

res = list(filter(lambda x: mymodule.isprime(x) == 0, l1))
print(res)

