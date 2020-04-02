# Créer la fonction isEven(x:int)
# Tester la faction dans un if __name__ ...
# Créer la fonction isPrime(x:int)
# Un nombre est premier > 1 et divisible uniquement par 1  et lui-même
# Ex : 7 est premier, 8 est divisble par 2 et 4 n'est pas premier
# Réciproque : Tout nombre > 1 est premier sauf s'il a un diviseur entre 2 et n-1

# Reprise à 13h

def isEven(x):
    return x % 2 == 0

def isPrime(x):
  if x < 2:
    return False
  else:
    for div in range(2,int(x ** 0.5) + 1):
      if x % div == 0:
        return False
    return True

if __name__ == '__main__':
    print(isEven(8))
    print(isEven(7))
    print(isPrime(6700417))
    print(isPrime(6088))
    l = [1,8,2,4]
    l[1:3] # => 8,2