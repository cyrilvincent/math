# Créer la liste range(10)
# min_max_avg(l) => (min, max, avg)
# Tester

def min_max_avg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        sum += i
        if i > max:
            max = i
        elif i < min:
            min = i
    return min, max, sum / len(l)

if __name__ == '__main__':
    res = min_max_avg(range(100))
    print(res)
    min, max, avg = min_max_avg(range(100))
    print(min, max, avg)

    l1 = ["a","b","c"]
    l2 = [1,2,3]
    l3 = [1.01,1.02,1.03]
    res = zip(l1, l2, l3)
    print(list(res))
