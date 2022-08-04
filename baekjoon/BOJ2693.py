
T = int(input())

for _ in range(T):
    num = list(map(int, input().split()))
    num_up = sorted(num)

    print(num_up[-3])
