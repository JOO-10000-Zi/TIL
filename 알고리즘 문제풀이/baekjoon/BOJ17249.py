import sys
sys.stdin = open("17249.txt")


tabo = input()
cnt = 0
for i in range(len(tabo)):
    if tabo[i] == "@":
        cnt += 1
    if tabo[i] == "(":
        print(cnt, end= " ")
        cnt = 0
print(cnt)

