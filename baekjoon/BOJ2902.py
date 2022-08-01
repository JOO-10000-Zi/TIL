names = input().split("-")

name_sum = []
for i in names:
    for j in i[0]:
        name_sum.append(j)
print("".join(name_sum))    