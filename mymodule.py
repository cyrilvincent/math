def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_prime(x):
    # Un nombre premier est divisible par exactement 2 diviseurs : 1 et lui même
    # 2,3,5,7,11,13, ...
    # Tout nombre x > 2 est premier SAUF s'il possède un diviseur (%) compris entre [2,x-1]
    
