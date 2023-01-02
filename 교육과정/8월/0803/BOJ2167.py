matrix = [[1, 2, 4], [8, 16, 32]]

K = 3

sum = 0
for _ in range(K):
    i, j, x, y = map(int,input().split())
    for row in range(i, x+1):
        for col in range(j, y+1 ):
            sum += matrix[row][col]
    
    print(sum)
