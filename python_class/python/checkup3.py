# 실습문제 풀이 3번
a = 0
reselt = 0
n = int(input())

while a < n:
    a += 1
    reselt += a
print(reselt)

a = 0
reselt = 0
n = int(input())

for a in range(n):
    a += 1
    reselt += a
print(reselt)