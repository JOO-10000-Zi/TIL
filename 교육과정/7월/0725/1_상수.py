# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(int, input().split())
c = str(a)
d = str(b)
c = c[::-1]
d = d[::-1]

print(max(int(c),int(d)))
