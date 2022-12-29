a, b = map(int, input().split())


soo10_list = []
result = 0
for i in range(100):
    for j in range(i):
        soo10_list.append(i)

for x in range(a-1, b):
    result = soo10_list[x] + result

print(result)
