# class preson:
#     pass

# # 인스턴스 생성
# p1 = preson()
# # 인스턴스 속성
# p1.name = '홍길동'


# print(p1.name)

# class person :
#     human = '사람'
#     # 인스턴스 메서드
#     # 인스턴스가 활용할 메서드
#     def greeting(self):
#         print('안녕하세요~')

# iu = person()
# iu.greeting()

# print(person.human)

class person:

    def __init__(self, name):
        self.name = name
    
    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')

jimin = person('지민')
jimin.greeting()

iu = person('지은')
iu.greeting()
