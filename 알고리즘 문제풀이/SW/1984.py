
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers = input().split(' ')
    new_n = []
    print(numbers)
    for i in numbers:
        if i != '':
            new_n.append(int(i))
    print(new_n)
    sum_n = sum(new_n)
    avg_num = round((sum_n - max(new_n) - min(new_n)) // 8, 0)
    print(avg_num)