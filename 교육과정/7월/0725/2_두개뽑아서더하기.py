# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    
    set_ = set()
    for i in range(numbers):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            
            sum_ = n1 + n2
            set_.add(sum_)
    list_ = list(set_)
    answer = sorted(list_)
                
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
