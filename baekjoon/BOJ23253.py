import sys
sys.stdin = open("23253.txt")

N, M = map(int, input().split())

p = True
for _ in range(M):
    book1 = int(input())
    book1_list = list(map(int, input().split()))
    for i in range(book1 - 1):
        if book1_list[i] < book1_list[i+1]:
            p = False
            break
    if not p : break

print('Yes' if p else 'No')
    

        



# N = list(map(int, input().split()))
# M1 = int(input())
# N_list1 = list(map(int, input().split()))
# M2 = int(input())
# N_list2 = list(map(int, input().split()))


# sort_list = []
# while len(N_list1) != 0 and len(N_list2) != 0:
#     sort_list.append(N_list1.pop())
#     sort_list.append(N_list2.pop())

# result = []

# for i in range(1, N[0]+1):
#     result.append(i)

# if sort_list == result :
#     print("YES")
# else:
#     print("NO")
# # print(sort_list)

