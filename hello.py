print("Hello World")
a = 1
b = 2
print(a + b ** 2)
a += 1
a = a + 1
print(a)

print(3/2)
print(3//2)
print(3%2)

toto = "300"
print(toto)

wind_speed = 300

i = 3
j = 3.14
k = i + j
print(k)

print(type(j))

# print(j + toto)

# my_string = input("Saisir qqchose: ")
# my_int = int(my_string)
# print(my_int + 1)

f = 3.99
print(int(f))

print("Le résultat est: "+str(f))
print(f"Le résultat est {2 ** 0.5:.2f}")

condition = f < 4 and (i > 2 or k % 2) == 0
if condition:
    print("OK")

i = 0
while i < 10:
    print(i)
    i+=1

for i in range(10,0,-3):
    print(i)
