# Value type
a = 1
b = a # a est copié dans b
b += 1
print(a, b)

# Ref type
l1 = [1, 2]
l2 = l1 # Passage par référence
l2.append(3)
print(l1, l2)

# Value reference
l1 = [1, 2]
l2 = list(l1) # Clone
l2.append(3)
print(l1, l2)

# == is
l1 = [1,2]
l2 = [1,2]
print(l1 == l2)
print(l1 is l2)
l1 = l2
print(l1 is l2)