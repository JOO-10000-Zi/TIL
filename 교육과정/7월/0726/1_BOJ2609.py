a, b = map(int, input().split())

# 인수로 받은 각가의 수를 그 수만큼 1부터 순회하는 값으로 나누어
# 0이 되는 값을 약수로 추출해 낸다

a1 = []
b1 = []
for i in range(1, a+1):
    if a%i == 0:
        a1.append(i)
# a 인수의 값 만큼 순회 하면서 a%i 한 나머지가 0이 아니면  a1리스트에 업데이트한다
for j in range(1, b+1):
    if b%j == 0 :
        b1.append(j)

yeak = [i for i in a1 if i in b1]
max_yeak = max(yeak)
a2 = a//max_yeak
b2 = b//max_yeak
min_yeak = a2 * b2 * max_yeak
print(max_yeak)
print(min_yeak)