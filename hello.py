import sys

print("Hello World!")
print(sys.version)

a = 3.14
a = a + 1
a += 1
print(f"La valeur est {a:.2f}")
b = 0

if a < 10 or b == 0:
    print("Je suis inférieur à 10")
else:
    print("Jene suis pas ingérieur à 10")

print (3 // 2, 3 % 2)

for i in range(10):
    print(i)

nb = 8191


def is_prime(nb):
    result = True
    if nb < 2:
        result = False
    else:
        for div in range(2, nb):
            if nb % div == 0:
                result = False
                break
    return result

result = is_prime(7)
print(result)
