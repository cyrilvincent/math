def factorielle(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibo(n: int) -> int:
    f0 = 0
    f1 = 1
    n = 10
    for i in range(2, n + 1):
        result = f0 + f1
        f0 = f1
        f1 = result
    return result

def is_prime(n: int) -> bool:
    """
    Retourne vrai si n est premier
    :param n: les nombre à tester
    :return: True si n est premier
    """
    if n <= 1:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True