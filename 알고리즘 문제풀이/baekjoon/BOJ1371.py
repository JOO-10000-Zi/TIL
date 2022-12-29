import sys
import string
sys.stdin = open("123.txt")

abc = string.ascii_lowercase

word_list = {}

for i in abc:
    word_list[i] = 0

while True:
    try:
        long_word = list(input())
        for i in long_word:
            if i in word_list:
                word_list[i] += 1     
    except:
        break
max_word = max(word_list.values())
for k, v in word_list.items():
    if v == max_word:
        print(word_list.get(v, k), end="")