import sys
import heapq

N = int(input())

ssulme = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 0:
        if len(ssulme) == 0:
            print(-1)
        else:
            gift = -heapq.heappop(ssulme)
            # 썰매에 선물이 있으면 팝으로 뽑아서 선물에 넣는다
            print(-gift)
    else:
        ssulme = a[1:]
        ssulme.sort(reverse=True)
        # 썰매 리스트에 받은 값의 0번재 제외하고 입력

#######################################################
################## 구글링 한 코드 ######################
#######################################################

import heapq

n = int(input())
gift = []

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(gift) == 0:
            print(-1)
        else:
            tmp = -heapq.heappop(gift)
            print(tmp)
    else:
        for j in range(a[0]):
            heapq.heappush(gift, -a[j + 1])
            print(gift)
