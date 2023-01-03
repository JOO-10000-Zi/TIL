import sys
sys.stdin = open("17388.txt")

University = list(map(int, input().split()))

chamyedo = sum(University)

if chamyedo >= 100 :
    print("OK")
else:
    if min(University) == University[0]:
        print('Soongsil')
    if min(University) == University[1]:
        print("Korea")
    if min(University) == University[2]:
        print('Hanyang')