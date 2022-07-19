from math import remainder
from re import A


number = int(input())
    
result = 0
num = 0

while number != 0:
    result = number % 10
    number = number // 10
    num += result
print(num)

# 강사님 풀이

numbers = 123

# result = 0
# while numbers:
#     result += numbers%10
#     numbers //= 10
numbers, remainder = divmod(numbers, 10)
result += remainder

print(result)
