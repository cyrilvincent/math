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