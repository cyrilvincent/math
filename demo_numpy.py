import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4], dtype=np.float64)
print(a1, a1.dtype)
for value in a1:
    print(value)

a2 = np.arange(4) # 0,1,2,3
a3 = np.arange(2,6) #2,3,4,5
a4 = np.arange(0,10,3) #0,3,6,9

a5 = np.arange(0,10.1,0.1)
print(a5)

a6 = np.linspace(0,10,101)
print(a6)

np.random.seed(42)
rnd = np.random.rand(10) * 10
print(rnd)
rnd2 = np.random.randint(0,100,10)
print(rnd2)

# a1 = a1 + 254
# print(a1)

print(a1 + a2)

print(np.cos(a1))
# np.exp, np.log, np.abs

print(a1 + a5)

