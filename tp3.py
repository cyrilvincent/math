import tp2

# def filter(fn, l):
#     res = []
#     for i in l:
#         if fn(i):
#             res.append(i)
#     return res
#
# def map(fn, l):
#     res = []
#     for i in l:
#         res.append(fn(i))
#     return res

if __name__ == '__main__':
    l = [1,2,99,-2,5,12,24]
    res = filter(lambda x : tp2.is_prime(x) == 0, l)
    print(list(res))
    # for i in res:
    #     print(i)
    # res = map(lambda x : x * 2, l)
    # print(res)

l = range(100)
# Filtrer les nb pairs
# Filtrer les nb premiers < 100
# Multiplier par 2 les nb premiers < 100
res = list(filter(lambda x : x % 2 == 0, l))
res = list(filter(lambda x : tp2.is_prime(x) == 0, l))
res2 = list(map(lambda x : x * 2, res))
print(res2)
