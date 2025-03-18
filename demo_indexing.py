import numpy as np

mat32 = np.array([[1,2,3],[4,5,6]])
print(mat32)
print(mat32[0,0])
print(mat32[1,1])
print(mat32[-1, -1])

# 1ere ligne
print(mat32[0])
# Dernière ligne
print(mat32[-1])
# 2ème colonne
print(mat32[:,1])
# Dernière colonne
print(mat32[:,-1])

# Sous matrice 2,3,5,6
print(mat32[:,1:])
# Sous matrice 6
print(mat32[1:,2:])

print()
a22 = np.array([[1,2],[3,4]])
print(a22)
print(np.sum(a22))
print(np.sum(a22, axis=0)) # Sur les rows
print(np.sum(a22, axis=1)) # Sur les vecteurs columns