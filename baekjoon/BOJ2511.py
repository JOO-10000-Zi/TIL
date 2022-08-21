from itertools import count
import sys
sys.stdin = open("2511.txt")

A_card = []
B_card = []
for i in range(2):
    card_num = list(map(int, input().split()))
    if i == 0:
        A_card = card_num
    if i == 1:
        B_card = card_num

A_point = 0
B_point = 0
check_list = "D"
for j in range(10):
    if A_card[j] > B_card[j]:
        A_point += 3
        check_list = "A"
    if A_card[j] < B_card[j]:
        B_point += 3
        check_list = "B"
    if A_card[j] == B_card[j]:
        A_point += 1
        B_point += 1

print(A_point, B_point)
if check_list.count("D") == 10:
    print("D")
else:
    if A_point > B_point:
        print("A")
    if B_point > A_point:
        print("B")
    if A_point == B_point:
        print(check_list)
                
# print(check_list)
# if A_point > B_point:
#     print("A")
# if A_card ==  B_card:
#     print("D")
