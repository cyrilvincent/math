def add(i: float,j: float):
    return i + j

def factorielle(n: int) -> int:
    """
    Calcul une factorielle
    :param n: le param
    :return: n!
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

print(factorielle(5))
print(is_prime(524287))
