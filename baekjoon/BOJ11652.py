import sys
sys.stdin = open("11652.txt")

N = int(input())

card = {}
#  딕셔너리 card를 만들어서 담는다
for _ in range(N):
    card_N = int(input())
    if card_N not in card:
        card[card_N] = 1
    else:
        if card_N in card:
            card[card_N] += 1
#  값이 없으면 1로 시작 있으면 +1 한다

cnt_ = []
# 벨류 값만 있는 리스트를 만든다 MAX값을 구하기 위함
for k, v in card.items():
    cnt_.append(card[k])
MAX_ = max(cnt_)

# MAX와 같은 키를 찾는다
MAX_card = []
for k, v in card.items():
    if card[k] == MAX_:
        MAX_card.append(k)

p = sorted(MAX_card)

print(p[0])