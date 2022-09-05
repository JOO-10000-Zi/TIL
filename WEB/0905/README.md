# HTML(form)

- HTML에서 문서 구조화(표)를 만들기 위해서는 \<thead> \<tbody> \<tfoot> 
  요소를 활용 한다 

![image-20220905133302592](assets/image-20220905133302592.png)

- \<tr>으로 가로줄을 구성하고 내부에는 \<th>혹은 \<td>로 셀을 구성

![image-20220905133933194](assets/image-20220905133933194.png)

- colspan, rowspan 속성을 활용하여 셀 병합

![image-20220905134007114](assets/image-20220905134007114.png)

- \<caption>을 통해 표 설명 또는 제목을 표현

![image-20220905134042376](assets/image-20220905134042376.png)

- table 태그 기본 구성

  - thead
    - tr > th

  - tbody
    - tr > td
  - tfoot
    - tr > td
  - caption



## form

- \<form>은 정보를 서버에 제출하기 위해 사용하는 태그
- \<form> 기본속성
  - action : form을 처리할 서버의 URL(데이터를 보낼곳)
  - method : form을 제출할 때 사용 할 HTTP 메서드 (GET혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송시(input type 이 file인 경우)

## input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- \<input> 대표적인 속성
  - name : form contro에 적용되는 이름 (이름/값 페어로 전송됨)
  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등

## input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사요잦는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용 할 수 있음
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을
    확인 할 수 있도록 함
  - \<input>에 id 속성을, \<label>에는 for 속설을 활용하여 상호 연관 시킴

![image-20220905142406577](assets/image-20220905142406577.png)

## input 유형 - 일반

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경구 form 제출 불가
  - number : min, max, step속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

## input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대하여는 name을 지정하고 선택괸 항목에 대한 value를 지정해야 함
  - checkbox : 다중 선택
  - radio : 단일 선택

## input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에세 보이지 않는 input

# Bootstrap

>Build fast, responsive sites with Bootstrap.
>**Quickly** design and customize **responsive** mobile-first sites with 
>Bootstrap, **the world’s most popular** front-end open source toolkit, 
>featuring Sass variables and mixins, **responsive grid system**, extensive 
>**prebuilt components**, and powerful JavaScript plugins.



## 기본 설정 과 다른 점

![image-20220905145554253](assets/image-20220905145554253.png)

- 마진의 상쇄 되는 현상을 Bootstrap에서는 CSS를 통해서 마진을 없에는 등의 다양한 설정 값을
  개발자와 사용자의 편리성을 위해 오픈 소스로 제공을 하고 있다.
