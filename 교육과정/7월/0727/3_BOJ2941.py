
# 입력 값을 크로아티아 문자형태로 있는지 비교
# 크로아티아 알파벳이 있으면 리스트에 넣기
# 크로아티아 문자를 제외하고 영어 카운트...
# 리스트를 카운트 한다
word = input()
cro_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in cro_word:
#     word = word.replace(i, "*")
# print(len(word))

a = []
b = []
for i in cro_word:
    while i in word :
        a.append(i)
        word = word.replace(i," ",1)
for j in a:
        word = word.replace(j,"")
        b.append(word)
    
for x in b[-1].replace(" ",""):
    a.append(x)

print(len(a))