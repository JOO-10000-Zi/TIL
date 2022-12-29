import sys
sys.stdin = open('11508.txt')

N = int(input())

uoosan = []
sum_pay = 0

for _ in range(N):
    pay = int(input())
    uoosan.append(pay)

uoosan_sort = sorted(uoosan, reverse=True)
for i in range(len(uoosan_sort)):
    if i % 3 < 2:
        sum_pay += uoosan_sort[i]

print(sum_pay)






#
#      if len(uoosan) == 3:
#         pay_sort = sorted(uoosan,reverse=True)
#         sum_pay += sum(pay_sort[0:2])
#         uoosan = []   
    
# total = sum_pay+sum(uoosan)
# print(total)


