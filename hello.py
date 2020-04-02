import monmodule as m
#from monmodule import *

def add(x,y):
    return x + y

def max(x,y):
    if x >= y:
        return x
    else:
        return y

def titi():
    return "toto"

def sum(l):
    res = 0
    for value in l:
        res = res + value
    return res

if __name__ == '__main__':
    print(m.titi())
    maliste = [1,2,9,8,7,-2,3.14,-99,99,50]
    print(len(maliste))
    print(min(maliste))
    for value in maliste:
        print(value)
    print(maliste[2])
    for i in range(100,0,-3):
        print(i)
    print(4//3)
    print(4%3)
    print(8%2 == 0)
    print(9%2 == 0)




