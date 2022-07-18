# -- coding: utf-8 --
# 예제 03번 실숩 풀이

# 오류 코드

# numbers = map(int, input().split())
# map 함수를 사용하여 input 되는 값을 int 스타일로 변경한다
# map를 사용 하지 않고 int(ipunt().split()) 로 하면
# numbers 는 list를 가질 수 없기 때문에 Error이 발생한다
# print(sum(numbers))

# 예제 04번 실습 풀이

# 오류 코드

# words = list(input().split())
# # map 함수를 사용해서 int로 받았기 때문에 
# # 문자열을 입력해서 오류가 발생 함
# print(words)

# 예제 05번 실습 풀이

### 오류 코드

# number = '22020718'
# print(len(number))
# int 속성은 갯수를 셀 수 없어서
# 문장 부호 ``를 사용하여 문자로 변환 함


# 예제 06번 실습 풀이

# 오류 코드
# N = 10
# answer = []
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)
# answer 를 ()로 묶으면 실행시 결과값이 튜플이 되기 때문에
# append 할수 없다는 오류가 나온다
# answer를 []로 리스트 타입으로 변경하면 정상적으로 실햄됨

# 예제 07번 실습 풀이

# 오류코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
#     count += 1

# print(total / count)
# count 위치가 for문안에서 반복이 되야 +1씩 증가가 되고
# print // 몫 만 구하는 수식으로 / 변경 해야 한다

# 예제 08번 실습 풀이

#오류 코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char in 'aeiou':
#         count += 1
# print(count)
# if char = 'a' or 'e' ... 이런식으로 사용 하면 'a'만
# 비교하기 때문에 제대로 인식이 안된다
# 따로 목록을 만들거나 char = 'a' or char =='e' ... 이런식으로
# 작성해야 인식 한다.


# 예제 09번 실습 풀이

#오류 코드
# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         # fruit_count 라는 딕셔너리에 없으면
#         fruit_count[fruit] = 1
#         # 딕셔너리에 '과일 : 1' 로 1 값을 지정 
#     else:
#         # 있으면 '과일 : +1' 동일하면 1씩 증가
#         fruit_count[fruit] += 1
    

# pprint(fruit_count)

# # 다른방법 추가 풀이
# result = {}
# for char in fruits:
#     result[char] = result.get(char, 0) + 1

# pprint(result)

# 예제 10번 실습 풀이

# 오류 코드

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max1 = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max1 > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max1 < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# # max 는 변수가 아니라 함수이기 때문에 함수를 변수로 지정하면서
# # 오류가 발생을 해서 두 번째 리스트의 max 값이 구해지지 않는
# 오류가 발생하였음

# 예제 11번 실습 풀이

# 오류 코드

# from pprint import pprint


# def movie_info(movie, genres):
#     genres_names = []
#     genre_ids = movie["genre_ids"]
#     for genre_id in genre_ids:
#         for genre in genres:
#             if genre_id == genre["id"]:
#                 genre_name = genre["name"]
#                 genres_names.append(genre_name)

#     new_movie_info = {
#         "genre_names": genres_names,
#         "id": movie["id"],
#         "overview": movie["overview"],
#         "title": movie["title"],
#         "vote_average": movie["vote_average"],
#     }



# if __name__ == "__main__":
#     movie = {
#         "adult": False,
#         "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
#         "genre_ids": [18, 80],
#         "id": 278,
#         "original_language": "en",
#         "original_title": "The Shawshank Redemption",
#         "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
#         "popularity": 67.931,
#         "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
#         "release_date": "1995-01-28",
#         "title": "쇼생크 탈출",
#         "video": False,
#         "vote_average": 8.7,
#         "vote_count": 18040,
#     }

#     genres_list = [
#         {"id": 28, "name": "Action"},
#         {"id": 12, "name": "Adventure"},
#         {"id": 16, "name": "Animation"},
#         {"id": 35, "name": "Comedy"},
#         {"id": 80, "name": "Crime"},
#         {"id": 99, "name": "Documentary"},
#         {"id": 18, "name": "Drama"},
#         {"id": 10751, "name": "Family"},
#         {"id": 14, "name": "Fantasy"},
#         {"id": 36, "name": "History"},
#         {"id": 27, "name": "Horror"},
#         {"id": 10402, "name": "Music"},
#         {"id": 9648, "name": "Mystery"},
#         {"id": 10749, "name": "Romance"},
#         {"id": 878, "name": "Science Fiction"},
#         {"id": 10770, "name": "TV Movie"},
#         {"id": 53, "name": "Thriller"},
#         {"id": 10752, "name": "War"},
#         {"id": 37, "name": "Western"},
#     ]

#     pprint(movie_info(movie, genres_list))

# 문제 19번 실습 풀이




