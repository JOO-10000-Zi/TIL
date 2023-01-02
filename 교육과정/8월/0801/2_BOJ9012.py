from collections import deque

T = int(input())

for _ in range(T):

    word = input()

    
    chek_list1 = deque(word)
    list_gyal = []
    # print(chek_list1)
    for i in list(chek_list1):
        if i == "(":
            list_gyal.append(i)
        elif i == ")":
            list_gyal.append(i)
            
        if list_gyal.count("(") < list_gyal.count(")"):
            print("NO")
            break

    if list_gyal.count("(") == list_gyal.count(")"):
        print("YES")
    elif list_gyal.count("(") > list_gyal.count(")"):
        print("NO")
            