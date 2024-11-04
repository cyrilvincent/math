my_list = [1,2,3,4,5,6,7,8,9,10]
print(len(my_list))
print(min(my_list))
print(sum(my_list))

def sum(l: list[float]) -> float:
    total = 0
    for i in l:
        total = total + i
    return total

print(sum(my_list))
