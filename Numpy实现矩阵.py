import numpy as np

# 创建一个5x5的矩阵
matrix = np.arange(6, 31).reshape(5, 5)
print("原始矩阵：",matrix)

transposed_matrix = matrix.T
print('转置矩阵为',transposed_matrix)

if np.linalg.det(matrix) != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("\n逆矩阵：")
    print(inverse_matrix)
else:
    print("\n该矩阵不可逆，因为其行列式为0。")