T = int(input())

for _ in range(T):
    all_ = list(map(int, input().split()))
    student = all_[0]
    total = sum(all_[1:])
    avg_ = total/student
    cnt_ = 0
    for i in all_[1:]:
        if avg_ < i:
            cnt_ += 1

    avg_student = cnt_/student
    print(format(avg_student*100,'0.3f')+'%')


