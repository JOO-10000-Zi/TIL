import sys
sys.stdin = open("2669.txt")
from pprint import pprint 

coordi = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    x1, y1, x2, y2 = x1, y1, x2-1, y2-1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            coordi[i][j] += 1

pull = 0
for a in range(len(coordi)):
    for b in range(len(coordi)):
        if coordi[a][b] > 0 :
            pull += 1

print(pull)