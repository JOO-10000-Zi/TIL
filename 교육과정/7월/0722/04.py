import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    db_URL = 'https://api.themoviedb.org/3'                             # 기본 URL을 받아 와서 변수로 정의한다
    path = '/search/movie'                                             # 사이트 내에서 경로가 되는 세부 URL을 별도 나눠서 변수로 정의한다
    params = {                                                          # api 키 를 딕셔너리 키, 벨류 값으로 넣어야 활용 할 수 있다
        'api_key' : '0e6592cf2bc6bdab02c8dbf629efc03a',                                     
        'language' : 'ko-KR',                                           # 언어를 한글로 바꿔주는 옵션 키 이다.
        'qurey' : title                                          
    }
    response = requests.get(db_URL+path, params = params).json() 

    coo = []
    for i in response.get('results'):
        coo.append(i)
    return coo

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
