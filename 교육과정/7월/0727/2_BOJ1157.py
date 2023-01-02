name = input().upper()
# 문자열을 입력하는 과정에서 대문자로 변경 한다
word_list = list(set(name))
# 입력된 문자의 중복을 제거하고 리스트로 만든다 마지막에 문자를 찾기 위함
name1 = []
for i in word_list:
    cnt = name.count(i)
    # name을 i가 있는 수를 카운트
    name1.append(cnt)
    # 카운트 된 수를 name1 리스트에 저장
if name1.count(max(name1)) > 1:
    print('?')
else :
    max_index = name1.index(max(name1))
    print(word_list[max_index])
