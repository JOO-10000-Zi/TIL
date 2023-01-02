from pprint import pprint
N = 8

pan = []
for _ in range(N):
    mar = list(input())
    pan.append(mar)


cnt = 0

for i in range(N):
    #  체스판 이기 때문에  8 * 8 이라서 8번씩 조회
    for j in range(8):
        # 순회 되면서 추출된 i, j 의 위치 값이 짝수인 수와
        # pan[i][j]의 인덱스값을 통해 위치의 값이 F와 같은지 비교
        if (i + j) % 2 == 0 and pan[i][j] == "F":
        # if i + j) % 2 == 0:
        #    pan[i][j] == "F":
            cnt += 1
            # 비교가 맞으면 카운트 +1 증가
        

pprint(cnt)

