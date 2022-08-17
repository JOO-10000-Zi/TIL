CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    blance INTEGER NOT NULL
);

.mode csv
.import users.csv users

-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름 3명
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;
-- first_name
-- ----------
-- 정호
-- 경희
-- 정자

-- 30세 이상이고 성이 김인 사람
SELECT age, first_name FROM users WHERE age >=30 and last_name='김';

-- 30세 이상인 사람들의 숫자
SELECT COUNT(*) FROM users WHERE age >= 30;
-- COUNT(*)
-- --------
-- 1656

--전체 중에 가장 작은 나이
SELECT min(age) FROM users;
-- min(age)
-- --------
-- 15

-- 이씨 중에 가장 작은 나이
SELECT min(age) FROM users WHERE last_name='이';
-- min(age)
-- --------
--15

-- 이씨 중 가장장은 나이를 가직 사람의 이름과 계좌
SELECT min(age), first_name, balance FROM users WHERE last_name='이';
-- min(age)  first_name  balance
-- --------  ----------  -------
-- 15        은영          78000

-- 컬럼명 수정
ALTER TABLE users RENAME COLUMN blance TO balance;

-- 30세 이상인 사람들의 평균 나이
SELECT avg(age) FROM users WHERE age >= 30;
-- avg(age)
-- ----------------
-- 35.1763285024155

-- 계좌 잔액이 가장 높은 사람
SELECT MAX(balance), first_name FROM users;
-- MAX(balance)  first_name
-- ------------  ----------
-- 1000000       순옥

-- 지역 번호가 02인 사람
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
-- COUNT(*)
-- --------
-- 996

-- 준으로 끝나는 사람
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
-- COUNT(*)
-- --------
-- 124

-- 중간 전화번호가 5114 인 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';
-- COUNT(*)
-- --------
-- 4

-- 나이 오름차순 10명
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
-- first_name
-- ----------
-- 서영
-- 지후
-- 우진
-- 우진
-- 은영
-- 지훈
-- 승현
-- 주원
-- 은정
-- 정수

-- 나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 정수          강          15   충청북도     02-7245-5623   500
-- 정수          강          15   충청북도     02-7245-5623   500
-- 정수          강          15   충청북도     02-7245-5623   500
-- 정수          강          15   충청북도     02-7245-5623   500
-- 우진          고          15   경상북도     011-3124-1126  300
-- 시우          고          15   제주특별자치도  016-3732-8726  270
-- 우진          고          15   경상북도     011-3124-1126  300
-- 시우          고          15   제주특별자치도  016-3732-8726  270
-- 우진          고          15   경상북도     011-3124-1126  300
-- 시우          고          15   제주특별자치도  016-3732-8726  270

-- 계좌 잔액순 내림 차순, 성-이름-잔액 조회
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- last_name  first_name  balance
-- ---------  ----------  -------
-- 김          순옥          1000000
-- 우          상철          1000000
-- 민          진호          1000000
-- 이          재호          1000000
-- 강          민준          1000000
-- 황          은정          1000000
-- 김          영수          1000000
-- 허          정남          1000000
-- 김          순옥          1000000
-- 우          상철          1000000

-- 계좌 잔액 내림차순, 성 오름차순
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
-- last_name  first_name  balance
-- ---------  ----------  -------
-- 강          민준          1000000
-- 강          민준          1000000
-- 강          민준          1000000
-- 강          민준          1000000
-- 김          순옥          1000000
-- 김          영수          1000000
-- 김          순옥          1000000
-- 김          영수          1000000
-- 김          순옥          1000000
-- 김          영수          1000000
