import mymodule as m
import math

def filter_even(l):
    res = []
    for val in l:
        if m.is_even(val):
            res.append(val)
    return res

def filter_prime(l):
    res = []
    for val in l:
        if m.is_prime(val):
            res.append(val)
    return res

def filter_generic(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,-2,-5,-99,100]
    print(filter_even(l))
    print(filter_prime(l))
    print(filter_generic(m.is_even, l))
    print(filter_generic(m.is_prime, l))
    print(list(filter(lambda x: x % 2 == 0, l)))
    print(list(filter(lambda x: m.is_prime(x) == 0, l)))

    print(list(map(lambda x: math.cos(abs(x ** 0.5 + 1)), l)))

    print(list(map(lambda x: x ** 2, filter(lambda x: m.is_prime(x), l))))

    print(list(filter(lambda x : x % 2 == 0, filter(lambda x: m.is_prime(x), l))))
    print(list(filter(lambda x: x % 2 == 0, filter(lambda x: x < 50 and x > 10, l))))
    print(list(map(lambda x: math.sin(x), filter(lambda x: m.is_prime(x), l))))
    # Filtrer le seul nombre premier pair
    # Filtrer les nombres pair compris entre 10 et 50
    # Filtrer les nombres premiers et afficher leur sinus

    # <=>
    # Intention List
    print([math.sin(x) for x in l if m.is_prime(x)])

    identity = [x for x in l]
    to_square = [x ** 2 for x in l]
    even_filter = [x for x in l if m.is_even(x)]

    res = list(map(lambda x: math.sin(x), filter(lambda x: m.is_prime(x), l)))
    # A réecrire en intention list
    res = [math.sin(x) for x in l if m.is_prime(x)]
    print(res)