// Parameter x is an integer
// The function should return an integer
function bitcount(x) {
    let count = 0;
    let b = x.toString(2);
    for(let i = 0; i < 32; ++i) {
        count += (b[i] & 1) ? 1 : 0;
    }
    return count;
}
