import requests

from pprint import pprint
def popular_count():
    
    # 여기에 코드를 작성합니다.  
    db_URL = 'https://api.themoviedb.org/3'                             # 기본 URL을 받아 와서 변수로 정의한다
    path = '/movie/popular'                                             # 사이트 내에서 경로가 되는 세부 URL을 별도 나눠서 변수로 정의한다
    params = {                                                          # api 키 를 딕셔너리 키, 벨류 값으로 넣어야 활용 할 수 있다
        'api_key' : '',                                     
        'language' : 'ko-KR'                                            # 언어를 한글로 바꿔주는 옵션 키 이다.
    }
    response = requests.get(db_URL+path, params = params).json()        # response 변수에 requests(URL에서 가져온 데이터)를 json형식으로 정의 한다
    # pprint(response)
    cnt = 0 
    for i in response.get('results'):                                   # 영화의 개수를 구하기 위해 for문 을 활용 하여 json형식으로 가져온 딕셔너리에서 results의
        cnt += 1                                                        # 목록을 하나씩 확인 하면서 cnt에 + 1식하여 개수를 구한다

    return cnt
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
