import numpy as np

print(np.__version__)

np.nan # Not a Number


a1 = np.array([1,2,3,4])
print(a1)
a2 = np.ones(4)
print(a2)
a3 = np.arange(1,10,2)
print(a3)
a4 = np.linspace(1,9,5)
print(a4)

np.random.seed(42)
rnd1 = np.random.rand(10)
print(rnd1)
rnd2 = np.random.randint(0,100, 10)
print(rnd2)

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
print(a2 * 3)
res = a1 + a2
print(res)
print(np.sum(a1))
print(a1.ndim, a1.size, a1.shape, a1.dtype)

for i in a1:
    print(i)
print(a1[0], a1[1])

a3 = np.arange(10) ** 2
print(a3)
print(a3[::-1])

a4 = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
a4 = np.sin(a4)
filter = (a4 > 0) | (True)
print(filter)
print(a4[filter])

t = np.arange(0, 1, 0.01)
v = np.sin(t)
filter = (t > 0.2) & (t < 0.4)
result_v = v[filter]
result_t = t[filter]
print(result_t)
print(result_v)

np.savez("data/mydata.npz", t=t, voltage=v)

data= np.load("data/mydata.npz")
print(data)
v2 = data["voltage"]
print(v2)

a = 0
b = 1
for i in range(100):
    c = a + b
    a = b
    b = c
    np.savez(f"data/fibo_{i}.npz", c=c)
print(c)

