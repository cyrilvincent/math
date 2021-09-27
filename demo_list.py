l1 = [1,2,5,9,99,-2]
print(l1)
for elem in l1:
    print(elem)

print(sum(l1))
print(l1[1])

somme = 0
for elem in l1:
    somme += elem
print(somme)

print(l1)
print(l1[1:4])
print(l1[1:-1])
print(l1[:4])
print(l1[1:])
print(l1[:])
l1.append(0)
l1.insert(0, 100)
print(l1)