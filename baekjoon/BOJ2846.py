import sys
from turtle import up
sys.stdin = open('2846.txt')

N = int(input())
uphill = list(map(int, input().split()))
start, end = uphill[0], uphill[0]

big_cnt = 0
for i in range(1, N):
    if end >= uphill[i]:
        start = uphill[i]
        end = uphill[i]
    else:
        end = uphill[i]
    big_cnt = max(big_cnt, end - start)

print(big_cnt)
