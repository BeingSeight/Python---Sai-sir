# 38. Matrix Transpose
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[int(input(f"Matrix[{i}][{j}]: ")) for j in range(3)] for i in range(3)]
transposed = transpose_matrix(matrix)
print("Transposed matrix:")
for row in transposed:
    print(row)
