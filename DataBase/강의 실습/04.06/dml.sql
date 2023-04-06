-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

--users의 전체 데이터 수를 세어줌
SELECT COUNT(*)
FROM users;

--전체 유저의 평균 잔고 계산
SELECT AVG(balance)
FROM users;

--중복없이 지역 조회
SELECT DISTINCT country
FROM users;

--전라북도의 평균 balance계산
SELECT country, AVG(balance)
FROM users
WHERE country='전라북도';

--각 지역별로 잔고 평균 조회
SELECT country, AVG(balance)
FROM users
GROUP BY country
ORDER BY AVG(balance) DESC;

--나이가 30이상인 사람들의 평균 나이
SELECT AVG(age)
FROM users
WHERE age>=30;

--각 지역별로 몇 명씩 살고 있는지 조회
--지역별로 그룹이 나누어졌기 때문에 COUNT(*)는 지역별 데이터 수를 세어줌
SELECT country, count(*)
FROM users
GROUP BY country;

--각 성씨가 몇명씩 있는지 조회
SELECT last_name, count(*)
FROM users
GROUP BY last_name;

--AS를 사용해서 컬럼명 임시로 변경
SELECT last_name, count(*) AS number_of_name
FROM users
GROUP BY last_name;


--Changing Data

--classmates table 생성
CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

--INSERT : 새 행을 테이블에 삽입

--column 순서를 생략하면 테이블의 column순서대로 들어가게 됨
INSERT INTO classmates(name, age, address)
VALUES ('홍길동', 23, '서울');

--여러 행 삽입
INSERT INTO classmates
VALUES
('김철수',30,'경기'),
('이영미',31,'강원'),
('박진성',26,'전라'),
('최지수',12,'충청'),
('정요한',28,'경상');


--UPDATE : 테이블의 값을 수정

--2번 데이터의 이름과 주소를 변경
UPDATE classmates
SET name='김수한무두루미', address='제주'
WHERE rowid=2;


--DELETE : 테이블의 행을 제거(한개/여러개 삭제 모두 가능)

--5번 데이터 삭제
DELETE FROM classmates
WHERE rowid=5;

--rowid와 전체 테이블 조회
SELECT rowid, *
FROM classmates;

--이름에 영이 포함되는 데이터 삭제하기
DELETE FROM classmates
WHERE name LIKE '%영%';

--테이블의 모든 데이터 삭제
DELETE FROM classmates;