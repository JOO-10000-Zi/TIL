--  1. playlist_track 테이블 A별칭 데이터 출력
SELECT * 
FROM playlist_track AS A
ORDER BY playlistId DESC
LIMIT 5;
-- PlaylistId  TrackId
-- ----------  -------
-- 18          597
-- 17          3290
-- 17          2096
-- 17          2095
-- 17          2094

-- 2. tracks 테이블에 B별칭 부여 데이터 출력
SELECT *
FROM tracks AS B
ORDER BY B.TrackId
LIMIT 5;
-- rackId  Name                                     AlbumId  MediaTypeId  GenreId  
-- Composer                                                      Milliseconds  Bytes     UnitPrice
-- -------  ---------------------------------------  -------  -----------  -------  
-- ------------------------------------------------------------  ------------  --------  ---------
-- 1        For Those About To Rock (We Salute You)  1        1            1        
-- Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99

-- 2        Balls to the Wall                        2        2            1        
--                                                               342562        5510424   0.99

-- 3        Fast As a Shark                          3        2            1        
-- F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

-- 4        Restless and Wild                        3        2            1        
-- F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99

-- W. Hoffman
-- 5        Princess of the Dawn                     3        2            1        
-- Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99

-- 3. 각 playlist_track 해당하는 track 함께 출력
SELECT PlaylistId, Name
FROM playlist_track
JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;
-- PlaylistId  Name
-- ----------  -----------------------
-- 18          Now's The Time
-- 17          The Zoo
-- 17          Flying High Again
-- 17          Crazy Train
-- 17          I Don't Know
-- 17          Looks That Kill
-- 17          Live To Win
-- 17          Ace Of Spades
-- 17          Creeping Death
-- 17          For Whom The Bell Tolls

-- 4. playlistId 가 10인 track 데이터 출력
SELECT PlaylistId, Name
FROM playlist_track
JOIN tracks
    ON playlist_track.TrackId = tracks.TrackId
WHERE PlaylistId = 10
ORDER BY Name DESC
LIMIT 5;
-- PlaylistId  Name
-- ----------  ------------------------
-- 10          Women's Appreciation
-- 10          White Rabbit
-- 10          Whatever the Case May Be
-- 10          What Kate Did
-- 10          War of the Gods, Pt. 2

-- 5. tracks 테이블 기준으로 tracks Composer 와 artists테이블 Name를 LEFT JOIN해서 출력
SELECT COUNT(*)
FROM tracks
JOIN artists
        ON tracks.Composer = artists.Name

-- COUNT(*)
-- --------
-- 402

-- 6. tracks 테이블 기준 tracks Composer 와 artists 테이블의 Name을 LEFT JOIN 해서 출력
SELECT COUNT(*)
FROM tracks
LEFT JOIN artists
        ON tracks.Composer = artists.Name
-- COUNT(*)
-- --------
-- 3503

-- 7. INNER JOIN 과 LEFT JOIN 행의 개수가 다른 이유를 작성 하시오
INNER JOIN : 두 테이블 중 같은 값을 교차집합으로 뽑아서 출력은 하는 것
LEFT JOIN : 기준이 되는 테이블 교차갑 제외 데이터와 과 조인 되는 테이블과의 교차값이 모두 출력 되는 것

-- 8. invoice_items 테이블 데이터를 출력하세요
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;
-- InvoiceLineId  InvoiceId
-- -------------  ---------
-- 1              1
-- 2              1
-- 3              2
-- 4              2
-- 5              2

-- 9. invoices 테이블의 데이터를 출력
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
-- InvoiceId  CustomerId
-- ---------  ----------
-- 1          2
-- 2          4
-- 3          8
-- 4          14
-- 5          23

-- 10. 각 invoice_item에 해당하는 invoive 데이터 함께 출력
SELECT InvoiceLineId, invoice_items.InvoiceId
FROM invoice_items
JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;
-- SELECT 구문 에서 invoice_items.InvoiceId 동일 테이블이 있어서 테이블 지정 해야 오류 X
-- InvoiceLineId  InvoiceId
-- -------------  ---------
-- 2240           412
-- 2239           411
-- 2238           411
-- 2237           411
-- 2236           411

-- 11. 각 invoice에 해당하는 customer 데이터 출력
SELECT InvoiceId, customers.CustomerId
FROM invoices
JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
-- InvoiceId  CustomerId
-- ---------  ----------
-- 412        58
-- 411        44
-- 410        35
-- 409        29
-- 408        25

-- 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력
SELECT InvoiceLineId, invoice_items.InvoiceId, invoices.CustomerId
FROM invoice_items
JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;
-- InvoiceLineId  InvoiceId  CustomerId
-- -------------  ---------  ----------
-- 2240           412        58
-- 2239           411        44
-- 2238           411        44
-- 2237           411        44
-- 2236           411        44

-- 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력
SELECT customers.CustomerId, COUNT(*)
FROM customers
JOIN invoices
    ON customers.CustomerId = invoices.CustomerId
JOIN invoice_items
    ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId
LIMIT 5;
-- CustomerId  COUNT(*)
-- ----------  --------
-- 1           38
-- 2           38
-- 3           38
-- 4           38
-- 5           38