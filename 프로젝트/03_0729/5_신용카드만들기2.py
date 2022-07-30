import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card_N = input()
    number = card_N.replace("-","")
    len_number = len(number)
    for i in card_N[0]:
 
        if (i == "3" or i == "4" or i == "5" or i == "6" or i == "9") and len_number == 16:
                                                  print(f'#{test_case} 1')
        else:
                                                  print(f'#{test_case} 0')