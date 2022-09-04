import sys
sys.stdin = open("14720.txt")

N = int(input())
shop = list(map(int, input().split()))

cnt = 0 
for i in range(N):
    if shop[i] == cnt % 3:
        cnt += 1
print(cnt)