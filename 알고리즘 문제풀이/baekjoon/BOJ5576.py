
K = []
Y = []
for i in range(20):
    score = int(input())
    if i < 10 :
        K.append(score)
    else:
        Y.append(score)
    K.sort(reverse=True)
    Y.sort(reverse=True)

print(sum(K[0:3]), sum(Y[0:3]))
