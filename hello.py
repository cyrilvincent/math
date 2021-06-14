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

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(3))