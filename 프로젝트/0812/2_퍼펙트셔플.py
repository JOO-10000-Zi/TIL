import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    word_card = list(input().split())
    L = len(word_card)//2
    card1 = []
    card2 = []
    if len(word_card)%2 == 0 :
        # 문장의 개수(길이)가 짝수 일때
        for j in range(L):
         #짝수 이기 때문에 word문의 2로 나눈 몫 만큼 순회(앞부분 추출)
            card1.append(word_card[j])
         # 앞부분을 추출 후 빈 리스트에 저장
        else:
          # 앞부분 추출 for문이 끝나면뒷 부분 추출 시작       
             for k in range(L):
              # #word 뒷부분 이기 때문데 나눈 몫만큼 더해서 뒷부분 출력
                card2.append(word_card[k+L])
                # 출력된 부분 별도 리스트 저장
    else:
        if len(word_card)%2 == 1 :
                    # 문장의 개수(길이)가 홀수 일때
            for j in range(L+1):
                 #홀수 이기 때문에 word문의 2로 나눈 몫+1 만큼 순회(앞부분이 한장더 있다)
                card1.append(word_card[j])
                # 앞부분을 추출 후 빈 리스트에 저장
            else:
               # 앞부분 추출 for문이 끝나면뒷 부분 추출 시작       
                for k in range(L):
                # #word 뒷부분 이기 때문데 나눈 몫만큼 더해서 뒷부분 출력 단 홀수면 앞장이 1장더 가져가기 때문에 인덱스 번호 + 1추가
                    card2.append(word_card[k+L+1])
                # 출력된 부분 별도 리스트 저장
        
    list_card = []
    if len(word_card)%2 == 0:
        # 짝수 일때 반복문 실행
        for i in range(L):
            # word를 2로 나눈 몫만큼 반복
            list_card.append(card1[i])
            list_card.append(card2[i])
            # 각 리스트를 인덱스값으로 출력해서 빈 리스트에 순서대로 저장
    else:
        # 홀수 있때 마지막 한장을 위한 반복문
        if len(word_card)%2 == 1:
            for j in range(L):
                list_card.append(card1[j])
                list_card.append(card2[j])
            else:
                # 반목문이 다 돌고 난 후 마지막 카드를 따로 추가
                list_card.append(card1[L])
   
    print(f'#{test_case}', *list_card)
            
        