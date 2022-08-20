import sys
sys.stdin = open("2711.txt")
import re

T = int(input())

for _ in range(T):
    N, word = input().split()

    print(word[:int(N)-1] + word[int(N):])
    