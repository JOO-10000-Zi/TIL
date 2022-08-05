import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(N)]

    die_pari = []
    for i in range(N-1):
        for j in range(N-1):
            die_pari.append(pari[i][j] + pari[i][j] + pari[i][j]+pari[i][j])
    print(f'#{test_case} {max(die_pari)}')

    ## M 만큼의 인덱스 조회를 통해서 값을 얻으려고 했으나
    ## 첫번째 예시는 수작업으로 했는데 두번째 예시 부터 틀렸네요 ㅠㅠ
    