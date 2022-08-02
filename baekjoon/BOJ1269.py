N, M = map(int, input().split())

A = set(map(int, input().split())) # set로 형변환 하면 {} 로 변환
B = set(map(int, input().split()))

# print(A)
# print(B)
print(len(A-B) + len(B-A))

# cnt = 0
# for i in set(B) :
#     if i not in set(A):
#         cnt += 1

# for i in set(A) :    
#     if i not in set(B):
#         cnt += 1
# print(cnt)
