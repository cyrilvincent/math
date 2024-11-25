import house_lib as h

surfaces, loyers = h.load("data/house/house.npz")
surfaces, loyers = h.filter(200, surfaces, loyers)