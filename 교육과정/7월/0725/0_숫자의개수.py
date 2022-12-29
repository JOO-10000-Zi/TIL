# https://www.acmicpc.net/problem/2577
from dis import code_info
from itertools import count
import sys

sys.stdin = open("0_숫자의개수.txt")
# A,B,C 에 인수가 입력 되면 곱한다
# 곱하여 나온 값에 각각의 숫자가 몇개씩 사용된 수를 카운트 한다
# 각 타운트 된 값은 0 ~ 10 까지 차레로 출력 한다.
# A, B, C = map(int, input().split('\n'))
A = int(input())
B = int(input())
C = int(input())

gob = A * B * C

numbers = [0, 1, 2, 3, 4, 5, 6, 7,8, 9]
cnt = [0] * 10
for i in str(gob):
    for j in numbers:
        if int(i) == j:
            cnt[j] += 1
for k in cnt:
    print(k)
    



   





