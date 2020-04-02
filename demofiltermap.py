import tp1
import math

def filterEven(l):
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

def filterPrime(l):
    res = []
    for i in l:
        if tp1.isPrime(i):
            res.append(i)
    return res

def myfilter(fn, l):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def isEven(x):
    return x % 2 == 0

if __name__ == '__main__':
    l = [1, 2, 9, 8, 7, -2, 11, -99, 99, 50]
    res = filterEven(l)
    res = filterPrime(l)
    res = myfilter(lambda x : x % 2 == 0, l)
    res = filter(tp1.isPrime, l)
    print(list(res))
    res = map(lambda x : math.tanh(x), l)
    print(list(res))