def min_max_avg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for val in l:
        if val < min:
            min = val
        elif val > max:
            max = val
        sum += val
    return min, max, sum / len(l)

if __name__ == '__main__':
    l = range(10)
    min, max, avg = min_max_avg(l)
    print(min, max, avg)