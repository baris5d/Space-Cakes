int bitRemoval(int x, int y) {
    return x ^ (x & y);
}

/* Most of the languages have the same syntax for bitwise operators so it will work on almost every language.
    Also JavaScript exceeds the time limit, that's why I chose C++ for this one.
 */
