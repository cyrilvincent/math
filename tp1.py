# Tester mon hello.py dans main.py
# Créer la fonction min_max_avg(l: List[float]) -> Tuple[float, float, float]
# Retourne le min, le max, la moyenne
# A coder avec une boucle
# Tester avec __name__ et dans main.py

from typing import List, Tuple


def min_max_avg(l: List[float]) -> Tuple[float, float, float]:
    min = l[0]
    max = l[0]
    sum = 0
    for value in l:
        if value < min:
            min = value
        if value > max:
            max = value
        sum += value
    return min, max, sum / len(l)

if __name__ == "__main__":
    l = [1,2,99,-5,10,7,8,3,12,15]
    min, max, avg = min_max_avg(l)
    assert min == -5
    assert max == 99
    print(avg)