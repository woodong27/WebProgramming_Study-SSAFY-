// const arr=[1,2,3,4,5]

// //forEach는 값을 반환하지는 못함
// arr.forEach(element => {
//     console.log(element+1)
// })

// //반환되는 값을 저장해서 새로운 배열을 만들고싶으면 map 사용
// //map은 forEach를 대신해서 사용될 수 있음->반환되는 값을 받을 변수를 만들지 않고 그냥 사용하면 됨
// const plused_arr=arr.map(element => {
//     return element+1
// })

// console.log(plused_arr)

// //filter
// //짝수만 찾기
// const filtered_num=arr.filter(element => {
//     //if문으로 해도 가능
//     return element%2===0
// })

// console.log(filtered_num)


// const arr1=[4,3,5,1,6,5]

// let cnt=0;
// arr1.forEach(element => {
//     if(element%2){
//         cnt++;
//     }
// })

// console.log(cnt);

// //실습
// const arr2=[-5,3,4,2,-7,-2,7]
// const pplus=[];
// const mminus=[];

// arr2.forEach(element => {
//     if (element>0){
//         pplus.push(element)
//     }
//     else {
//         mminus.push(element)
//     }
// })

// console.log(pplus)
// console.log(mminus)


// //map활용
// const arr=[1,2,3,4,5]
// const square=arr.map(element => element**2)
// console.log(square)

// const arr2=['a','bcd','ef','g']
// const lengths=arr2.map(element => element.length)
// console.log(lengths)

// //[]말고 배열 만드는 방법
// //생성자 함수 Array를 사용해서 만들 수 있음
// const empty_arr=Array()
// console.log(empty_arr)

// //arr1 : 홀수만
// //arr2 : 3초과 9미만 숫자만 모아서 출력
// const arr=[1,2,3,4,5,6,7,8,9,10]
// const arr1=arr.filter(element => element%2)
// console.log(arr1)
// const arr2=arr.filter(element => 3<element && element<9)
// console.log(arr2)

// //bucketList를 작성하고 done 속성이 false인 것만 새로운 Array에 저장하여 출력
// const bucketList=[
//     {
//         id:1,
//         text:'여행 가기',
//         done:false,
//     },
//     {
//         id:2,
//         text:'치킨 먹기',
//         done:true,
//     },
//     {
//         id:3,
//         text:'코딩 하기',
//         done:true,
//     },
//     {
//         id:4,
//         text:'요리 하기',
//         done:false,
//     },
// ]

// const not_done=bucketList.filter(element => element['done']===false)
// console.log(not_done)
// console.log(bucketList.filter(e => !e.done))


//find : 결과가 true인 첫번째 원소를 반환
//some : 결과가 true인 원소가 하나라도 있으면 true반환

//reduce
//결과값으로 출력할 변수, 배열의 원소 순서대로 인자로 들어감
// const arr=[1,2,3,4,5]
// const total_sum=arr.reduce((sum, element) => sum+element)
// console.log(total_sum)

// const arr=[1,2,3,4]

// console.log(arr.reduce((acc, cur) => {
//     const data=cur*cur
//     acc.push(data)
//     return acc
// }, []))

// console.log(arr.reduce((acc, cur) => {
//     if (cur>2){
//         acc.push(cur)
//     }
//     return acc
// }, []))

// const arr=['피카츄', '라이츄', '파이리', '꼬부기', '피카츄', '파이리']

// const result=arr.reduce((acc,cur) => {
//     if(acc[cur]){
//         acc[cur]=acc[cur]+1
//     }
//     else{
//         acc[cur]=1
//     }
//     return acc
// }, [])

// console.log(result)


//객체(object)
// const me={
//     name:'woo',
//     age:27,
//     address:'Haeundae',
//     gender:'male',
//     phone:'010-3379-5548',
//     birth:'05/09/1997',
//     hobby:'solving algorithm problems',
//     baekjoon_tier:'Gold 5',
//     mbti:'?',
// }

// // 객체를 만드는 방법
// const Person=(name, age, address)=>{
//     this.name=name
//     this.age=age
//     this.address=address
//     return this
// }

// const me=Person('woo',27,'Haeunadae')
// console.log(me)

// //생성자 함수로 객체 만들기
// function Person(name, age, address){
//     this.name=name
//     this.age=age
//     this.address=address
// }

// const me=new Person('woo', 27, '해운대')
// console.log(me)


// //key가 name, value는 자기 이름인 객체를 만들어라
// const obj={
//     name:'자기이름',
// }

// //key와 value가 같으면 축약할 수 있음
// const age=99
// const obj={
//     age,   
// }
// console.log(obj.age)

// //객체 메서드명 생략
// const obj={
//     greeting() {
//         console.log('hello')
//     }
// }

// obj.greeting()

// //객체의 변수를 다른 변수에 할당하는 법
// const obj={
//     name:'자기이름',
//     age:'자기나이',
// }

// const {age}=obj
// console.log(age)

//객체 spread


// //객체에 함수 넣는거 활용(교수님코드 ~line 239)
// function test(str){
//     return str
// }

// const a = test("hello")
// // console.log(a)

// const c = "허범성"


// const obj3 = {
//     [test("hello")] : 1,
//     [test("bye")] : 2,
//     [`나는 ${c} 입니다`] : 3,
// }

// console.log(obj3.hello)
// console.log(obj3.bye)
// console.log(obj3['나는 허범성 입니다'])


// // const a = '허범성'
// // const b = "싸피"

// // console.log("나는 " + a + " 입니다 제가 일하는 곳은 " + b  + " 입니다")
// // console.log(`나는 ${a} 입니다 제가 일하는 곳은 ${b} 입니다`)


// //배열 순회해서 출력하기
// const chars=['a', 'b', 'c', 'd']

// //1
// chars.forEach(char => console.log(char))
// console.log()

// //2
// for (let i=0;i<chars.length;i++){
//     console.log(chars[i])
// }
// console.log()

// //3
// for (const char of chars){
//     console.log(char)
// }
// console.log()

// //4
// for (const idx in chars){
//     console.log(chars[idx])
// }


//짝수인 애들만 찾아서 제곱해서 출력
const arr=[1,2,3,4,5]

// arr.forEach(num => {
//     if(num%2===0){
//         console.log(num**2)
//     }
// })

//map 사용법
const temp=arr.map(num => num**2)
console.log(temp)

//결과물
const ans=arr.filter(num => !(num%2)).map(filtered => filtered**2)
console.log(ans)