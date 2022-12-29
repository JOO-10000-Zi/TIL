import sys
sys.stdin = open("SWEA1204.txt")
from pprint import pprint
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    points = {}
    cnt = 0
    double_p = []
    n = int(input())
    point_list = list(map(int, input().split()))
    for i in point_list:
        if i not in points:
            points[i] = 1
        else:
            if i in points:
                points[i] += 1
    for k, v in points.items():
        if v > cnt:
            cnt = v
    for k, v in points.items():
        if v == cnt:
            double_p.append(k)
    max_db = max(double_p)
    print(f'#{test_case} {max_db}')

