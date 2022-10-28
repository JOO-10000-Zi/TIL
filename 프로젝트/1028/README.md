# django pair project

## 팀원(이성인,안동우,주세환)

- 이성인 : 유저(로그인, 회원가입, 회원상세페이지, 로그아웃), 네브바, 팔로우 구현
- 안동우 : 리뷰(생성, 디테일), 좋아요 구현
- 주세환 : 리뷰(인덱스(목록), 업데이트, 삭제), 댓글(생성, 삭제, 목록) 구현
- 공동 작업
  - 좋아요 비동기 구현
  - 댓글 비동기 구현
  - 세부 디자인 수정
  - heroku 배포

## 명서세 작업 내역

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야 합니다.

- **CRUD** 구현(구현 방법 제한 없음)
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원 가입 / 회원 조회 / 로그인 / 로그아웃)
- Media 활용 동적 파일 다루기
- 모델간 **1 : N / M : N 관계** 매핑

## 요구 사항

### 모델 Model

- 모델 이름 : User
  Django **AbstractUser** 모델을 상속 받고, 필드를 직접 정의하세요.
- 모델 이름 : Review
  모델의 필드를 직접 정의하세요.

* 모델 이름 : Comment
  모델의 필드를 직접 정의하세요.

### **폼 Form**

회원 가입

- Django 내장 회원 가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 생성
- 출력할 필드를 직접 정의합니다.

로그인

- Django 내장 로그인 폼 AuthenticationForm 활용

### 기능 View

**리뷰 reviews**

데이터 목록 조회

- `GET` http://127.0.0.1:8000/reviews/

```python
# urls.py 작성 내용
path("", views.index, name="index")

# views.py 작성 내용
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)
```

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/
- 로그인한 유저만 데이터 생성이 가능합니다.

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/update/
- 해당 리뷰 작성자만 수정할 수 있습니다.

```python
# urls.py 작성 내용
path("<int:pk>/update/", views.update, name="update"),

# views.py 작성 내용
@login_required
def update(request, pk):
    reviews = Review.objects.get(pk=pk)
    if request.user == reviews.user:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, "글 수정을 완료 했습니다.")
                return redirect("reviews:detail", reviews.pk)
        else:
            form = ReviewForm(instance=reviews)
        context = {"form": form}
        return render(request, "reviews/update.html", context)
```

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/delete/
- 해당 리뷰 작성자만 삭제할 수 있습니다.

```python
# urls.py 작성 내용
path("<int:pk>/delete", views.delete, name="delete"),

# views.py 작성 내용
def delete(request, pk):
    reviews = Review.objects.get(pk=pk)
    if request.user == reviews.user:
        reviews.delete()
    return redirect("reviews:index")
```

리뷰 좋아요 / 좋아요 취소

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/like/
- 로그인한 유저만 좋아요 기능을 사용할 수 있습니다.

**댓글 comments**

리뷰의 댓글 목록 조회

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/
- 해당 게시글의 댓글 목록 조회

```html
<!-- 비동기 댓글 기능 구현 -->
<script>
  const commentAdd = document.querySelector("#comment-add");
  commentAdd.addEventListener("submit", function(event) {
    event.preventDefault();
    const reviewId = event.target.dataset.reviewId;
    axios({
      method: "post",
      url: `/reviews/${reviewId}/comments/`,
      headers: { "X-CSRFToken": csrftoken },
      data: new FormData(commentAdd)
    }).then(response => {
      const comments = document.querySelector("#comment-create");
      comments.insertAdjacentHTML(
        "beforeEnd",
        `
          <p>${response.data.userName} | ${response.data.comment}</p>
          <form class='text-end' action="/reviews/${reviewId}/comments/${response.data.commentPk}/comment_delete/" method="POST" data-comment-id=${response.data.commentPk}>
            {% csrf_token %}
            <input type="submit" class='btn btn-dark' value='삭제'>
          </form>
          <hr>`
      );
      commentAdd.reset();
    });
  });
</script>
```

댓글 생성

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/comments/create/
- 로그인한 유저만 댓글 생성이 가능합니다.

```python
# urls.py 작성 내용
path("<int:pk>/comments/", views.comment_create, name="comment_create"),

# views.py 작성 내용
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        context = {
            'comment': comment.content,
            'userName': comment.user.username,
            'commentPk': comment.pk,
        }
        return JsonResponse(context)
```

댓글 삭제

- `POST` http://127.0.0.1:8000/reviews/<int:review_pk>/comments/<int:comment_pk>/delete/
- 해당 댓글 작성자만 삭제할 수 있습니다.

```python
# urls.py 작성 내용
path("<int:review_pk>/comments/<int:comment_pk>/comment_delete/",views.comment_delete,name="comment_delete"),
# views.py 작성 내용
def comment_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("reviews:detail", review_pk)
```

**회원 관리 accounts**

회원 가입

- `POST` http://127.0.0.1:8000/accounts/signup/

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

팔로우

- `POST` http://127.0.0.1:8000/accounts/<int:user_pk>/follow/
- 로그인한 유저만 팔로우 기능을 사용할 수 있습니다.
- 자기 자신은 팔로우 할 수 없습니다.

### 화면 Template

**네비게이션바, Bootstrap <nav>**

- 서비스 로고
- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 로그인 상태에 따라 다른 화면을 출력합니다.
  1. 로그인 상태
     - 로그인한 사용자의 username
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원 가입 페이지 이동 버튼

**메인 페이지**

- `GET` http://127.0.0.1:8000/
- 자유 디자인

**목록 페이지**

- `GET` http://127.0.0.1:8000/reviews/

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/
- 해당 리뷰 정보 출력
- 댓글 작성 폼
- 해당 리뷰에 작성된 댓글 목록
  - 각 댓글에는 삭제 버튼이 있습니다. 단, 댓글 작성자만 삭제를 할 수 있습니다.
- 좋아요 버튼
  - 해당 리뷰의 좋아요 개수를 함께 출력합니다.
  - 로그인한 유저는 리뷰에 좋아요를 남길 수 있습니다.

```html
{% extends 'base.html' %} {% load django_bootstrap5 %} {% block title %}게시판
페이지{% endblock title %}
<!-- body -->
{% block content %}
<h1 class="text-center my-4">게시판</h1>
<table class="table text-center">
  <thead>
    <th>게시번호</th>
    <th>제목</th>
    <th>작성자</th>
  </thead>

  <tbody>
    {% for review in reviews %}
    <tr>
      <td>{{ review.pk }}</td>
      <td>
        <a href="{% url 'reviews:detail' review.pk %}">{{ review.title }}</a>
      </td>
      <td>{{ review.user }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% if request.user.is_authenticated %}
<a class="btn btn-dark" href="{% url 'reviews:create' %}">글쓰기</a>
{% endif %} {% endblock content %}
```

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:review_pk>/update/
- 리뷰 수정 폼

```html
{% extends 'base.html' %}
{% load django_bootstrap5 %} 
{% block title %}게시글 수정하기{% endblock title %} 
<!-- body -->>
{% block content %}
<h1 class="text-center my-4">게시글 수정하기</h1>
<form action="" method="POST">
  {% csrf_token %} {% bootstrap_form form %}
  <input type="submit" class="btn btn-dark" value="수정하기" />
</form>
{% endblock content %}
```

회원 가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원 가입 폼

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 회원이 작성한 게시글 목록 출력

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원 가입 페이지 이동 버튼

팔로우 버튼

- 로그인한 유저는 해당 유저를 팔로우 할 수 있습니다.
- 단, 자기 자신은 팔로우 할 수 없습니다.
