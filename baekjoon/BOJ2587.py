numbers = []

for _ in range(5):
    numbers.append(int(input()))
    
numbers.sort()


print(int((sum(numbers)/5)), numbers[2])
    