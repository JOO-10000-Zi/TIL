import sys

sys.stdin = open("_창용마을무리의개수.txt")


#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    
    maeul = [[]  for _ in range(n+1)]
    check_list = [False] * (n+1)
    

    for _ in range(m):
        R1, R2 = map(int, input().split())
        maeul[R1].append(R2)
        maeul[R2].append(R1)
    
    start = 1
    stack = [start]
    check_list[start] = True
    cnt = 0
    for _ in range(n):
        human = stack.pop()

        for adj in maeul[human]:
            if human in maeul[adj] :
                stack.append(adj)
                check_list[adj] = True          
    cnt += 1
    
    for i in check[1:]:
        if 
        start = 
        stack = [start]
        check_list[start] = True
        for _ in range(n):
            human = stack.pop()

            for adj in maeul[human]:
                if human in maeul[adj] :
                    stack.append(adj)
                    check_list[adj] = True          
    cnt += 1
    
    print(check_list)
    print(cnt)
 