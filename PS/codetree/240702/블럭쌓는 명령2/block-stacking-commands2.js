const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [n,k] = input[0].split(' ').map(Number);
const segments = input.slice(1,k+1).map(line => line.split(' ').map(Number));
const blocks = Array(n+1).fill(0);

for (let i = 0; i < segments.length; i++){
    const [a,b] = segments[i];
    for (let j = a; j <= b; j++){
        blocks[j] += 1;
    }
}

const maxNum = Math.max(...blocks);
console.log(maxNum);