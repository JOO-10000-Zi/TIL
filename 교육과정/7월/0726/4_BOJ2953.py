

T = 5

total = []
for i in range(1, T+1):
    a, b, c, d =map(int, input().split())
    point = a + b + c + d
    total.append(point)
    # 인수로 받은 4개의 점수를 더해서 total 리스트에 append
    # 자동으로 값이 입력된 순서대로 정령 된다
idx = total.index(max(total)) + 1
    # 점수가 가장 높은 사람의 순서를 구하기 귀해서 리스트에
    # 순서대로 정리된 점수중 가장 높은 점수의 인덱스를 구하는데
    # 인덱스는 0 부터 시작 하기 때문에 +1 을 해서 1번부터 시작하도록 변경
print(f'{idx} {max(total)}')