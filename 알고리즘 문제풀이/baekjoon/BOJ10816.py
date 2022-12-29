import sys
sys.stdin = open("10816.txt")

N = int(input())

card = {}
card_n = input().split()
for i in card_n:
    if i not in card:
        card[i] = 1
    else:
        if i in card:
            card[i] += 1
print(card)

M = int(input())
answer = input().split()
for i in answer:
    if i in card:
        print(card[i], end=" ")
    else:
        if i not in card:
            print(0, end= " ")