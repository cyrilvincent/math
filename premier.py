def is_even(x):
    return x % 2 == 0

def is_prime(x):
    return False
    # x est premier sauf s'il possède un diviseur (x % qqchose == 0) entre 2 et x-1

print(is_even(8))
print(is_prime(7)) #True
print(is_prime(8)) #False
