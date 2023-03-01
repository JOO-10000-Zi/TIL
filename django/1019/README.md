# 1:N(User - Comment)

### 개요

- User(1) - Comment(N)
- User 모델과 Comment 모델 간 관계 설정
- "0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음"



## 모델 관계 설정

![image-20230301211544453](assets/image-20230301211544453.png)



- Comment 모델에 User 모델을 참조하는 외래키 작성
  ![image-20230301211608945](assets/image-20230301211608945.png)
