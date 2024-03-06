import sys
from typing import List, Tuple

def is_even(nb: int) -> bool:
    return nb % 2 == 0

def is_prime(nb : int) -> bool:
    # Tout nb entier naturel > 1 est premier sauf s'il possède un diviseur entre 2 et nb-1
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True

def filter_prime(l: List[int]) -> List[int]:
    res = []
    for value in l:
        if is_prime(value):
            res.append(value)
    return res

def demo_tuple() -> Tuple[float, float, float]:
    # N-uplet
    # Couple = 2-uplet
    # Triplet = 3-uplet
    # Traitement
    return 1.0,2.0,3.1



if __name__ == '__main__':
    print("Hello World 2")
    print(sys.version)
    res = is_even(2)
    assert res is True
    res = is_even(3)
    assert res is False
    assert is_prime(1223) is True
    l = range(10)
    res = filter_prime(l)
    assert [2,3,5,7] == res
    x, y, z = demo_tuple()
    print(x, y, z)
