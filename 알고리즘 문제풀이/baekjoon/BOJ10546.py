import sys
sys.stdin = open("10546.txt")

N = int(input())

list_ = {}

for _ in range(N):
    name = input()
    if name not in list_:
        list_[name] = 1
    else:
        if name in list_:
            list_[name] += 1

for _ in range(N-1):
    name2 = input()
    if name2 in list_:
        list_[name2] -= 1

flex_human = []

for k, y in list_.items():
    if list_[k] == 1:
        flex_human.append(k)

print(*flex_human)