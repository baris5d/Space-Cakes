const HEIGHT = 4;
const WIDTH = 6;
const FRAME = 1;

let GRID = '-----*\n--*---\n*-----\n-***-*'.split('\n').map(x => x.split(''));
let tmpGRID = createTemplate();


function createTemplate() {
    let tmp = new Array();

    for(let y = 0; y < HEIGHT; y++) {
        tmp[y] = new Array();
        for(let x = 0; x < WIDTH; x++) {
            tmp[y][x] = '-';
        }
    } 
    
    return tmp;
}



for(let f = 0; f < FRAME; f++) { // Her frame'i gez

    for(let y = 0; y < HEIGHT; y++) {
        for(let x = 0; x < WIDTH; x++) {
            liveOrDie(y, x);
        }
    }
    GRID = tmpGRID;
    tmpGRID = createTemplate();

}

function liveOrDie(y, x) {
    neighbourCount = 0;

    let isAlive = isPopulated(y, x);

    let top    = y == 0 ? HEIGHT - 1 : y - 1;
    let bottom = y == HEIGHT - 1 ? 0 : y + 1;

    let left   = x == 0 ? WIDTH - 1 : x - 1;
    let right  = x == WIDTH - 1 ? 0 : x + 1;

    neighbourCount += isPopulated(top, left) ? 1 : 0;
    neighbourCount += isPopulated(top, x) ? 1 : 0;
    neighbourCount += isPopulated(top, right) ? 1 : 0;

    neighbourCount += isPopulated(y, left) ? 1 : 0;
    neighbourCount += isPopulated(y, right) ? 1 : 0;

    neighbourCount += isPopulated(bottom, left) ? 1 : 0;
    neighbourCount += isPopulated(bottom, x) ? 1 : 0;
    neighbourCount += isPopulated(bottom, right) ? 1 : 0;

    if(isAlive && (neighbourCount < 2 || neighbourCount > 3)) {
        tmpGRID[y][x] = '-';
    } else if(!isAlive && neighbourCount == 3) {
        tmpGRID[y][x] = '*';
    } else if (isAlive) {
        tmpGRID[y][x] = '*';
    }
}

function isPopulated(y, x) {
    return GRID[y][x] == '*';
}

let output = "";
GRID.forEach(x => {
    output += x.join('') + "\n";
})

console.log(output);