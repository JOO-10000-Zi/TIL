## Git / GitHub

## 1. 개요

- 분산 버전 관리 시스템
- GUI 와 다른 `CLI(Command Line Interface)'를 의미

## 2. 특징

1. 명령어
   
   - pwd(print working directory) : 현재 디렉토리 출력(폴러 / 파일)
   - cd(vhange directory) : 디렉토리 이동
     - . : 현재 디렉토리, . : 상위 디렉토리
   - ls(list) : 목록
   - mkdir(make directory) : 디렉토리(폴더) 생성
   - touch : 새 파일 생성
   - git config --global user.name '사용자 ID'
   - git config --globlr user.email '사용자 email'
   - clear : 화면 지우기(명령어 작성 기록) / ctrl + L
   - git init : 버전, 저장관리
   - git add "name" : 워킹 디렉토리 > 스테잉에어리어 추가
     - 빨간 네임 > 그린 네임으로 확인
   - git commit -m "메세지 내용" : 커밋을 통해 버전으로 기록
     - 내가 무슨 작업을 했는지 기록을 하기위해 메세지 내용 입력 필수!
   - git status : 현재 버전의 정보 조회
   - git log : 기록된 버전의 정보 조회
     - git log -1 : 최근 1개 커밋을 조회
     - git log  --oneline : 한줄로 보여줘
     - git log -2 --oneline : 최근 2개를 한줄로 보여줘
   - rm (파일명) : 파일 지우기
   - rm -r (폴더명) : 폴더 지우기
   - rm -rf : init(마스터) 지우기 (잘못된 위치에서 git init 한 경우)

2. 버전관리시스템 개념

> 여러버전을 관리하는 시스템

- 1통(working directory) : 작업 중인 환경
- 2통(Staging Area) : 중간저장 단계(커밋 전 여러 버전을 가지고 있는 단계)
- 3통(Repository) : 커밋 단계(버전 기록)
3. GitHub에 Push하기
   
   - ```
     git push origin master : 오리진을 마스터로 지정
     ```
   
   - ```
     git remote add origin https://github.com/JOO-10000-Zi(username)/ex1.git(저장소 이름)
     ```

## 분산버전관리시스템(DVCS)

중간 저장 - 내가 버전기록 파일 들을 모아서 따로 저장하기 위해 존재한다

Git 파일을 modified(수정), staged(add명령어 사용),committed(커밋완료)로 관리

## 파일 라이프사이클

1. Untracked : 한번도 커밋 X
2. Unmodified : 커밋 되었음/ 수정 X
3. Modified : 2번 수정 된 단계
4. staged : 임시공간(2통) 커밋 후 2번 으로

## 원격저장소 기본 흐름

> push > 원격 저장소에 저장
> 
> pull > 원격 저장소에서 로컬로 가져온다

## 1. (master) 있는 곳에서는 git init을 하지 않는다

## 2. git 명령어를 입력할때에는 항상 경로를 잘보자

## 3. 명령어를 잘 확인 하자

## 참고 자료

> 버전관리 왜 프로그램,파일 예외 적용 가능 소스 활용

1. 이그노어.io
