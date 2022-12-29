import sys
from pprint import pprint
sys.stdin = open("10798.txt")

word_list = [[0] * 15 for _ in range(5)]
for i in range(5):
    word = list(input())
    word_len = len(word)
    for j in range(word_len):
        word_list[i][j] = word[j]
for i in range(15):
    for j in range(5):
        if word_list[j][i] == 0:
            continue
        else:
            print(word_list[j][i], end ='')


        
