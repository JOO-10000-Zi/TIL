x, y = input().split()

Re_x = x[::-1]
Re_y = y[::-1]
sum_ = int(Re_x) + int(Re_y)
rev_ = str(sum_)

print(int(rev_[::-1]))