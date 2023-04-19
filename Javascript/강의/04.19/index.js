// // javascript는 매개변수의 수가 달라도 함수에서 에러가 발생하지 않음

// //javascript spread 응용
// const restArgs=function(arg1, arg2, ...restArgs){
//     return [arg1, arg2, restArgs];
// }

// console.log(restArgs(1,2,3,4,5));

// //화살표 함수 연습
// const arrow1=function(name){
//     return 'hello ${name}'
// }

// //1. function 키워드 생략 가능
// const arrow2=(name)=>{
//     return 'hello ${name}'
// }

// //2. 원소가 한개인 경우 ()생략 가능
// const arrow3=name=>{
//     return 'hello ${name}'
// }

// //3. 함수 바디가 return을 포함한 표현식 1개인 경우
// //{}와 return 생략 가능
// const arrow4=name=>'hello ${name}'


//this
// console.log(this);

// let x=1;

// function first(){
//     let x=10;
//     second();
// }

// function second(){
//     console.log(x);
// }

// first();
// second();

// const tests=[90, 90, 80, 77];

// //함수 따로 만들어서 정의
// const sum=function(total, x){
// 	return total+x
// };

// const tests_sum=tests.reduce(sum, 0);
// console.log(tests_sum);
// //337

// const sum=(a, b)=>{
//     return a+b;
// }

// console.log(sum(1,2));

// function Foo(name){
//     //this는 나중에 생성자로 생성할 인스턴스를 가르킴
//     this.name=name;
//     console.log(this);
// }

// const new_name=new Foo('woo');
// console.log(new_name.name);

// const obj={
//     f:function(){
//         console.log(this);
//     }
// };

// obj.f();

function test(){

}

function aaaa(f){
    f();
}

aaaa(test)