-- 1. 흡연 여부 구분 각 그룹 컬럼명 그룹의 사람 수
SELECT smoking 흡현, COUNT(*) 인원수
FROM healthcare
GROUP BY smoking
HAVING SMOKING != "";
-- 2. 음주 여부 구분 각 그룹 컬럼명 그룹의 사람 수
SELECT is_drinking 음주, COUNT(*) 인원수
FROM healthcare
GROUP BY is_drinking
HAVING is_drinking != "";
-- 3. 음주 여부로 구분한 각 그룹의 혈압이 200 이상인 사람
SELECT is_drinking 음주, COUNT(*) 인원수
FROM healthcare
WHERE blood_pressure >= 200
GROUP BY is_drinking
HAVING NOT blood_pressure <> "";
-- 4. 시도에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에사는
    -- 사람의 수
SELECT sido 시도, COUNT(*) 주민수
FROM healthcare
GROUP BY sido
HAVING COUNT(sido) >= 50000;
-- 5. 키로 구분 하고 키와 사람의 수
SELECT height 키, COUNT(*) 인원
FROM healthcare
GROUP BY height
ORDER BY 인원 DESC
LIMIT 5;
-- 6. 키와 몸무게 로 그룹, 몸무게, 키, 해당사람의 수
SELECT weight 몸무게, height 키, COUNT(*) 인원
FROM healthcare
GROUP BY  키, 몸무게
ORDER BY 인원 DESC
LIMIT 5;
-- 7. 음주 여부 평균 허리 둘레 사람의 수
SELECT is_drinking 음주, ROUND(avg(waist), 2) 허리, COUNT(*)
FROM healthcare
GROUP BY is_drinking
HAVING NOT is_drinking="";
-- 8. 각 성병의 평균 왼쪽 시력 과 오른쪽 시력 출력
SELECT gender 성별, ROUND(AVG(va_left), 2) '평균 왼쪽 시력', ROUND(AVG(va_right), 2) '평균 오른쪽 시력'
FROM healthcare
GROUP BY gender; 
-- 9. 각 나이대 의 평균 키, 몸무게 출력
SELECT age 나이대, ROUND(AVG(height), 2) '평균 키', ROUND(AVG(weight), 2) '평균 몸무게'
FROM healthcare
GROUP BY age
HAVING AVG(height) >= 160 AND AVG(weight) >=60;
-- 10. 음주 와 흡연 따른 BMI 출력
SELECT is_drinking 음주, smoking 흡연, ROUND(AVG(weight/((height*0.01)*(height*0.01))), 2) BMI
FROM healthcare
GROUP BY 음주, 흡연
HAVING NOT 음주="" AND NOT 흡연="";