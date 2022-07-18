
# 딕셔너리 기초내겸 설명
# word = 'banana'

# result = {}

# for char in word:
#     if char not in result:
#         result[char] = 1
#     else:
#         result[char] += 1



# # result['a'] = 0

# print(result)

# 예외처리 test/ 예외처리문 수업 따라하기
numbers = input('숫자를 입력하세요 : ')

try:
    print(100/int(numbers))
except ZeroDivisionError:
    print('0으로 나눌수는 없습니다.')
except ValueError :
    print('숫자 형식을 입력해요.')





