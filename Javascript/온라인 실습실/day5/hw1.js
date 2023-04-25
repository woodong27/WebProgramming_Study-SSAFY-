axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log((response.data))
})

/*
동기
입력받은 명령을 순서대로 실행
만약 앞의 명령이 시간이 오래 걸린다면 뒤에 오는 명령은 계속 대기해야함

비동기
빨리 처리되는 명령부터 처리하고 오래 걸리는 작업은 나중에 처리함
*/