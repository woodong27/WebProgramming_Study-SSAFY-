--problem1
--animals 테이블 생성
CREATE TABLE animals(
animal_name TEXT NOT NULL,
height INT NOT NULL,
weight INT NOT NULL,
age INT
);


--meal이라는 새 column추가
ALTER TABLE animals ADD COLUMN meal TEXT;

--animal_name column명을 name으로 변경
ALTER TABLE animals RENAME COLUMN animal_name TO name;

--table명을 zoos로 변경
ALTER TABLE animals RENAME TO zoos;

--zoos 테이블 삭제
DROP TABLE zoos;


--problem2
--zoo table 생성
CREATE TABLE zoo(
name TEXT NOT NULL,
eat TEXT NOT NULL,
weight INT NOT NULL,
height INT,
age INT
);

--빈 값을 넣으면 어떻게 나오는지 확인용
INSERT INTO zoo('name', 'eat', 'weight')
VALUES
('a','b',1);

--zoo 테이블에 데이터 추가
INSERT INTO zoo
VALUES
('gorilla', 'omnivore', 215, 180, 5),
('rabbit', 'herbivore', 3, 150, NULL),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('eagle', 'carnivore', 8 ,75, NULL),
('dolphin', 'carnivore', 210, NULL, 3),
('alligator', 'carnivore', 250, 50, NULL),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

--모든 동물의 이름과 키를 조회
SELECT name, height
FROM zoo;

--토키의 키를 15로 수정
UPDATE zoo
SET height=15
WHERE name='rabbit';

--잡식(omnivore)만 삭제
DELETE FROM zoo
WHERE eat='omnivore';


--problem3
--hotels 테이블 생성
CREATE TABLE hotels(
room_num TEXT NOT NULL,
check_in TEXT NOT NULL,
check_out TEXT NOT NULL,
grade TEXT NOT NULL
);

--null이 허영되지 않는 숫자를 저장하는 price컬럼 추가
ALTER TABLE hotels ADD COLUMN price INT NOT NULL DEFAULT 900;

--hotels에 데이터 추가
INSERT INTO hotels
VALUES
('B203', '2021-12-31', '2022-01-03', 'suite', 900),
('1102', '2022-01-04', '2022-01-08', 'suite', 850),
('303', '2022-01-01', '2022-01-03', 'deluxe', 500),
('807', '2021-01-04', '2022-01-07', 'superior', 300),
('B205', '2022-01-04', '2022-01-07', 'deluxe', 550);

--방 번호가 807인 데이터에서 체크인 날짜를 2022-01-04로 수정
UPDATE hotels
SET check_in='2022-01-04'
WHERE room_num='807';

--객실의 위치가 지하거나 등급이 deluxe인 객실 모든 정보 조회
SELECT *
FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';


--problem3
--users table 생성
CREATE TABLE users(
first_name TEXT,
last_name TEXT NOT NULL,
age INT NOT NULL,
country TEXT NOT NULL,
phone TEXT,
balance INT NOT NULL
);

--table에 값 추가
INSERT INTO users
VALUES
('미현', '김', 19, '경기도', '011-211-8482', 300),
(NULL, '최', 33, '제주특별자치도', NULL, 300),
('미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
('남석', '박', 18, '경기도', '011-484-8667', 260),
('철수', '박', 22, '경상남도', '016-295-8989', 500),
(NULL, '박', 45, '전라북도', NULL, 320),
('민준', '이', 35, '전라남도', '019-965-8833', 350),
(NULL, '남', 24, '충청남도', '010-5882-5969', 210),
('신', '유', 29, '경상북도', '010-4949-2848', 290),
(NULL, '김', 18, '대전광역시', NULL, 300);

--나이가 25미만인 사람들의 id, age, balance정보, age내림차순, balance 오름차순
SELECT rowid AS id, age, balance
FROM users
WHERE age<25
ORDER BY age DESC, balance;

--first_name이 존재하는 사람들 중 balance가 400보다 큰 사람들
SELECT first_name, balance
FROM users
WHERE first_name!='NULL' AND balance>400;