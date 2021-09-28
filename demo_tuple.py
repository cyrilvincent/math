def return_tuple():
    return 3,4

a,b = return_tuple()
print(a,b)

# TP
# Tester tp_liste filter map
# Tester demo_value_ref
# def min_max_avg(l):
# Avec une boucle retourne min, max, avg
# Tester

def min_max_avg(l):
    """

    :param l:
    :return: min, max, avg
    """
    min = l[0]
    max = l[0]
    sum = 0
    for elem in l:
        if elem < min:
            min = elem
        elif elem > max:
            max = elem
        sum += elem
    return min, max, sum / len(l)

min, max, avg = min_max_avg([1,2,3,4,5,6,7,8,9,10])
print(min, max, avg)
_, _, avg = min_max_avg([1,2,3,4,5,6,7,8,9,10])