import sys
sys.stdin = open('3986.txt')

N = int(input())

cnt = 0

for _ in range(N):
    good = input()
    stack = []
    for i in good:
        if len(stack) == 0 :
            stack.append(i)
        else:
            if i == "A":
                if stack[-1] == "B":
                    stack.append(i)
                elif stack[-1] =="A":
                    stack.pop()
            elif i == "B":
                if stack[-1] == "A":
                    stack.append(i)
                elif stack[-1] == "B":
                    stack.pop()
    if len(stack) == 0:
        cnt += 1


print(cnt)            