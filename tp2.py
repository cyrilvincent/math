from typing import List, Tuple
import tp1

# Faire la fonction min_max qui retourne le min et le max avec une boucle
# Faire la fonction filter_even qui retourne une liste filtrée par les nombres pairs
# [1,2,3,4,8,99,-2,7] -> [2,4,8,-2]
# Bonus faire de même avec les nombres premiers : comment rendre le code + générique ?

def min_max(l: List[float]) -> Tuple[float, float]:
    min = l[0]
    max = l[0]
    for i in l[1:]:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

def filter_even(l: List[int]) -> List[int]:
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

def filter_prime(l: List[int]) -> List[int]:
    res = []
    for i in l:
        if tp1.is_prime(i):
            res.append(i)
    return res

def filter_generic(fn, l:List[int]) -> List[int]:
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 8, 99, -2, 7]
    min, max = min_max(l1)
    print(min, max)
    #l_even = filter_even(l1)
    l_even = filter_generic(lambda x: x % 2 == 0, l1)
    print(l_even)
    l_prime = filter_generic(lambda x: tp1.is_prime(x), l1)
    print(l_prime)