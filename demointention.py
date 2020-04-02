import tp1

l = range(100)
res = map(lambda x : x ** 2, filter(tp1.isPrime, l))
print(list(res))

# <=> Intention list, comprehension list

res = [x ** 2 for x in l if tp1.isPrime(x)]
print(res)

a = 1
b = a
a += 1
print(a,b)

l1 = [1,2,3]
l2 = list(l1)
l1.append(4)
print(l1, l2)

l1 = [1,2,3]
l2 = l1
l1.append(4)
print(l1, l2)
