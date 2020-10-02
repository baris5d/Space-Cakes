// Parameter array is an array of integers
// The function should return an integer
function findAnyDuplicate(array) {
    let temp = [];
    for(let i = 0; i < array.length; i++) {
        if(temp.indexOf(array[i]) !== -1)
            return array[i]
        temp.push(array[i])
    }
    return 0;
}
