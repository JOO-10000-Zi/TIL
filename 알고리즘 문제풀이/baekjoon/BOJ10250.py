import sys
sys.stdin = open('10250.txt')
from pprint import pprint

T = int(input())

for _ in range(1):
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(H)

    hotel = [[0]*H for _ in range(W)]
    hotel = list(map(list, zip(*hotel)))[::-1]

    pprint(hotel)

    