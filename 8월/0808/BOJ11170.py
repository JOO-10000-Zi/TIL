T = int(input())


for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m+1):
        if "0" in str(i):
            zero_cnt = str(i).count("0")
            cnt += zero_cnt
    print(cnt)
