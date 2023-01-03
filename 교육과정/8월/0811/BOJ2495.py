import sys
sys.stdin = open("2495.txt")


for _ in range(3):
    num = input()
    cnt = 1 # 기본 값을 1로 설정 같은 값이 나오면 추가 하기 위함
    max_cnt = 1 # 큰 값이 들어오면 바꿔주기 위한 변수
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            cnt += 1
        # 인덱스위치의 값이 다음 인덱스 위치값과 같으면 1추가
        else:
            if max_cnt <= cnt:
        # 위 if 문이 아닐 경우 cnt 값보다 max 값이 적으면 cnt로 변경
                max_cnt = cnt
        # cnt 는 다시 1로 초기화
                cnt = 1
    if cnt > max_cnt :
        print(cnt)
    elif max_cnt == 1:
        # for문이 끝나고 나서 두 값이 같으면 1출력
        print(1)
    else:  
        print(max_cnt)
        # 두 값이 다르면 max_cnt 값을 출력

            


'''
cnt = 0
check_list = []
un_cnt = 0
for _ in range(1):
    num = input()
    cnt = 0
    check_list = []
    un_cnt = 0
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            cnt += 1
            if i == len(num)-2:
                cnt += 1
                check_list.append(cnt)
        else:
            un_cnt += 1
            cnt += 1
            check_list.append(cnt)
            cnt = 0
    if un_cnt == 8:
        print(1)
    else:
        print(cnt)
'''        


'''
import sys
sys.stdin=open("input/2495.txt")
cnt=0
check=0
length=[]
for i in range(3):
    number=input()
    cnt=0
    length=[]
    check=0
    for k in range(len(number)-1):
        if number[k] == number[k+1]:
            cnt+=1
            if k == len(number)-2:
                cnt+=1
                length.append(cnt)
        else:
            check+=1
            cnt+=1
            length.append(cnt)
            cnt=0
    if check ==8:
        print(1)
    else:
        print(max(length))
'''
