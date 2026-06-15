# Créer la fonction min(a, b) qui retourne le min de a et b
# Créer la fonction is_even(i) qui retourne True si i est pair
# Créer la fonction power(a, b) avec un for qui retourne a**b
# Bonus : difficile is_prime(a) qui retourne True si a est premier, tout nb i >= 2 est premier sauf si possède un diviseur entre 2 et n-1

def min(a, b):
    if a < b:
        return a
    else:
        return b

def is_even(i):
    return i % 2 == 0

def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

def is_prime(i):
    if i < 2:
        return False
    for div in range(2, i):
        if i % div == 0:
            return False
    return True

print(power(2,8))

print(min(4,99))
print(is_prime(8), is_prime(7), is_prime(1223))