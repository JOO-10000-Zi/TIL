import sys

n = 4
m = 10000000
sys.setrecursionlimit(m) 

pan = [[0] * m for _ in range(n)] 
z = 0
for x in range(m):
    for y in range(n):
        if x == 0:
            pan[y][x] = y + 1
        if x != 0:
            pan[y][x] = pan[y][0] + z
    z += 4

x1, y1 = map(int, input().split())
x1_cnt = []
y1_cnt = []
for i in range(m):
    for j in range(n):
        if pan[j][i] == x1:
            x1_cnt.append(i)
            y1_cnt.append(j)
        if pan[j][i] == y1:
            x1_cnt.append(i)
            y1_cnt.append(j)
    x1_cnt.sort(reverse=True)
    y1_cnt.sort(reverse=True)

mongki = (x1_cnt[0] - x1_cnt[1]) + (y1_cnt[0] - y1_cnt[1])

print(mongki)