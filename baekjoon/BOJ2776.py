import heapq
from collections import deque

T = int(input())

note1_ = []
note2_ = []
for _ in range(T):
    note1_num = int(input())
    # for _ in range(note1_num):
    note1_list = list(map(int, input().split()))
    for i in note1_list:
        heapq.heappush(note1_, i)

    note2_num = int(input())
    # for _ in range(note2_num):
    note2_list = list(map(int, input().split()))
    for j in note2_list:
        heapq.heappush(note2_, j)
    
check_ = []
check_ = deque(note2_)

for _ in range(note1_num):
    if  check_.popleft() in note1_ :
        print(1)
    else:
        print(0)