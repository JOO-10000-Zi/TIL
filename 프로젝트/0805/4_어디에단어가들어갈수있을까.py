import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 제한 시간에는 다 못풀 었지만 자습 시간에 천천히 생각해보고
# 마지막에 고수님들의 조금 도움을 얻었습니다
# 한줄에 K로 주어진 문장의 길이 값이 중복 나오는 걸
# break 해서 모두 체크하지 못해서 예시 10개중 7개만 맞았었는데
# 그부분 수정 하진 패스했네요...
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    word_pz =[list(map(int, input().split())) for _ in range(N)]
    
    zari = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_pz[i][j] == 1:
                cnt += 1
            else:
                if cnt != K :
                    cnt = 0
                if cnt == K:
                    zari += 1
                    cnt = 0
        if cnt == K:
            zari += 1
#        print(cnt, zari)
    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_pz[j][i] == 1:
                cnt += 1
            else:
                if cnt != K:
                    cnt = 0
                if cnt == K:
                    zari += 1
                    cnt = 0
        if cnt == K:
            zari += 1
#        print(cnt, zari)
    print(f'#{test_case} {zari}')

##########################################################################
############## 모의고사때 작성한 코드 ######################################
##########################################################################

'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    word_pz =[list(map(int, input().split())) for _ in range(N)]
    
    zari = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_pz[i][j] == 1:
                cnt += 1
            if cnt == 3:
                zari += 1
            if cnt > K :
                zari -= 1
                cnt =0
            if word_pz[i][j] == 0:
                if cnt == 3:
                    zari += 0
                else:
                    cnt = 0
                    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if word_pz[j][i] == 1:
                cnt += 1
            if cnt == 3:
                zari += 1
            if cnt > K :
                zari -= 1
                cnt =0
            if word_pz[i][j] == 0:
                if cnt == 3:
                    zari += 0
                else:
                    cnt = 0

        print(cnt, zari)
'''
# 행열을 순회 하면서 1이 나오면 1식 더해서 3이면 자리 카운트 1 하고
# 0이 나오면 현재 카운트 개수를 확인해서 3이면 카운트를 0으로 돌려주는
# 방식으로 접근 을 했는데 값이 틀리네요..... 1시간 30분넘게 붙잡고 있다가
# 포기 했습니다... 이거 하느라 다른건 못풀 었네요..
# 1번 예시를 맞추면 2번에서 틀리고.... if문 순서가 중요한거 같은데 모르겠네요 ㅠ

    #print(f'#{test_case} {zari},{zari2}')