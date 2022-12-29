import sys
import heapq
N = int(input())
heap = []
for _ in range(N):
    numbers = int(input())
        
    if numbers != 0 :
        heapq.heappush(heap, (abs(numbers),numbers))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            