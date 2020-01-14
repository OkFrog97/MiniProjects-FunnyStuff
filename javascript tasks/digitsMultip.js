function digitsMultip(data) {
    
    let d = String(data).split('');
    let answ = 1;
    for (let i = 0; i < d.length; i++) {
        if (d[i] != 0) {
            answ = answ * d[i];
        }
    }
    return answ;
}