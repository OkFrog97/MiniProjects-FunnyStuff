function nonUniqueElements(data) {
    let answer = [];
    let count = 0;
    for (let i in data){
        for (let n in data) {
            if (data[i] == data[n]){
                count ++;
            }
        }
        if (count > 1){
            answer.push(data[i]);
            
        }
        count = 0;
    }
    return answer;
}