number = int(input())
    
result = 0
num = 0

while number != 0:
    result = number % 10
    number = number // 10
    num += result
print(num)



