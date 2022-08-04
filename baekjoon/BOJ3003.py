from collections import deque

mar_main = [1, 1, 2, 2, 2, 8]

number = list(map(int, input().split()))


result = []
result = deque(number)
mar = []

for i in range(len(number)):
    if result[i] == mar_main[i]:
        mar.append(0)
    elif result[i] > mar_main[i]:
        mar.append(mar_main[i] - result[i])
    elif result[i] < mar_main[i]:
        mar.append(mar_main[i] - result[i])

print(*mar)

