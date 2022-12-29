import sys
sys.stdin = open("1764.txt")

N, M = map(int, input().split())

name = {}
for _ in range(N+M):
    human = input()
    if human not in name:
        name[human] = 1
    else:
        if human in name:
            name[human] += 1

bojab = []
for k, v in name.items():
    if name[k] == 2:
        bojab.append(k)
answer = sorted(bojab)

print(len(answer))
for i in answer:
    print(i)