const fs = require('fs');
const commands = fs.readFileSync(0).toString().trim().split('');

let pos = [0,0];
let moves = [
    [1,0],
    [0,1],
    [-1,0],
    [0,-1]
]
let direction = 0;
for(c of commands){
    if(c === 'L'){
        direction = (direction - 1 + 4) % 4
    }
    else if (c === 'R'){
        direction = (direction + 1) % 4
    }
    else{
        pos = [pos[0]+moves[direction][0],pos[1]+moves[direction][1]]
    }
}
console.log(pos[1],pos[0])