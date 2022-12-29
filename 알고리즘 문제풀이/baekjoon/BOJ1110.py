N = int(input())

num = N
cnt = 0
while True:
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10) + c
    cnt += 1
    if num == N:
        break

print(cnt)