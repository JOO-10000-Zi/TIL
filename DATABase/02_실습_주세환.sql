-- 1. 모든 데이터 수
SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
-- --------
-- 1000000

-- 2. 연령의 최대, 최소값 모두 술력
SELECT MAX(age), MIN(age) FROM healthcare; 
-- MAX(age)  MIN(age)
-- --------  --------
-- 18        9

-- 3. 신장과 체중의 최대 최소값 모두
SELECT MAX(height), MIN(weight) FROM healthcare;
-- MAX(height)  MIN(weight)
-- -----------  -----------
-- 195          30

-- 4. 신장이 160이상 170이하인 사람은 몇명
SELECT COUNT(*) FROM healthcare WHERE 160 <= height AND height <= 170;
-- COUNT(*)
-- --------
-- 516930
-- 5. 음주를 하는 사람의 허리 둘레를 높은순(내림차순) 5명
SELECT * FROM healthcare WHERE is_drinking=1 AND NOT waist = "" ORDER BY waist DESC LIMIT 5;
-- 6. 시력이 양쪽 1.5 이상 이면서(AND) 음주를 하는 사람(AND) 사람의 수(COUNT)
SELECT COUNT(*) FROM healthcare WHERE (va_left >= 1.5 AND va_right >=1.5) AND is_drinking=1;
-- COUNT(*)
-- --------
-- 36697
-- 7. 혈압이 정상범위(120)미만인 사람의 수
SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
-- COUNT(*)
-- --------
-- 360808
-- 8. 혈압이 140 이상인 사람들의 평균 허리 둘레
SELECT avg(waist) FROM healthcare WHERE blood_pressure >= 140;
-- avg(waist)
-- ----------------
-- 85.8665098512525
-- 9. 성별이 1인 사람의 평균 키와 몸무게
SELECT avg(height), avg(weight) FROM healthcare WHERE gender=1;
-- avg(height)       avg(weight)
-- ----------------  ----------------
-- 167.452735422145  69.7131620222875
-- 10. 키가 가장 큰 사람 중 두번째 무거운 사람의 id, 키, 몸무게를 출력
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
-- id      height  weight
-- ------  ------  ------
-- 836005  195     110
-- 11. MBI가 30 이상인 사람의 수를 출력
SELECT COUNT(*) FROM healthcare WHERE weight/((height*0.01)*(height*0.01)) >= 30;
-- COUNT(*)
-- --------
-- 53121
-- 12. 흡연이 3 인 사람의 BMI수가 제일 높은 사람 5명
SELECT id, weight/((height*0.01)*(height*0.01)) as BMI FROM healthcare WHERE smoking=3 ORDER BY weight/((height*0.01)*(height*0.01)) DESC LIMIT 5;
-- id      BMI
------  ----------------
-- 231431  50.78125
-- 934714  49.9479708636837
-- 722707  48.828125
-- 947281  47.7502295684114
-- 948801  47.7502295684114
-- 13. BMI가 제일 낮은 사람 id, BMI 보기
SELECT id, weight/((height*0.01)*(height*0.01)) as BMI FROM healthcare ORDER BY BMI ASC LIMIT 5;
-- id      BMI
-- ------  ----------------
-- 403134  10.3806228373702
-- 758886  10.3806228373702
-- 499197  11.0192837465565
-- 139543  11.71875
-- 268110  11.71875
-- 14. 양쪽 시력이 0.8 이하인 사람의 평균 나이와 평균 키, 가장 큰 몸무게 를 출력
SELECT AVG(age), AVG(height), MAX(weight) FROM healthcare WHERE va_left <= 0.8 and va_right <= 0.8;
-- AVG(age)          AVG(height)       MAX(weight)
-- ----------------  ----------------  -----------
-- 12.9852899298195  157.989729213206  135
-- 15. 혈압이 130 ~ 140 에 포함된 사람의 id, height, weight ,BMI 20명 출력
SELECT id, height, weight, blood_pressure, weight/((height*0.01)*(height*0.01)) as BMI FROM healthcare WHERE blood_pressure >= 130 and blood_pressure <= 140 ORDER BY blood_pressure DESC LIMIT 20;
-- id   height  weight  blood_pressure  BMI
-----  ------  ------  --------------  ----------------
-- 21   165     70      140             25.7116620752984
-- 65   165     50      140             18.3654729109275
-- 85   170     75      140             25.9515570934256
-- 157  155     60      140             24.9739854318418
-- 168  150     60      140             26.6666666666667
-- 270  170     85      140             29.4117647058824
-- 342  190     90      140             24.9307479224377
-- 346  145     55      140             26.1593341260404
-- 399  165     70      140             25.7116620752984
-- 411  150     55      140             24.4444444444444
-- 454  160     55      140             21.484375
-- 486  170     85      140             29.4117647058824
-- 504  175     85      140             27.7551020408163
-- 600  150     55      140             24.4444444444444
-- 602  145     55      140             26.1593341260404
-- 738  170     75      140             25.9515570934256
-- 770  165     100     140             36.7309458218549
-- 873  170     55      140             19.0311418685121
-- 885  165     55      140             20.2020202020202
-- 913  160     55      140             21.484375