def is_even(x):
    return x % 2 == 0

def is_prime(x):
    if x < 2:
        return False
    else:
        for denominateur in range(2,x):
            if x % denominateur == 0:
                return False
    return True


print(is_even(8))
print(is_prime(7)) #True
print(is_prime(8)) #False
print(is_prime(4391))
