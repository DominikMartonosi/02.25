x = 7

matrix = [['.' for _ in range(x)] for _ in range(x)]

for i in range(x):
    matrix[i][i] = 'O'
    matrix[i][-i-1] = 'O'

for row in matrix:
    print(' '.join(row))