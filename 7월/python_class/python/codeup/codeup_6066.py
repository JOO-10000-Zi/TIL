a, b, c = map(int, input().split())

num = []
num = a, b, c

for i in num:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
