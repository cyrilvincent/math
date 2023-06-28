import numpy as np
import tensorflow as tf

array1 = np.array([[1., 2], [3, 4]])
tensor1 = tf.convert_to_tensor(array1, dtype=tf.float64)
print(tensor1)
array1_inv = tf.linalg.inv(array1)
print(array1_inv)

array2 = np.array([[5., 6], [7, 8]])
tensor2 = tf.convert_to_tensor(array2, dtype=tf.float64)
res = tf.matmul(tensor1, tensor2)
print(res)