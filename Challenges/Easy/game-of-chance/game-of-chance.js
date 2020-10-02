function main() {
    [N, A, B] = [nextInt(), nextInt(), nextInt()];

    for(let i = 0; i < N * 2; ++i) {
        if(i < N) {
            A += nextInt();
        } else {
            B += nextInt();
        }
    }

    // Shorthand Ternary operator for the if statement below
    console.log(A > B ? 1 : A < B ? 2 : 0);
    /*
    if(A > B) {
        console.log(1);
    } else if (A < B) {
        console.log(2);
    } else {
        console.log(0);
    } */
}
