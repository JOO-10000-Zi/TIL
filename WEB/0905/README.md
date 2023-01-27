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

![image-20230127134918274](assets/image-20230127134918274.png)

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

## spacing (Margin and padding)

![image-20220905150427533](assets/image-20220905150427533.png)

```html
<div class="mt-3 ma-5">bootstrap-spacing</div>
```

- 약어를 통해 마진과 패딩을 조절 할 수 있다
  - property(속성)
    - m - for classes that set margin
    - p - for classes that set padding
  - sides
    - t - margin-top or padding-top 속성 설정 
    - b - margin-bottom or padding-bottom 설정
    - s(start) - **LTR**(margin-left or padding-left), **RLT**(margin-right or padding-right)
          왼쪽부터, 오른쪽부터 시작하여 여백을 주는 설정
    - e(end)-  s 와 반대되는 개념
    - x - 좌우 둘다 설정 하는 경우
    - y - 상하 둘다 설정 하는 경우

## 기본 단위

![image-20220905151654929](assets/image-20220905151654929.png)

- m, p 간격 단위는 동일
- .mx-auto : 블럭 요소 수평 중앙 정렬 가로 가운데 정렬
- .py-0 : 위 아래 패딩 값이 0



- 종합 표

![image-20220905151855382](assets/image-20220905151855382.png)

## color

![image-20220905151937362](assets/image-20220905151937362.png)



## Bootstrap 사용하기

1. CSS 파일을 다운받아서 사용

2. 설정 URL을 복사하여 HTML문서에 붙여넣어서 바로 사용

   - 3개의 코드를 가져와 바로 사용 가능

     - ```html
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
       ```

       - 헤더 부분에 입렵

     - ```html
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
       ```

       - body 부분에 입력 후 사용

# Bootsrtap 파헤치기

## Layout

### Breakpoints

- Breakpoints 는 모니터 또는 뷰포트 크기에 반응하는 반응형 레이아웃의 작동 방식을 결정 하는 방식

![image-20220905161131369](assets/image-20220905161131369.png)

- xl = PC 모니터 & 노트북
- lg or md = 테블릿 & 구형 모니터
- sm, None = 모바일 

> 모니터의 너비가 변화에 따라서 만들어 놓은 페이지가 자동으로 변화 할 수 있도록 사전에 정의 해 놓은
> 클래스이며, 이를 활용하여 페이지 마다 각각의 화면 너비에 맞도록 디자인 할 수 있다

## Content

### Reboot

> CSS변경의 모음 으로 퀵스타트 할 수 있도록 일관된 기준선을 제공하는 콘텐츠

- Reboot는 Normalize를 기반으로 하여 독닥적인 스타일로 많은 HTML 요소를 제공합니다
- \<table>에 더 간단한 기준선을 위해 일부 스타일을 정하여 지원 하고 .table, .table-bordered등을 제공한다



**제목 및 단락**

- 기본 적인 마진율에서 Bootstrap에서 지정한 제목의 마진과 스타일로 새로 정의 됩니다

![image-20220905164604890](assets/image-20220905164604890.png)

**수평 규칙**

- 수평 선에 대해서 다양항 타입을 지정 할수 있으며, 문서와 비슷한 색상과 굵기, 별도의 컬러와 투명도를
  활용하여 지정 할수 있습니다

![image-20220905164837380](assets/image-20220905164837380.png)

**인라인 코드**

- \<code>를 사용하여 HTML 내용에 꺽쇠 괄호를 이스케이프 처리 할 수 있습니다.
  - &lt = \< , &gt = \>

![image-20220905165158065](assets/image-20220905165158065.png)



**사용자 입력**

![image-20220905165354848](assets/image-20220905165354848.png)





**form**

- 기본적으로 지원하는 폼 양식
  - fieldset : 테두리, 패딩 또는 여백이 없다
  - legend : 제목이 표시되록 만든 스타일
  - label : display: inline-block할 수 있도록 설정, margin을 설정 할 수 있다
  - textarea : 가로의 크기를 수정하면 페이지 레이아웃이 변경 될 수 있어 세로 크기만 조정 된다
  - button 및 input : not(disabled) 기능이 있다



**이미지**

- .img-fluid : 부모 너비에 맞게 크기가 조정되도록 이미지에 max-width: 100%, height: auto로 적용

정렬

​					  ![image-20220905170704849](assets/image-20220905170704849.png)	

![image-20220905170732983](assets/image-20220905170732983.png)

**테이블**

![image-20220905171011032](assets/image-20220905171011032.png)

- 줄무늬 행 & 줄무늬 열

![image-20220905171115762](assets/image-20220905171115762.png)

![image-20220905171128025](assets/image-20220905171128025.png)

- 어두운 모드 사용 가능

![image-20220905171202168](assets/image-20220905171202168.png)

- hover 적용

![image-20220905171252183](assets/image-20220905171252183.png)

## Form

![image-20220905171811047](assets/image-20220905171811047.png)

**form control**

- sizing
  - form-control-lg 처럼 클래스를 사용하여  탭의 높이를 설정 할 수 있다

![image-20220905172450315](assets/image-20220905172450315.png)

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

**select**

- 리스트 상자를 만들어서 목록을 선택 하도록 만들 수 있다

![image-20220905172641193](assets/image-20220905172641193.png)

![image-20220905172734094](assets/image-20220905172734094.png)

**check box & radio**

- 체크박스와 라디오 버트븐을 지원 하는 기능이 있다
  - checkbox : 중복 선택 가능
  - radio : 단일 선택 가능
- checkbox

![image-20220905173147145](assets/image-20220905173147145.png)

- radio

![image-20220905173337879](assets/image-20220905173337879.png)

```html
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
  <label class="form-check-label" for="flexRadioDefault1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
  <label class="form-check-label" for="flexRadioDefault2">
    Default checked radio
  </label>
</div>
```

- 스위치

![image-20220905173427039](assets/image-20220905173427039.png)

```html
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
  <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
  <label class="form-check-label" for="flexSwitchCheckChecked">Checked switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDisabled" disabled>
  <label class="form-check-label" for="flexSwitchCheckDisabled">Disabled switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Disabled checked switch checkbox input</label>
</div>
```



