import sys
sys.stdin = open('1920.txt')

N = int(input())
soo = list(map(int, input().split()))
N2 = int(input())
soo2 = list(map(int, input().split()))

for i in soo2:
    if i in soo:
        print(1)
    else:
        print(0)