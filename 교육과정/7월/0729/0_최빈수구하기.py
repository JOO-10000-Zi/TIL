import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_n = int(input())
    porints = map(int, input().split())
    score_ = {}
    
    for i in porints:
        if score_.get(i) is none:
            score_[i] = 1
        else:
            score_[i] += 1
    max_point = max(score_.values())
    max_list = {}
    for k, v in score_.items():
        if v == max_point:
            max_list[k] = v
answer_ = 
print(f'{test_case} ')       