




answer = "YES"
stack_list = [[12, 4, 1], [9, 5, 2], [11, 8, 6], [10, 7, 3]]
# stack = [11, 10, 8, 5]

for stack in stack_list:
    comparison = stack.pop()

    while len(stack) != 0 :
        if stack[-1] > comparison:
            comparison = stack.pop()
        else:
            answer = "NO"
            break







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

