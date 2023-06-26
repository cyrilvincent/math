def is_even(x: int) -> bool:
    return x % 2 == 0

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input("Saisir un nombre: "))
    res = is_even(x)
    if res:
        print("Even")
    else:
        print("Odd")
    res = is_prime(x)
    if res:
        print("Prime")
    else:
        print("Not prime")