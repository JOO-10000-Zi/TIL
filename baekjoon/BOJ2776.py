import sys
sys.stdin = open("2776.txt")

for _ in range(int(input())):
    N = int(input())
    li1 = set(map(int, input().split()))
    M = int(input())
    li2 = list(map(int, input().split()))
    for n in li2:
        print(1 if n in li1 else 0)