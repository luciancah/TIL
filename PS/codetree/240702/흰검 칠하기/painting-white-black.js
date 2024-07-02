const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = Number(input[0])
const commands = input.slice(1,n+1).map(line=>line.split(' '))
const MAX_K = 100000;
const a = Array(2*MAX_K + 1).fill(0)
const cntB = Array(2*MAX_K + 1).fill(0)
const cntW = Array(2*MAX_K + 1).fill(0)
let b = 0, w = 0, g = 0;

let cur = MAX_K

for (c of commands){
    let [x,command] = c
    x = Number(x)
    if (command === 'L'){
        while (x > 0){
            a[cur] = 1;
            cntW[cur] +=1;
            x -= 1;
            if (x){
                cur -=1;
            }
        }
    }
    else{
        while (x > 0 ){
            a[cur] = 2;
            cntB[cur] += 1;
            x -= 1;
            if(x){
                cur += 1;
            }
        }
    }
}
for (let i = 0; i < 2 * MAX_K + 1; i++){
    if (cntB[i] >= 2 && cntW[i] >= 2){
        g += 1;
    }
    else if (a[i] == 1){
        w += 1
    }
    else if (a[i] === 2){
        b += 1
    }
}
console.log(w,b,g);