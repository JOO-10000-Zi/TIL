result_num = set(range(1, 10001))
d_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    d_num.add(i)

self_num = sorted(result_num - d_num)
for i in self_num:
    print(i)