
number = int(input())

result = 0

while number != 0:
    result = number % 10
    number = number // 10
    

    print(result,end="")


# 강사님 풀이

# number = 123

# resul = 0
# while number:
#     result *= 10
#     result += number % 10
#     number //= 10


