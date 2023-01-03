import sys
sys.stdin = open("11724.txt")

N, M = map(int, input().split())

yoso = [[] for _ in range(N+1)]
yoso_cnt = [False] * (N+1)
cnt = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    yoso[v1].append(v2)
    yoso[v2].append(v1)

    start = 1
    yoso_cnt[start] = True
    stack =[start]

    while stack:
        cur = stack.pop()

        for i in yoso[cur]:
            if not yoso_cnt[i]:
                yoso_cnt[i] = True
                stack.append(i)
    cnt += 1

print(cnt)    
print(yoso)
print(yoso_cnt)

