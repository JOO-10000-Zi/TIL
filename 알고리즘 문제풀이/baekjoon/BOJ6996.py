import sys
sys.stdin = open("6996.txt")

T = int(input())

for _ in range(T):
    N1, N2 = input().split()

    word_dic = {}
    cnt_word = []
    cnt = 0
    for i in N1:
        if i not in word_dic:
            word_dic[i] = 1
        else:
            word_dic[i] += 1

    for j in N2:
        if j in word_dic:
            word_dic[j] -= 1
        if j not in word_dic:
            word_dic[j] = 1
    
    for k, v in word_dic.items():
        cnt_word.append(v)

    for k in cnt_word:
        if k != 0:
            cnt += 1
    
    if cnt > 0:
        print(f'{N1} & {N2} are NOT anagrams.')
    elif cnt == 0:
        print(f'{N1} & {N2} are anagrams.')