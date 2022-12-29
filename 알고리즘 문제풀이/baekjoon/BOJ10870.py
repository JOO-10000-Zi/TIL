N = int(input())

pibo = [0,1]
# 처음 피보라는 리스트에 0,1 처음 정해진 값을 지정

for i in range(N-1):
    # 반복문을 통해 N-1 만큼의 횟수 만큼 인덱스 값을 이용 하여
    # 값을 더해 준다
   hab = pibo[i] + pibo[i+1]
   pibo.append(hab)
# 더해준 수의 인덱스 값을 활용하여 마지막만 출력 한다.
if N == 0 :
    print(pibo[0])
else:
    print(pibo[-1])