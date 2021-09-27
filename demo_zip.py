t = [0,1,2,3,4,5,6,7,8,9]
temp = [20.0, 20.1, 20.2, 20.3, 20.4, 20.5, 20.6, 20.7, 20.8, 20.9]
pres = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
t_temp = list(zip(t, temp))
t_temp_pres = list(zip(t, temp, pres))

print(t_temp_pres)
print(t_temp_pres[1][2])

# for tuple in t_temp_pres:
#     print(tuple[1] * tuple[2])