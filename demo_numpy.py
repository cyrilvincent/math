import numpy as np

print(np.__version__)

v1 = np.array([1,2,3,4])
print(v1)
vones = np.ones(4)
print(vones)

# v10 = np.arange(10,20,3)
# print(v10)
#
# v11 = np.linspace(0,10,1000)
# print(v11)
#
# vrnd = np.random.rand(10)
# print(vrnd)

result = v1 + vones
print(result)
v2 = np.array([5,6,7,8])
print(v1 * v2)
# v3 = np.array([1,2,3])
# print(v2+v3)

print(np.sin(v2))

print(np.random.rand(10) * 10)
print(np.random.randint(0,100,10))

print(v1 * 2)
print(np.sum(v1))

print(v1.size, v1.dtype, v1.shape, v1.ndim)

bytes = np.arange(250,256).astype(np.uint8)
print(bytes, bytes.dtype)
print(bytes + 1)

for i in v1:
    print(i)

print(v1[0], v1[-1])
v10 = np.arange(50)
print(v10)

print(v10[2:20])
print(v10[:10])
print(v10[20:])
print(v10[-10:])
print(v10[1:-1:3])
n = 5
print(v10[n:-n])