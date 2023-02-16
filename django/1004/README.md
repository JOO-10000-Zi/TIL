# Django ModelForm

### 개요

- DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 모델(DB)과 매우 밀접한 관계를 가짐
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  - 즉, 모델에 저으이한 필드의 구성 및 종유레 따라 HTML Form이 결정됨
- 사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며
  이는 서버 사이드에서 반드시 처리애햐 함.

## ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 helper class
- ModelForm은 Form과 똑같은 방식으로 View 함수에 사용

### ModelForm 선언

- forms 라이브러리의 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

![image-20230214133627404](assets/image-20230214133627404.png)

### ModelForm에서의 Meta Class

- ModelForm의 정보를 작성 하는곳
- ModelForm을 사용할 경우 참조 할 모델이 있어야 하는데, Meta class의
  model 속성이 이를 구성함
  - 참조하는 모델에 정의된 field 정보를 Form에 적용함



![image-20230214133743148](assets/image-20230214133743148.png)

- fields 속성에 '\__all__'를 사용하여 모델의 모든 필드를 포함할 수 있음
- 또는 exclude 속성을 사용하여 모델에서 포함하지 않는 필드를 지정할 수 있음

![image-20230214133850705](assets/image-20230214133850705.png)



### ModelForm 활용

1. ModelForm 객체를 context로 전달
   ![image-20230216112629363](assets/image-20230216112629363.png)
2. Input Field 활용
   ![image-20230216112717425](assets/image-20230216112717425.png)

#### From erndering options

- \<label> & \<input> 쌍에 대한 3가지 출력 옵션

  - as_p()
    - 각 필드가 단락(\<p> 태그)으로 감싸져서 렌더링

  - as_ul()
    - 각 필드가 목록 항목(\<li> 태그)으로 감싸져서 렌더링
    - \<ul> 태그는 직접 작성해야 한다.
  - as_table()
    - 각 필드가 테이블(\<tr> 태그) 행으로 감싸져서 렌더링

### 저장 및 활용

![image-20230216113319699](assets/image-20230216113319699.png)



## ModelForm with view functions

#### ModelForm 활용 로직

- 요청 방식에 따른 분기
  - HTML Form전달
  - 사용자 입력 데이터 수신
- 유효성 검사에 따른 분기
  - 유효성 검사 실패시 Form 으로 전달
  - 유요성 검사 성공시 DB 저장

![image-20230216113537821](assets/image-20230216113537821.png)



#### CREATE

- 유효성 검사를 통과하면
  - 데이터 저장 후
  - 상세 페이지로 리다이렉트

- 통과하지 못하면
  - 작성 페이지로 리다이렉트

![image-20230216114230619](assets/image-20230216114230619.png)

#### "is_valid()" method

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
- 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()제공하여
  개발자의 편의를 도움

#### The "save()" method

- form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
- ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지 , 수정할지를 결정
  - 제공되지 않는 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)
  - 제공되면 save()는 해당 인스턴스를 수정(UPDATE)

![image-20230216114745344](assets/image-20230216114745344.png)



#### form 인스턴스의 errors 속성

- is_valid()의 반환 값이 False인 경우 form 인스턴스의 errors 속성에 값이 작성되는데,
  유효성 검증을 실패한 원인이 되는 딕셔너리 형태로 저장됨![image-20230216115336421](assets/image-20230216115336421.png)



- title에 공백을 넣고 제출해 보기![image-20230216115157170](assets/image-20230216115157170.png)



- 이 같은 특징을 통해 다음과 같은 구조로 코드를 작성하면 유효성 검증을 실패 했을 때
  사용자에게 실패 결과 메세지를 출력해줄 수 있음![image-20230216115126862](assets/image-20230216115126862.png)

#### UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정
- request.POST
  - 사용자가 form을 통해 전송한 데이터(새로운 데이터)
- instance
  - 수정이 되는 대상



- edit - view 수정
  ![image-20230216115827225](assets/image-20230216115827225.png)



- edit - template 수정
  ![image-20230216115856767](assets/image-20230216115856767.png)



- update - view 수정
  ![image-20230216121235908](assets/image-20230216121235908.png)



## Handling HTTP requests

### Create 

- new와 create view 함수를 합침
- 각각의 역할은 request.mehtod 값을 기준으로 나뉨

![image-20230216121401487](assets/image-20230216121401487.png)



- 이제는 불필요해진 new의 view 함수와 url path를 삭제

![image-20230216121549955](assets/image-20230216121549955.png)



- new.html -> create.html 이름변경 및 action 속성 값 수정

![image-20230216121632663](assets/image-20230216121632663.png)



- new.html -> create.html 이름변경으로 인한 템플릿 수정

![image-20230216121709344](assets/image-20230216121709344.png)



- index 페이지에 있던 new 관련 링크 수정

![image-20230216121741011](assets/image-20230216121741011.png)



#### 주의!! context의 들여쓰기 위치

- 이렇게 작성하면 if form.is_valid(): 에서 flase로 펼가 받았을 때 이어질 코드가 없음
  ![image-20230216121847294](assets/image-20230216121847294.png)



- 반면 다음과 같이 작성하면 if form.is_valid(): 에서 false로 평가 받았을 때 에러 정보가 담긴
  form 인스턴스가 context로 넘어 갈 수 있음
  ![image-20230216124058537](assets/image-20230216124058537.png)



### Update

- edit과 update view 함수를 합침

![image-20230216124728781](assets/image-20230216124728781.png)

- new와 마찬가지로 불필요해진 edit의 view 함수와 url path를 삭제

![image-20230216124805400](assets/image-20230216124805400.png)



- edit.html -> update.html 이름변경으로 인한 관련 정보 수정

![image-20230216124840516](assets/image-20230216124840516.png)
