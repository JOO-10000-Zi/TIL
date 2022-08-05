import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mobumseng_N = list(map(int, input().split()))
    gganbu = list(map(int, range(1, N+1)))
    list_ = []
    list_.sort
    for i in range(N) :
        if gganbu[i] not in mobumseng_N:
            list_.append(gganbu[i])
    print(f'#{test_case}', *list_)
             
        