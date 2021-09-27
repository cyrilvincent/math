import premier

# TP1
def remove_all(l, item):
    nb = l.count(item)
    for i in range(nb):
        l.remove(item)
    return l

l1 = [1,2,9,99,-1,99,0,50,21,7,31]
# print(l1.index(99))
# l1.remove(99)
# print(l1)
remove_all(l1, 99)
print(l1)

# TP2
# Filtrer les nombres pairs
def filter_even(l):
    result = []
    for elem in l:
        if elem % 2 == 0:
            result.append(elem)
    return result

print(filter_even(l1)) # => [2,0,50]

# TP3
# Filtrer les nombres premiers
def filter_premiers(l):
    result = []
    for elem in l:
        if premier.is_prime(elem):
            result.append(elem)
    return result

print(filter_premiers(l1))

# TP4 : Reflexion Bonus
def filter_generic(l, fn_filter):
    result = []
    for elem in l:
        if fn_filter(elem):
            result.append(elem)
    return result

res = filter_generic(l1, premier.is_prime)
print(res)
res = filter_generic(l1, lambda x: x % 2 == 0)
print(res)

print(list(filter(lambda x: x % 2 == 0, l1)))

print(list(map(lambda x: x+ 1, l1)))