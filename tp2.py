import math

def is_even(x):
    return x % 2 == 0

is_even = lambda x : x % 2 == 0

def is_prime(x):
    if x < 2:
        return False
    else:
        for div in range(2, int(math.sqrt(x)) + 1):
            if x % div == 0:
                return False
        return True

if __name__ == '__main__':
    print(is_even(8))
    print(is_even(7))
    print(is_prime(4049))

# tp2
# Créer la fonction is_even(x)
# Tester dans le même module
# Tester depuis un autre module
# Créer la lambda is_even
# Créer la fonction is_prime(x)