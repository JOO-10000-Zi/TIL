import sys

sys.stdin = open("_Flatten.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump_cnt = int(input())
    num = list(map(int, input().split()))
	
    for _ in range(dump_cnt):
        # 덤프 횟수 만큼 반복
        for i in num:
		# num 을 하나씩 순회하면서 해당 값이 num리스트의 max값과 같을때
            if i == max(num):
        # max, min 값으로 인덱스를 다시 조회해서 가장 큰 값과 작은 값을 각각 -1, +1 해준다
                num[num.index(min(num))] = min(num) + 1
                num[num.index(max(num))] = max(num) - 1
                
    answer = max(num) - min(num)
    print(f'#{test_case} {answer}')

    ###########################################
    # 큰값과 작은 값이 각각 줄고 커지면서 평탄화 작업 코드를 만들었습니다
    # 작동은 되고 작은 값으로도 해보고 텍스트 파일로도 해봤는데 정답이 안나오네요...