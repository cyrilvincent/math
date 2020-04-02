import tp1

def myfilter(fn, l):
    for i in l:
        if fn(i):
            yield i

def mymap(fn , l):
    for i in l:
        yield fn(i)

def list(l):
    res = []
    for i in l:
        res.append(i)
    return res

if __name__ == '__main__':
    # res = myfilter(tp1.isPrime, range(10))
    # res = myfilter(lambda x : x % 2 == 0, res)
    # res = mymap(lambda x : x ** 2, res)
    res = filter(tp1.isPrime, range(100))
    res = filter(lambda x : x % 2 == 0, res)
    res = list(map(lambda x : x ** 2, res))
    print(len(res))
    for i in res:
        print(i)