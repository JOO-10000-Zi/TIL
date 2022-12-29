import sys
sys.stdin = open("25304.txt")

total_pay = int(input())

pay_cnt = int(input())

min_check = []
for _ in range(pay_cnt):
    pay, list_ = map(int, input().split())

    min_check.append(pay * list_)
if total_pay == sum(min_check):
    print("Yes")
else:
    print("No")