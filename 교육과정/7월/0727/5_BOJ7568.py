H = int(input())

max_Human = []

for i in range(1, H+1):
    W, hi = map(int, input().split())
    max_Human.append((W, hi))

ranks = [0] * H
for a in range(H):
    A  = max_Human[a]
    for b in range(H) :
        B = max_Human[b]

        if A[0] > B[0] and A[1] > B[1]:
            ranks[b] += 1
for rank in ranks:
    print(rank+1, end=" ")
