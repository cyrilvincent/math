# Créer la liste des entiers < 100 : range(100)
# Filtrer les nombres premiers
# Sur le résultat précédent filtrer les nombres pairs
# Tester avec un enorme range(100000000000000000)

import tp1
l = range(100000000000000000000000000000)
res = filter(tp1.isPrime, l)
res = filter(lambda x : x % 2 == 0, res)
res = map(lambda x : x ** 0.5, res)
for i in res:
    print(i)
