def toto():
    return 1,2,3,4

if __name__ == '__main__':
    x,y,z,a = toto()
    print(x,y,z,a)
    res = toto()
    print(res)
