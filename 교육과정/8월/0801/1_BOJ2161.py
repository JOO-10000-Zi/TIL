from collections import deque

N = int(input())

card_list = []
card_list = deque(card_list)    # deque로 현병환
for i in range(1, N+1):
    card_list.append(i)
# print(card_list.popleft())
return_list = []
# return_list = card_list[0]

return_list.append(card_list.popleft())
for j in list(card_list)[1:]:
    card_list.append(card_list.popleft())
    return_list.append(card_list.popleft())
    

print(*return_list, *list(card_list), end=" ")