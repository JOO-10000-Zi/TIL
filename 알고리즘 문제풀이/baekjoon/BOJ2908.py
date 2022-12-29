a, b = map(int, input().split())
c = str(a)
d = str(b)
c = c[::-1]
d = d[::-1]

print(max(int(c),int(d)))