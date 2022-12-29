from pprint import pprint
import sys

sys.stdin = open("1652.txt", "r")

# 연속해서 빈칸이 2개 , 벽이나 짐에 한쪽이 닿아야 한다(중간 X)
# 가로 세로 다 가능 
T = int(input())
room_condition = [list(map(str, input())) for _ in range(T)]

sleep_cnt = 0

for i in range(T):
    cnt = 0
    for j in range(T):
        if room_condition[i][j] == ".":
            cnt += 1
        elif room_condition[i][j] == "X":
            if cnt >= 2:
                sleep_cnt += 1
            cnt = 0
    if cnt >= 2:
        sleep_cnt +=1
        cnt =0

sleep_cnt2 = 0
for j in range(T):
    cnt1 = 0
    for i in range(T):
        if room_condition[i][j] == ".":
            cnt1 += 1
        elif room_condition[i][j] == "X":
            if cnt1 >= 2:
                sleep_cnt2 += 1
            cnt1 = 0
    if cnt1 >= 2:
        sleep_cnt2 += 1
        cnt1 = 0

print(sleep_cnt, sleep_cnt2)