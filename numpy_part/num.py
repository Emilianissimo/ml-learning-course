import numpy as np

new_list = [1, 2, 3]

new_array = np.array(new_list)

new_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 6, 5],
]

new_matrix_array = np.array(new_matrix)

random_array = np.random.rand(5, 2)
random_gauss_array = np.random.randn(3, 2)

# Indexing

arr_2d = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

print(arr_2d.shape)
print(arr_2d[2, 2])
