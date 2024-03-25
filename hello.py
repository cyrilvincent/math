import sys

print("Hello World!")
print(sys.version)

x = 1

def add(x, y):
    return x + y

def essai(l):
    sum = 0
    for i in l:
        sum += i
    return sum

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# TP
# Créer la fonction is_prime(x) qui renvoie True si x est premier False sinon
# Tout nombre >= 2 est premier sauf s'il possède un diviseur entre 2 et n-1

result = add(2,3)
print(result)

l = [1,2,3,4,5,6,7,8,9,10]
print(sum(l))
print(is_even(7))

for i in range(2, 10):
    print(i)