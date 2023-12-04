class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(s) for s in row.split()] for row in matrix_string.splitlines()]      

    def row(self, index):
        return self.matrix_string[index - 1]

    def column(self, index):
        return [s[index - 1] for s in self.matrix_string]

