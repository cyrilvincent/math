def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_prime(x):
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True

def remove_all(l, nb):
    res = []
    for val in l:
        if val != nb:
            res.append(val)
    return res

def remove_all2(l, nb):
    count = l.count(nb)
    for i in range(count):
        l.remove(nb)
    return l


