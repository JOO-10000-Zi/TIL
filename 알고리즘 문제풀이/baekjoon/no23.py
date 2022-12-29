import sys
from pprint import pprint
sys.stdin = open("no23.txt")

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

graph_list = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph_list[v1].append(v2)

pprint(graph)
print(graph_list)
