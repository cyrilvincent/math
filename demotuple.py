def min_max_avg(l):
    sum = 0
    min = l[0]
    max = l[0]
    for val in l:
        sum += val
        if val < min:
            min = val
        elif val > max:
            max = val
    return min, max, sum / len(l)

l = [1,2,3,4,5,6,7,-2,-5,-99,100]
min, max, avg = min_max_avg(l)
print(min, max, avg)

