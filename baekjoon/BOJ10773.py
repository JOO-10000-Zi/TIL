N = int(input())

input_list = []
for _ in range(N):
    # inputs = [3, 0, 4, 0]
    input_list.append(int(input()))

scack =[]

for i in input_list:
    if i != 0:
        scack.append(i)
    else:
        scack.pop()

print(sum(scack))
