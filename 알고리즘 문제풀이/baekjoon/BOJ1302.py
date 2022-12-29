import sys
sys.stdin = open("1302.txt")

N = int(input())

book ={}
for _ in range(N):
    title_ = input()
    if title_ not in book:
        book[title_] = 1
    else:
        if title_ in book:
            book[title_] +=1


list_ = []
for k, v in book.items():
    point = book[k]
    list_.append(point)
max_ = max(list_)

best_book = []
for k, v in book.items():
    if book[k] == max_:
        best_book.append(k)

answer_ = sorted(best_book)
print(answer_[0])


