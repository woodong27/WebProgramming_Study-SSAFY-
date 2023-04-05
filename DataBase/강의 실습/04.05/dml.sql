CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

--나이순으로 오름차순, 나이가 같으면 잔고 순으로 내림차순
SELECT first_name, age, balance
FROM users
ORDER BY age, balance DESC;

--지름과 지역을 조회해서 지역순으로 오름차순
SELECT DISTINCT first_name, country
FROM users
ORDER BY country;

--이름과 나이 잔고를 가져와서 나이가 30이상, 잔고가 50초과인 사람만 출력
SELECT first_name, age, balance
FROM users
WHERE age>=30 and balance >500000;

--이름에 호가 들어가는 모든 사람들 출력
SELECT first_name
FROM users
WHERE first_name LIKE '%호%';

--이름이 준으로 끝나는 사람들 출력
SELECT first_name
FROM users
WHERE first_name LIKE '%준';

--전화번호가 서울 지역인 사람들의 이름과 번호
SELECT first_name, phone
FROM users
WHERE phone LIKE '02-%';

--20대인 사람들의 이름과 나이 조회
SELECT first_name, age
FROM users
WHERE age LIKE '2_';

--전화번호 중간 4자리가 51로 시작하는 사람들의 번호
SELECT first_name, phone
FROM users
WHERE phone LIKE '%-51__-%';

--지역이 경기도나 강원도인 사람들의 이름, 지역 출력
SELECT first_name, country
FROM users
WHERE country IN ('경기도', '강원도');

--경기도 강원도에 살고있지 않는 사람들
SELECT first_name, country
FROM users
WHERE country NOT IN ('경기도', '강원도');

--나이가 20살 이상, 30살 이하인 사람들의 이름 나이
SELECT first_name, age
FROM users
WHERE age BETWEEN 20 AND 30;

--20살 미만, 30살 초과인 사람들의 이름, 나이
SELECT first_name, age
FROM users
WHERE age NOT BETWEEN 20 AND 30;

--첫번째부터 열번째 rowid와 이름 조회
SELECT rowid, first_name
FROM users
LIMIT 10;

--잔고가 가장 많은 10명의 이름과 잔고 조회
SELECT first_name, balance
FROM users
ORDER BY balance DESC
LIMIT 10;

--나이가 가장 어린 5명의 이름과 나이 조회
SELECT first_name, age
FROM users
ORDER BY age
LIMIT 5;

--rowid가 11부터 10명 조회
SELECT rowid, first_name
FROM users
LIMIT 10 OFFSET 10;