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

l1 = [1,2,3,4,2,3,2]
l1[3] = -1
l3 = list(range(1000))
l2 = []
l1.append(99)
print(l1)
for _ in range(l1.count(2)):
    l1.remove(2)
print(l1)

for elem in l1:
    print(elem)

for i in range(100):
    l2.append(i ** 2)
print(l2)

