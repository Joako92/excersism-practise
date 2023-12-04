matrix = "89 1903 3\n18 3 1\n9 4 800"
matrix2 = "1"

matrix_string = [[int(s) for s in row.split()] for row in matrix.splitlines()]

index = 1

row = [s for s in matrix_string[index - 1]]
column = [s[index - 1] for s in matrix_string]

print("Matrix:\n",matrix)
print()
print("matrix_string:\n",matrix_string)
print()
print(f"row {index}:", row)
print()
print(f"column {index}:", column)
