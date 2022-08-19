-- 단순 조회
SELECT id, gender
FROM healthcare
LIMIT 5;
-- id  gender
-- -- ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2

-- 성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END 성별
FROM healthcare
LIMIT 5;
-- id  성별
-- --  --
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자

-- 흡연 여부
SELECT DISTINCT smoking
FROM healthcare;

SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비흡연자'
        ELSE '무응답'
    END 흡연여부
FROM healthcare
LIMIT 10;
-- id  smoking  흡연여부
-- --  -------  -----
-- 1   1        비흡연자
-- 2   1        비흡연자
-- 3   1        비흡연자
-- 4   1        비흡연자
-- 5   1        비흡연자
-- 6   3        헤비흡연자
-- 7   3        헤비흡연자
-- 8   3        헤비흡연자
-- 9   1        비흡연자
-- 10  1        비흡연자


-- 유저 테이블 가져오기
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
-- 나이에 따른 구분
SELECT 
    last_name 성,
    first_name 이름,
    age 나이,
    CASE
        WHEN age <= 20 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 then '중장년'
        ELSE '노년'
    END 구분
FROM users
LIMIT 10;
-- 성  이름  나이  구분
--  --  --  ---
-- 유  정호  40  청년
-- 이  경희  36  청년
-- 구  정자  37  청년
-- 장  미경  40  청년
-- 차  영환  30  청년
-- 이  서준  26  청년
-- 민  주원  18  청소년
-- 김  예진  33  청년
-- 김  서현  23  청년
-- 오  서윤  22  청년
