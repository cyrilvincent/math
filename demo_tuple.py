from typing import List, Tuple, Iterable


def my_function(param: float) -> Tuple[int, str]:
    return 1, "toto"

def sum(l: List[float]):
    res = 0
    for x in l:
        res += x
    return res

x, y = my_function(3.14)
print(x, y)
print(sum([1,2,3]))

