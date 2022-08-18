import sys
sys.stdin = open("2851.txt")

sum_point = 0
sum_list = []
for _ in range(10):
        point_ = int(input())
        sum_list.append(point_)
        sum_point += point_
        if sum_point >= 100:
            break
b = sum_point - 100
a = 100 - (sum_point - sum_list[-1])
if b == a:
    print(sum_point)
elif b  >  a:
    print(sum_point - sum_list[-1])
elif b  <  a:
    print(sum_point)

