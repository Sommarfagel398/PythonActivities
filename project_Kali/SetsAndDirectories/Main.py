"""problem 5"""
rowcol = lambda row, col: sum(row[i] * col[i] for i in range(len(row)))
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Incompatible matrix"

    return [
        [rowcol(A[i], [B[j][k] for j in range(len(B))]) for k in range(len(B[0]))]
        for i in range(len(A))
    ]

rowA = int(input("Enter the number of rows for matrix A: "))
colA = int(input("Enter the number of columns for matrix A: "))
A = [list(map(int, input(f"Enter row {i + 1} for matrix A: ").split())) for i in range(rowA)]

rowB = int(input("Enter the number of rows for matrix B: "))
colB = int(input("Enter the number of columns for matrix B: "))
if colA != rowB:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    B = [list(map(int, input(f"Enter row {i + 1} for matrix B: ").split())) for i in range(rowB)]
    result = matrix_multiply(A, B)
    print("Result: ")
    for row in result:
        print(row)



































