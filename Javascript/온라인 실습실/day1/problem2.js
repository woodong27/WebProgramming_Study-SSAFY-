words=['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word){
    const len_word=word.length;
    for (let i=0;i<parseInt(len_word/2);i++){
        if (word[i]!=word[len_word-1-i]){
            return false;
        }
    }
    return true;
}

for (const word of words){
    console.log(palindrome(word));
}