T = int(input())

Q_dic = {
    "Q1" : 0,
    "Q2" : 0,
    "Q3" : 0,
    "Q4" : 0,
    "AXIS" : 0
}

for _ in range(T):
    X, Y = map(int, input().split())
    if X == 0 or Y == 0:
        Q_dic["AXIS"] += 1
    elif  X > 0 and Y > 0:
        Q_dic["Q1"] += 1
    elif  X < 0 and Y > 0:
        Q_dic["Q2"] += 1
    elif  X < 0 and Y < 0:
        Q_dic["Q3"] += 1
    else:
        Q_dic["Q4"] += 1
for k, v in Q_dic.items():
    print(f'{k}: {v}')
