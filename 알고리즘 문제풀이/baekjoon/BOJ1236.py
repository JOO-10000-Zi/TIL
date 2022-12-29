from pprint import pprint

N, M = map(int, input().split())

cnt_haang = 0
cnt_10 = 0
matrix = []
for _ in range(N):
    gard = list(input()) 
    matrix.append(gard)
    if "X" not in gard:
        cnt_haang += 1

for i in range(M):
    cnt_1 = 0
    for j in range(N):
        # print(matrix[j][i])
        if matrix[j][i] == "X":
            break
        else:
            cnt_1 +=1

    if cnt_1 == N:
        cnt_10 += 1

 
# pprint(matrix)
pprint(max(cnt_haang, cnt_10))
