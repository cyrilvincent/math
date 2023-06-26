import math

print("Hello")

a = 1
b = a + 1
# commentaire

print(f"Voici la valeur de b: {math.sin(b):.2f}")

s = input("Saisir un nombre: ")
print(type(s))
x = int(s)
if x % 2 == 0:
    print(f"{x} est pair")
else:
    print(f"{x} est impair")

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(2,10,2):
    print(i)

def add(i, j):
    return i + j

res = add(2, 3)
res = add(i = 2, j = 3)
print(res)