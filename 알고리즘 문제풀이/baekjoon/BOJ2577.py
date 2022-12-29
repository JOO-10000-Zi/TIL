A = int(input())
B = int(input())
C = int(input())

gob = A * B * C

numbers = [0, 1, 2, 3, 4, 5, 6, 7,8, 9]
cnt = [0] * 10
for i in str(gob):
    for j in numbers:
        if int(i) == j:
            cnt[j] += 1
for k in cnt:
    print(k)
    