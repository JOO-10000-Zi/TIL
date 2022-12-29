T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    unit_cnt = [0] * 8
    for i in range(8):
        if N >= units[i]:
            cnt = N // units[i]
            unit_cnt[i] += cnt
            N %= units[i]
    print(f'#{test_case}')
    print(*unit_cnt)

