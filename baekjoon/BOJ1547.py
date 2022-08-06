N = int(input())

CUP_numbers = [1, 2, 3]


for _ in range(N):
    X, Y = map(int, input().split())
    x = CUP_numbers.index(X)
    y = CUP_numbers.index(Y)
    CUP_numbers[x], CUP_numbers[y] = CUP_numbers[y], CUP_numbers[x]

print(CUP_numbers[0])