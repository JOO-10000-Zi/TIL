import sys

sys.stdin = open("_직사각형길이찾기.txt")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sagak = list(map(int, input().split()))
    
    line_ = {}
    for i in sagak:
        if i not in line_:
            line_[i] = 1
        else:
            line_[i] += 1
            
    print(line_)
    print(f'#{test_case} {min(line_, key=line_.get)}')
# 수가 몇 번 있는지 카운트 한 후 
# 수가 2보다 작고 2보다 큰경우 값을 출력 할려고 했는데
# 마지막에서 막혔습니다...
# 딕셔너리 값 추가하는 방법이 생각이 안나서 결국 리스트로....