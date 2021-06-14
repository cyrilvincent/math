import mymodule as m
from mymodule import is_even

print("Hello World")

i = 2
print(type(i))

i += 1

if i % 3 == 0:
    print(f"{i} est multiple de 3")
elif i% 3 == 1:
    print(f"{i} est * 3 + 1")
else:
    print(f"{i} est * 3 + 2")

for i in range(10):
    print(i)
    if i == 5:
        break

def is_even():
    return "toto"

res = m.is_even(3)
print(res)
res = is_even(3)
print(res)