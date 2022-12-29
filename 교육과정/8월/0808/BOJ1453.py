N = int(input())

sonnim = list(map(int, input().split()))

pc_space = []

# 첫번째 포함 
cnt = 0
for i in sonnim:
    if i not in pc_space:
        pc_space.append(i)
    else:
        cnt += 1

print(cnt)
