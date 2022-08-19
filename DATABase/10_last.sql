-- AC/DC 모든 앨범 검색
-- AC/DC = artists
-- 앨범 = albums

-- 앨범을 검색하려는데
-- 아티스트는 id로 저장
-- ac/dc id 를 모름

-- id 조회
SElECT ArtistId
FROM artists
WHERE name = 'Nirvana';
-- ArtistId
-- --------
-- 110

-- 서브쿼리
SELECT *
FROM albums
WHERE ArtistId = (SELECT ArtistId 
FROM artists WHERE name='Nirvana');
-- AlbumId  Title                                       ArtistId
-- -------  ------------------------------------------  --------
-- 163      From The Muddy Banks Of The Wishkah [Live]  110
-- 164      Nevermind                                   110