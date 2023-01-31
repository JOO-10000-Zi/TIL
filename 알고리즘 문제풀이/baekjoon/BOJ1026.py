N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_sum = 0
for i in range(N):
    min_sum += min(A) * max(B)
    # A리스트의 최소값과 B리스트의 최대값을 뽑아서 계산한다.(누적 합산)
    A.pop(A.index(min(A)))
    # A리스트의 최소값을 계산 후에 pop 해서 제거한다.
    B.pop(B.index(max(B)))
    # B리스트의 최대값을 계산 후 pop 해서 제거한다.

print(min_sum)
