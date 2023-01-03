import sys
sys.stdin = open("2857.txt")

random_list = []
FBI_list = []

for _ in range(5):
    name = input()
    random_list.append(name.upper())
for i in random_list:
    if "FBI" in i :
        FBI_list.append(i)
if FBI_list == [] :
    print("HE GOT AWAY!")

for i in FBI_list:
    print(random_list.index(i)+1, end=" ")