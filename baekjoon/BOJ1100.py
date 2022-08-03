from pprint import pprint
N = 8

pan = []
for _ in range(N):
    mar = list(input())
    pan.append(mar)


cnt = 0

for i in range(N):
    for j in range(8):
        if (i + j) % 2 == 0 and pan[i][j] == "F":
        # if i + j) % 2 == 0:
        #    pan[i][j] == "F":
            cnt += 1
        

pprint(cnt)

