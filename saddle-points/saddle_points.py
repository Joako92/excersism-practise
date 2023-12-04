def saddle_points(matrix):
    columns = list(zip(*matrix))
    points = [] ##SADDLE POINTS
    
    if any(len(row) != len(matrix[0]) for row in matrix): ##IF ROWS HAVE DIFF LENGTH
        raise ValueError("Matrix not square.")

    for row in range(len(matrix)): ##ROWS INDEX        
        for col in range(len(matrix[row])): ##COLUMNS INDEX         
            if matrix[row][col] == max(matrix[row]) and matrix[row][col] == min(columns[col]):
                points.append((row+1,col+1))
    return [{"row": point[0], "column": point[1]} for point in points]

