N, K = map(int, input().split())

coin_lst = list()

for i in range(N):
    coin_lst.append(int(input()))
    # N만큼 금액 받기

count = 0
for i in reversed(range(N)):
    # 리버스로 거꾸로 길이만큼 인덱스 값 받기
    count += K // coin_lst[i]
    # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K % coin_lst[i]
    # K는 동전으로 나눈 나머지로 계속 반복

print(count)
