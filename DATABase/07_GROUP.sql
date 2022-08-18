CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv
.import users.csv users

-- 성별 갯수
SELECT last_name 성, COUNT(*)
FROM users
GROUP BY last_name;


SELECT last_name 성, avg(age) 평균, COUNT(*) 수
FROM users
GROUP BY last_name;
-- avg = 첫번째 데이터 값 적용이 안된다 사용시 주의

SELECT last_name, age
FROM users
WHERE last_name="주"; 

SELECT *
FROM users
LIMIT 5;

SELECT last_name 성, COUNT(*) 수
FROM users
GROUP BY last_name
LIMIT 5;

-- GROUP BY 조건을 쓰고 싶다면 HAVING
SELECT last_name 성, COUNT(*) 명
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
-- 성  명
-- -  ---
-- 김  268
-- 이  179