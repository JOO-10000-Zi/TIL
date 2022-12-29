eumgay = list(map(int, input().split()))

result = [1, 2, 3, 4, 5, 6, 7, 8]

if eumgay == result:
    print('ascending')
elif eumgay == result[::-1]:
    print("descending")
else:
    print("mixed")
