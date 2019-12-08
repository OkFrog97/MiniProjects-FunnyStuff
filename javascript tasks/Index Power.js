function indexPower(array, n){
    let answ = array[n]**n;
    if (answ) {
        return answ;
    }
    return -1;
}


function indexPower(array, n){
    return (array[n]**n) ? array[n]**n : -1;
}