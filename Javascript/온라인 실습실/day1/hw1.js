// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

/*
const로 선언된 변수는 재할당이 불가능하기 때문에 해당 에러가 발생
let으로 선언해주면 해결됨
*/

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string

/*
in 대신 of 사용해줘야 함
in은 인덱스를 조회해주는 거고 of는 원소를 조회해줌
*/