import sys
from tp_house import display_surf_loyer

print("Hello World!")
print(sys.version)

# i = int(input("Saisir i:"))
# i += 1
# print(i)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


for i in range(0,10):
    a = is_even(i)
    print(a)