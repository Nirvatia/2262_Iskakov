n = 5
tblmul = [[(col + 1) * (row + 1) for col in range(n)] for row in range(n)]
print(*tblmul,sep='\n')

# Expected: 
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# [4, 8, 12, 16, 20]
# [5, 10, 15, 20, 25]