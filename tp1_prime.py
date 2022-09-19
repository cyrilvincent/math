def is_prime_number(x):
    # Return True or False
    # Tout nombre > 1 qui n'est divisible que par 1 et x
    # Tout nombre > 1 est premier sauf s'il possède un diviseur (% == 0) compris entre 2 et x - 1
    for div in range(2,x):
        if x % div == 0:
            return False
    return True

# Saisir un entier
my_nb = int(input("Saisir un entier: "))
res = is_prime_number(my_nb)
print(res)