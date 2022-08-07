N = int(input())


result = 0
for i in range(1, N+1):
    if i < 100 :
        result += 1
    else:
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            result += 1            
print(result)
