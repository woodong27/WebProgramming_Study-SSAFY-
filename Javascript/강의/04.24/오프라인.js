//버튼 이벤트
const btn=document.querySelector('.color')

btn.addEventListener('click', function(){
    this.classList.toggle('red')
})


//input 이벤트
const inputTag=document.querySelector('input')
inputTag.addEventListener('input', function() {
    console.log('Hello World')
    const pTag=document.querySelector('p')
    pTag.innerText=this.value
})


//Event 전파
const a=document.querySelector('.a')
const b=document.querySelector('.b')
const c=document.querySelector('.c')

//eventcapturing
// 원래는 하위->상위 노드 순서로 전파가 일어나지만(Event Bubbling)
// addEventListener의 마지막에 인자로 true를 넣어주면 상위 노드부터 하위노드로 진행(Event Capturing)
// 원래는 {capture:true} 로 해주지만 true로 넣어도 됨
// Capturing : 부모에서 target으로 내려가면서 모든 이벤트를 발생시킴


a.addEventListener('click', function(){
    event.stopPropagation()
    console.log('a click')
    console.log(event.target)
})

b.addEventListener('click', function(){
    event.stopPropagation()
    console.log('b click')
    console.log(event.target)
})

c.addEventListener('click', function(){
    // stopPropagation : 상위 노드로의 이벤트 전파를 막아줌 
    event.stopPropagation()
    console.log('c click')
    console.log(event.target)
})


//EventListener에서 function()을 사용하면 this는 무조건 객체 자신을 가르킴
const btn1=document.querySelector('.last')
btn1.addEventListener('click', function() {
    console.log(this)
})
//btn1을 출력

//화살표 함수는 무조건 상위 객체를 출력함
btn1.addEventListener('click', e => {
    console.log(this)
})
//window를 출력