import math
import sys
import mymodule

print("Hello World")
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

res = list(filter(lambda x: mymodule.isprime(x), l1))
print(res)

res = list(map(lambda x : math.tanh(x), res))
print(res)

res = list(map(lambda x : math.tanh(x), filter(lambda x: mymodule.isprime(x), l1)))
# Intention list <=> Comprehension list
res = [math.tanh(x) for x in l1 if mymodule.isprime(x)]
print(res)

a = 1
b = a
b += 1
print(a, b, a == b)

l1 = [1,2,3]
l2 = l1
l2.append(4)
print(l1, l2, l1 == l2)

l1 = [1,2,3]
l2 = list(l1)
l2.append(4)
print(l1, l2, l1 == l2)

print([1,2] == [1,2], [1,2] is [1,2])
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2, l1 is l2)
l1 = l2
print(l1 == l2, l1 is l2)

def toto():
    return 1,True
a,b = toto()
print(a, b)

index = [1,2,3,4]
l1 = ["a","b","c","d"]
t2 = [1.0,2.1,-5.1,5]
res = list(zip(index, l1, t2))
print(res[0][1])

