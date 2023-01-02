import heapq

N = int(input())

heap = []
for _ in range(N):
    numbers = int(input())
    heapq.heappush(heap, numbers)

while len(heap) !=0:
    print(heapq.heappop(heap))