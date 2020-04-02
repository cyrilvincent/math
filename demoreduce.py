l = range(1,10)
print(sum(l))
import functools
res = functools.reduce(lambda acc, cur : acc * cur, l)
"""
acc = 0
cur = 1 => 1
acc = 1
cur = 2 => 3
acc = 3
cur = 3 => 6
"""
print(res)