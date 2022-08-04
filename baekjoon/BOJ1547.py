from collections import deque

N = int(input())

CUP_numbers = [1, 2, 3]


for _ in range(N):
    X, Y = map(int, input().split())
    CUP_numbers.insert(X-1, Y)
    CUP_numbers.remove(Y)
    CUP_numbers.remove(X)
    CUP_numbers.insert(Y-1, X)
    print(CUP_numbers)
print(CUP_numbers)
print(CUP_numbers[0])