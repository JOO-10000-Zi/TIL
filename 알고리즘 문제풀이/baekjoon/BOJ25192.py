import sys
sys.stdin = open("25192.txt")

N = int(input())

gomgom = {}
cnt = 0

for _ in range(N):
    name_ = input()

    if name_ == "ENTER":
        for k, v in gomgom.items():
            if v == 1:
                cnt +=1
        gomgom={}
    else:
        if name_ not in gomgom:
            gomgom[name_] = 1

for k, v in gomgom.items():
    if v == 1:
        cnt += 1

print(cnt)
