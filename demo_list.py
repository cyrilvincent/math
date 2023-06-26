l1 = [1,2,3,4]
# function
res = len(l1)
print(res)
# method
l1.append(5)
print(l1)
l2 = [1,2,3,2,4,5,2,3]
print(l2.index(2))

nb = l2.count(2)
for i in range(nb):
    l2.remove(2)
print(l2)