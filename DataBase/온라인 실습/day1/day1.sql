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
LIMIT 20;