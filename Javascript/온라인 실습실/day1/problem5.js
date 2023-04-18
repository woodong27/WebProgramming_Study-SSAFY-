const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

function find_alone(numbers){
    len=numbers.length;
    for (let i=0;i<len;i++){
        let cnt=0;
        for (let j=i+1;j<len;j++){
            if (numbers[i]===numbers[j]){
                cnt+=1;
            }
        }
        if (cnt===0){
            return numbers[i];
        }
    }
}

for (const game of participantNums){
    console.log(find_alone(game));
}