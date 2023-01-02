import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_n = int(input())
    score_ = list(map(int, input().split()))
     
    sum_pay = sum(score_)
    avg_ = sum_pay // len(score_)
    cnt = 0
    for i in score_:
        if i <= avg_:
            cnt += 1
     
    print(f'#{test_case} {cnt}')

    