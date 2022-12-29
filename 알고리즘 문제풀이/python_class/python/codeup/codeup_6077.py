a = int(input())

result = 0
for i in range(1, a+1):
    if i % 2 == 0:
        result += i

print(result)