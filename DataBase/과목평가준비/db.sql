-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

--객관식 3번
SELECT DISTINCT country
FROM users;

--객관식 4번
SELECT first_name, last_name, age
FROM users
WHERE last_name='이' AND age>=30;

--객관식 5번
SELECT first_name, last_name, age
FROM users
WHERE last_name='이' OR age>=30;

--객관식 10번
SELECT first_name, last_name, age
FROM users
WHERE age BETWEEN 20 AND 29;
--또는
SELECT first_name, last_name, age
FROM users
WHERE age>=20 AND age<30;

--객관식 13번
SELECT first_name, age
FROM users
ORDER BY age ASC;

--단답식 1번(GROUP BY)
--예시 1. 지역별 평균 balance
SELECT country, AVG(balance)
FROM users
GROUP BY country;
--지역별 사는 사람 수
SELECT country, COUNT(*)
FROM users
GROUP BY country;
--성씨별 사람 수
SELECT last_name, COUNT(*) AS num_of_people
FROM users
GROUP BY last_name;
--ORDER BY COUNT(*) 를 추가하면 사람 수 순으로 정렬

--단답식 3번, 집계함수
SELECT COUNT(*)
FROM users;

