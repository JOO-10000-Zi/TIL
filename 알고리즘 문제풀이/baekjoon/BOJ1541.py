A = input()

number = []
c = []
for i in A:
    if i != "-" or i != "+":
        c += i


print(len(c))
