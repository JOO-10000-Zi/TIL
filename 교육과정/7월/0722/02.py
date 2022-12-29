import requests
from pprint import pprint


def vote_average_movies():
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
    SP = 0
    ingi = []
    for i in response.get('results'):
        SP = i.get('vote_average')
        if SP >= 8 :
          ingi.append(i)
    return ingi




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
