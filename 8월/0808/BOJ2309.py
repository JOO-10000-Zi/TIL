list_ = [int(input()) for i in range(9)]

sum_ = sum(list_)

for i in range(9):
    for j in range(i+1, 9):
        if 100 == sum_ - (list_[i] + list_[j]):
            num1, num2 = list_[i], list_[j]

            list_.remove(num1)
            list_.remove(num2)
            list_.sort()

            for i in range(len(list_)):
                print(list_[i])
            break
    if len(list_) < 9 :
        break