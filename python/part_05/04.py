n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]

new_matrix = [[0] * n for i in range(m)]

for i in range(n):
    for j in range(m):
        new_matrix[j][i] = matrix[i][j]

for x in range(m):
    for y in range(n):
        print(new_matrix[x][y], end=" ")
    print()
