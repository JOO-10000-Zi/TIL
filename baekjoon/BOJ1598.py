from pprint import pprint
n = 4
m = 40
pan = [[0]*m for _ in range(n)]
z = 4
for x in range(m+1):
    for y in range(n+1):
        if not (-1 < x < n and -1 < y < m):
            break
        if x == 0:
            pan[y][x] = x

    z += 4

pprint(pan)