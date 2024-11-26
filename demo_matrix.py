import numpy as np

mat1 = np.array([[1,2],[3,4]])
print(mat1)
mat2 = np.array([[5,6],[7,8]])
print(mat2)
mat3 = mat1 + mat2
print(mat3)

print(mat1[0,0])
for row_index, row in enumerate(mat1):
    for col_index, col in enumerate(row):
        print(row_index, col_index, col)

print(mat1.ndim, mat1.size, mat1.shape)

v12 = np.arange(12)
mat34 = v12.reshape(-1,4)
print(mat34)
mat43 = v12.reshape(4,-1)
print(mat43)
mat112 = v12.reshape(1,12)
print(mat112)
mat121 = v12.reshape(12,1)
print(mat121)
mat62 = mat34.reshape(6,2)
cube232 = v12.reshape(2,3,2)
print(cube232)

res = np.linalg.inv(mat1)
print(res)

rnd = np.random.rand(100,100)
print(np.mean(rnd))

print(np.dot(mat1, mat2))

print(mat1)
print(np.sum(mat1, axis=0))
print(np.sum(mat1, axis=1))