// Parameter x is an integer
// The function should return an integer
function lsb(x) {
    return x & -x
}

// JavaScript uses 2's complement for negative numbers, so using AND operator with its negative presentation gives us the desired result
