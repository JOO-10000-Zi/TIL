-- classmates
-- name : TEXT
-- age : INT
-- address : TEXT

CREATE TABLE classmates (
    name TEXT,
    age INT,
    adderss TEXT
);

-- 테이블 조회
.tables

INSERT INTO classmates (name, age) VALUES('홍길동', 33);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, adderss) VALUES('임꺽정', 44, '한양');

SELECT rowid, * FROM classmates;

INSERT INTO classmates VALUES ('이몽룡', 25, '경주');

DROP TABLE classmates;
