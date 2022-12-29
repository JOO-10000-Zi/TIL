
import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.  
    db_URL = 'https://api.themoviedb.org/3'                             # 기본 URL을 받아 와서 변수로 정의한다
    path = '/movie/popular'                                             # 사이트 내에서 경로가 되는 세부 URL을 별도 나눠서 변수로 정의한다
    params = {                                                          # api 키 를 딕셔너리 키, 벨류 값으로 넣어야 활용 할 수 있다
        'api_key' : '',                                     
        'language' : 'ko-KR'                                            # 언어를 한글로 바꿔주는 옵션 키 이다.
    }
    response = requests.get(db_URL+path, params = params).json()        # response 변수에 requests(URL에서 가져온 데이터)를 json형식으로 정의 한다
    # pprint(response)
    # 평점이 높은 5위를 출력하라
    inki = []                                                           # fot문으로 출력한 값을 변수 inki에 리스트를 만들어 업데이트 한다
    for i in response.get('results'):                                   
          inki.append(i)
          osun = sorted(inki, key= lambda i : i.get('vote_average'))    # lambda 를 활용하여 정렬 하여 변수 osun에 넣는다
          osunup = osun[::-1]                                           # 슬라이싱 하여 순서를 역순으로 바꾼다 
    return osunup[0:5]                                                  # 슬라이싱으로 0 ~ 4 인덱스까지 리턴한다
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
