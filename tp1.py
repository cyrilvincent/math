import math

# Afficher les nombres pairs < 100
# Créer la variable year = 2020
# Saisir votre année de naissance
# Afficher votre age
# Saisir un entier et afficher s'il est pair
# Saisir un entier et afficher s'il est premier

# for i in range(0,100,2):
#     print(i)
# year = 2020
# birth = int(input("Année de naissance:"))
# age = year - birth
# print(f"Vous avez {age} an(s)")
# if birth % 2 == 0:
#     print("Pair")
# else:
#     print("Impair")
nb = int(input("Saisir un nombre:"))
if nb < 2:
    print("Non premier")
else:
    is_prime = True
    for div in range(2,int(math.sqrt(nb)) + 1):
        if nb % div == 0:
            print("Non premier")
            is_prime = False
            break
    if is_prime:
        print("Premier")


