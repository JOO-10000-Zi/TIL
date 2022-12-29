import sys
sys.stdin = open("14467.txt")
N = int(input())

cow_dic = {

}
cnt = 0
for _ in range(N):
    cow, move = map(int, input().split())
    if cow not in cow_dic:
        cow_dic[cow] = move
    else:
        if cow_dic.get(cow) != move:
            cnt += 1
            cow_dic[cow] = move


print(cnt)
