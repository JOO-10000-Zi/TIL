numbers = [0, 20, 100, 80]
max_number = numbers[0]
second_number = numbers[0]


for n in numbers:
    if max_number < n:
        second_number = max_number
        max_number = n

print(second_number)

