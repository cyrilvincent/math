import sys

print("Hello World!")
print(sys.version)

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True



print(is_prime(7919))
res = is_prime(7)
