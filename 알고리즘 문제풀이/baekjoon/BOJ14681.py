x = int(input())
y = int(input())

saboon = {}
saboon[x] = y

for k, v in saboon.items():
    if k > 0 and v > 0 :
        print(1)
    elif k < 0 and v > 0 :
        print(2)
    elif k > 0 and v < 0 :
        print(4)
    else :
        print(3)
 