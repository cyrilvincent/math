import sys
import numpy
import numpy as np

print(sys.version, numpy.__version__)
print("Hello World")
x = 1
y = x + 1
x = x + 1
x += 1
x /= 2 # x = x / 2
print(f"La valeur de x est: {x:.2f}")

# x = input("Saisir x: ")
# print(x / 2)

n = 5
result = 1
for i in range(1, n+1):
    result *= i
print(result)