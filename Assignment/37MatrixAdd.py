# 37. Matrix Addition
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 = [[int(input(f"Matrix1[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
matrix2 = [[int(input(f"Matrix2[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("Resultant matrix after addition:")
for row in result:
    print(row)
