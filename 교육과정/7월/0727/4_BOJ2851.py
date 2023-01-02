
N = 10

scores = []
for i in range(N):
    score = int(input())
    scores.append(score)

sum_ = 0
min_ = 10e9
max_score = 0
for i in range(N):
    sum_ = sum_ + scores[i]
    
    diff = abs(100- sum_)
    
    if diff <= min_:
        min_ = diff
        max_score = sum_   
    
print(max_score)