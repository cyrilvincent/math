def iseven(x: int):
    return x % 2 == 0


f = lambda x: x % 2 == 0
# f(x) = x + 1
# f(x) = x % 2 == 0


def isprime(nb: int) -> bool:
    """
    Detecte si nb est premier
    :param nb: un entier
    :return: True si premier
    """
    if nb < 2:
        return False
    for div in range(2, nb):
        if nb % div == 0:
            return False
    return True

def filtereven(l):
    res = []
    for elem in l:
        if iseven(elem):
            res.append(elem)
    return res

def filterprime(l):
    res = []
    for elem in l:
        if isprime(elem):
            res.append(elem)
    return res

def filter(fn, l):
    res = []
    for elem in l:
        if fn(elem):
            res.append(elem)
    return res

def map(fn, l):
    res = []
    for elem in l:
        res.append(fn(elem))
    return res

def get_min_max_avg(l):
    """

    :param l:
    :return:
    """
    min = l[0]
    max = l[0]
    sum = 0
    for nb in l:
        sum += nb
        if nb < min:
            min = nb
        if nb > max:
            max = nb
    return min, max, sum / len(l)

# tp1
# Créer un module monmodule
# Créer la fonction isprime(nb:int) qui retourne True si nb est premier
# Un nombre est premier si et seulement si il possède uniquement 2 diviseurs : 1 et nb
# Tous les nombres >= 2 sont premiers sauf s'il possède un diviseur entre 2 et nb-1
# Modulo : %
# Tester

#tp2
#Dans le programme principale créer une liste de 1000 entiers
#Dans mymodule créer la fonction filtereven(l) et renvoie la liste filtrée
#Exemple filtereven([1,2,3,4]) => [2,4]
#Créer la fonction filterprime(l) => retourne la liste filtrée des nombres premiers
#Bonus : Essayer de créer une fonction de filtre générique

#tp3
#Programmer la fonction get_min_max_avg(l) => Tuple min, max, avg
#A programmer avec 1 seule boucle