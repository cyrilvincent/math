print("hello")
x = 1
x = x + 1
x += 1
print(x)

x = 2**3

# x = int(input("Saisir une donnée: "))
# print(x ** 2)
#
# if x % 2 == 0:
#     print("Pair")
# else:
#     print("Impair")

# i = 0
# while i < 10:
#     print(i)
#     i+=1

for i in range(10):
    print(i)

def is_even(x):
    return x % 2 == 0

print(is_even(7))
print(is_even(8))