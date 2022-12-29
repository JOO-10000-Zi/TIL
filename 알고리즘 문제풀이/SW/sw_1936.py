T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    # 가위는 1, 바위는 2, 보는 3
    if A == 1:
        if B == 2:
            print('B')
        else:
            if B == 3:
                print('A')
    if A == 2:
        if B == 1:
            print('A')
        else:
            if B == 3:
                print('B')
    if A == 3:
        if B == 1:
            print('B')
        else:
            if B == 2:
                print('A')