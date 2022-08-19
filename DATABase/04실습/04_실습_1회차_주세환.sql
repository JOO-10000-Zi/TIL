-- 1.  데이터 열기
-- sqlite3 sample.sqlite3
-- 테이블 조회
-- .table 
-- albums          employees       invoices        playlists
-- artists         genres          media_types     tracks
-- customers       invoice_items   playlist_track

-- 2. 모든 데이터 확인
-- 눈버깅

-- 3. 앨범 테이블 데이터 출력 5개 내림차순
SELECT *
FROM albums
ORDER BY Title DESC
LIMIT 5;
-- AlbumId  Title                         ArtistId
-- -------  ----------------------------  --------
-- 208      [1997] Black Light Syndrome   136
-- 240      Zooropa                       150
-- 267      Worlds                        202
-- 334      Weill: The Seven Deadly Sins  264
-- 8        Warner 25 Anos                6

-- 4. 고객 테이블의 행 개수 출력(단, 컬럼명 고객 수)
SELECT COUNT(firstName) '고객 수'
FROM customers;
-- 고객 수
-- ----
-- 59

-- 5. 고객이 사는 나라사 USA인 고객의 풀 네임 출력(이름 기준 내림차 5명)
SELECT FirstName 이름, LastName 성
FROM customers
WHERE Country = 'USA'
ORDER BY FirstName DESC
LIMIT 5;
-- 이름        성
-- --------  ----------
-- Victor    Stevens
-- Tim       Goyer
-- Richard   Cunningham
-- Patrick   Gray
-- Michelle  Brooks

-- 6. 송장 테이블에서 Billingpostalcode가 NULL이 아닌 행 개수
SELECT COUNT(*) 송장수
FROM invoices
WHERE Billingpostalcode IS NOT NULL;
-- 송장수
-- ---
-- 384

-- 7. 송장 테이블 Billingstate 가 NULL인 데이터
SELECT *
FROM invoices
WHERE BillingState IS NULL 
ORDER BY InvoiceDate DESC
LIMIT 5;
-- 생략 --

-- 8. 송장 테이블 InvoiceDate 년도가 2013년인 행의 수
SELECT COUNT(*)
FROM invoices
WHERE strftime("%Y",InvoiceDate) = "2013";
-- COUNT(*)
-- --------
-- 80

-- 9. 고객 테이블 FirstName이 L로 시작 하는 고객의 CustomerID, FirstName, LastName 출력
SELECT CustomerID 고객ID, FirstName 이름, LastName 성
FROM customers
WHERE FirstName LIKE "L%"
ORDER BY 고객ID;
-- 고객ID  이름        성
-- ----  --------  ---------
-- 1     Luis      Goncalves
-- 2     Leonie    Kohler
-- 45    Ladislav  Kovacs
-- 47    Lucas     Mancini
-- 57    Luis      Rojas

-- 10. 고객 테이블 각 나라의 고개 수와 해당 나라의 이름 출력
SELECT COUNT(*) "고객 수", Country 나라
FROM customers
GROUP BY Country
ORDER BY "고객 수" DESC
LIMIT 5;
-- 고객 수  나라
-- ----  -------
-- 13    USA
-- 8     Canada
-- 5     France
-- 5     Brazil
-- 4     Germany

-- 11. 앨범 테이블 에서 앨범이 가장 많은 아티스트의 ID와 앨범 수
SELECT ArtistID, COUNT(*) "앨범 수"
FROM albums
GROUP BY ArtistID
ORDER BY "앨범 수" DESC
LIMIT 1;
-- ArtistId  앨범 수
-- --------  ----
-- 90        21

-- 12. 앨범 보유수 10개 이상 ArtistID, 앨범수
SELECT ArtistID, COUNT(*) "앨범 수"
FROM albums
GROUP BY ArtistID
HAVING "앨범 수" >= 10
ORDER BY "앨범 수" DESC;
-- ArtistId  앨범 수
-- --------  ----
-- 90        21
-- 22        14
-- 58        11
-- 50        10
-- 150       10

-- 13. 고객 테이블 State 존재 하는 고객 Country, State 기준 구룹, 각가 고객 수 
SELECT COUNT(*) "고객 수", Country, State
FROM customers
WHERE State IS NOT NULL
GROUP BY Country, State
ORDER BY "고객 수" DESC, Country DESC
LIMIT 5;
-- 고객 수  Country  State
-- ----  -------  -----
-- 3     USA      CA
-- 3     Brazil   SP
-- 2     Canada   ON
-- 1     USA      WI
-- 1     USA      WA

-- 14. 고객 테이블 Fax = NULL 이면 X 아니면 O
SELECT 
    CustomerID,
    CASE
        WHEN Fax IS NULL THEN "X"
        ELSE "O"
    END "Fax 유/무"
FROM customers
ORDER BY CustomerID
LIMIT 5;
-- CustomerId  Fax 유/무
-- ----------  -------
-- 1           O
-- 2           X
-- 3           X
-- 4           X
-- 5           O

-- 15. 점원 테이블의 올해 년도 - 생일년도 + 1 계산해 나이 추출
SELECT LastName, FirstName, (strftime("%Y", "NOW") - strftime("%Y", BirthDate) + 1) 나이
FROM employees
ORDER BY EmployeeID;
-- LastName  FirstName  나이
--------  ---------  --
-- Adams     Andrew     61
-- Edwards   Nancy      65
-- Peacock   Jane       50
-- Park      Margaret   76
-- Johnson   Steve      58
-- Mitchell  Michael    50
-- King      Robert     53
-- Callahan  Laura      55

-- 16. 가수 테이블 앨범 의 개수 가장 많은 가수 Name 출력
SELECT ArtistID
FROM albums
GROUP BY ArtistID
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT Name
FROM artists
WHERE ArtistID = (SELECT ArtistID
FROM albums
GROUP BY ArtistID
ORDER BY COUNT(*) DESC
LIMIT 1);
-- Name
-- -----------
-- Iron Maiden

-- 17. 장르 테이블 음악(tracks) 개수가 가장 적은 장의 이름 출력
SELECT GenreID
FROM tracks
GROUP BY GenreID
ORDER BY COUNT(*)
LIMIT 1;
-- COUNT(*)
-- --------
-- 1
SELECT Name
FROM genres
WHERE GenreID = (SELECT GenreID
FROM tracks
GROUP BY GenreID
ORDER BY COUNT(*)
LIMIT 1);
-- Name
-- -----
-- Opera
