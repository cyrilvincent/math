def iseven(x: int):
    return x % 2 == 0


def isprime(nb: int)->bool:
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True

# tp1
# Créer un module monmodule
# Créer la fonction isprime(nb:int) qui retourne True si nb est premier
# Un nombre est premier si et seulement si il possède uniquement 2 diviseurs : 1 et nb
# Tous les nombres >= 2 sont premiers sauf s'il possède un diviseur entre 2 et nb-1
# Modulo : %
# Tester