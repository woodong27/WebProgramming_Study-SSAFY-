CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

--day1_problem1
--이름, 나이, 계좌 잔고를 나이가 어린순으로, 같은 나이면 잔고가 많은순으로 정렬해서 조회
SELECT first_name, age, balance
FROM users
ORDER BY age, balance DESC;

--day1_problem4
--전화번호 중간자리가 51로 시작하고 지역이 서울이 아닌 사람들의 이름과 번호 조회
SELECT first_name, phone, country
FROM users
WHERE country!='서울' and phone LIKE '%-51__-%'

--day1_problem5
--나이 어린 순서대로 조회, 페이지당 출력은 20개로 제한, 3번째 페이지를 출력
SELECT *
FROM users
ORDER BY age
LIMIT 20 OFFSET 3;

--day1_problem3
--이름이 건우고 지역정보가 경기도인 데이터를 조회
SELECT first_name, country
FROM users
WHERE first_name='건우' AND country='경기도';

--경기도 혹은 강원도에 살지 않는 사람들 중 나이가 20살 이상, 30살 이하인 사람들의 데이터를 나이 기준 오름차순
SELECT *
FROM users
WHERE age BETWEEN 20 AND 30 AND country NOT IN ('경기도', '강원도')
ORDER BY age;

--day1_problem2
--이름 오름차순, 나이 내림차순 정렬
SELECT first_name, age
FROM users
ORDER BY first_name, age DESC;