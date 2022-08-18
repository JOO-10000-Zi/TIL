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

SELECT * FROM users LIMIT 1;

SELECT
    last_name || first_name 성명,
    age 연령,
    country 도시,
    phone 휴대전화,
    balance
FROM users
LIMIT 5;

-- 성명   연령  도시    휴대전화           balance
-- ---  --  ----  -------------  -------
-- 유정호  40  전라북도  016-7280-2855  370
-- 이경희  36  경상남도  011-9854-5133  5900
-- 구정자  37  전라남도  011-4177-8170  3100
-- 장미경  40  충청남도  011-9079-4419  250000
-- 차영환  30  충청북도  011-2921-4284  220

-- 문자열 길이 LENGTH
SELECT
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환

-- 문자열 REPLACE
SELECT
    first_name 이름,
    phone 전화,
    REPLACE(phone, "-","")
FROM users
LIMIT 5;
-- 이름  전화             REPLACE(phone, "-","")
--  -------------  ----------------------
-- 정호  016-7280-2855  01672802855
-- 경희  011-9854-5133  01198545133
-- 정자  011-4177-8170  01141778170
-- 미경  011-9079-4419  01190794419
-- 영환  011-2921-4284  01129214284

-- 숫자 활용
SELECT MOD(5, 2)
FROM users
LIMIT 1;
-- MOD(5, 2)
-- ---------
-- 1.0

-- 올림 ,내일, 반올림 
SELECT CEIL(3.14) 올림, FLOOR(3.14) 내림, ROUND(3.14) 반올림
FROM users
LIMIT 1;
-- 올림   내림   반올림
-- ---  ---  ---
-- 4.0  3.0  3.0

-- 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;
-- SQRT(9)
-- -------
-- 3.0

-- 제곱
SELECT POWER(9, 3)
FROM users
LIMIT 1;
-- POWER(9, 3)
-- -----------
-- 729.0