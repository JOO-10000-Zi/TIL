n = int(input())
a = list(map(int, input().split()))
a.sort()
# 입력 받은 수를 오름 차순으로 정렬
x = int(input())

i = 0
# 인덱스 값을 통해 좌, 우 위치 값을 주기 위해 0부터 시작
j = n - 1
# 배열의 수로 입력된 n 에서 -1을 해서 인덱스 값을 찾아 맨 마지막 인덱스 찾기
cnt = 0
# 쌍의 수를 카운트 하기 위해

while True:
    if a[i] + a[j] == x:
        cnt += 1
    # 쌍의 수를 찾는 값과 같으면 개수 증가

    if a[i] + a[j] < x:
        i += 1
    # 좌측 인덱스 값 변경을 위해 x보다 작으면 i 에 1을 더해 한칸 옆으로 이동
    else:
        j -= 1
    # 쌍의 값과 같은 수이면 우측을 한칸 줄이기 위해 j에 -1을 실행
    if i >= j:
        break
    # 좌측 인덱스 i와 우측 인덱스 j 가 같거나 i가 크면 멈춤

print(cnt)
