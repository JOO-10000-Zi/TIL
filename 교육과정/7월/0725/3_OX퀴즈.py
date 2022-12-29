# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1, T+1):
    exit = input()
    # 반복문을 통해 O,X를 하나씩 뽑고 O일 경우 +1 하고
    # 다시 포인트에 더한 값을 누적 하여 합을 구하고
    # O가 아닐경우 0으로 리셋 후 다시 시작 한다
    point = 0
    cnt = 0
    for o in exit:
        if o =='O':
         cnt += 1
         point += cnt
        else:
            cnt = 0
         
    print(point)