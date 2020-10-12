print("Hello World")
i = 1
i += 1
print(i)

if i == 2:
    print(i)
elif i == 3:
    print(i)
else:
    print(i)

i = 2 ** 8
i = 4 / 3 # 1.33333
i = 4 // 3 # 1

print(f"La valeur de i est {i:.2f}")

i = 0
while i < 99:
    i+=1

for i in range(10,0,-2):
    print(i)

if i % 2 == 0:
    pass

annee = input("Saisir un message:")
iannee = int(annee)
print(iannee + 1)
