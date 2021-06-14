# Value type str, int, float, bool
a = 1
b = a
print(a == b)
a += 1
print(a == b)

# Reference type
l1 = [1,2,3]
l2 = l1
print(l1 == l2)
l1.append(4)
print(l1 == l2)
print(l1 is l2) # True
print(l1, l2)

# Reference type with list()
l1 = [1,2,3]
l2 = list(l1)
print(l1 == l2) # True
print(l1 is l2) # False
l1.append(4)
print(l1 == l2)
print(l1, l2)