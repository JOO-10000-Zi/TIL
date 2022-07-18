import random

n=int(input())
for i in range(n):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    print(numbers, type(numbers))
