import sys
from pprint import pprint
sys.stdin = open("2606.txt")

N = int(input())
M = int(input())
check_list =[[] for _ in range(N+1)]
cnt_list = [False] * (N+1)
cnt = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    check_list[v1].append(v2)
    check_list[v2].append(v1)
pprint(check_list)


def dfs(cnt_list):
    stack = [cnt_list]
    cnt_list[0] = True
    while stack:
        cur = stack.pop()

        for adj in check_list[cur]:
            if not cnt_list[adj]:
                cnt_list[adj] = True
                stack.append(adj)
print(cnt_list)