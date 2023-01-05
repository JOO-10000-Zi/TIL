import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input()
    moeum = ['a', 'e', 'i', 'o', 'u']
    sick_word = []
    for i in moeum:
        if i in word:
            word = word.replace(i, "")
            
    print(f'#{test_case} {word}')