def factorielle(n: int) -> int:
    """
    Calcul la factorielle de n!
    :param n: le nombre en entrée
    :return: n!
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """
    Suite de fibonacci
    :param n: index de la suite
    :return: f(n)
    """
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        result = 0
        for i in range(2, n + 1):
            result = a + b
            a = b
            b = result
        return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        for div in range(2, n):
            if n % div == 0:
                return False
        return True


