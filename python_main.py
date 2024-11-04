import tp_house_lib as house

surfaces, loyers = house.load("data/house/house.npz")
print(house.stats(surfaces))
print(house.stats(loyers))
print(house.compute_loyers_m2(loyers, surfaces))