import numpy as np


N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))


avg = round(sum(numbers) / len(numbers))
center = np.median(sorted(numbers, reverse=False))
