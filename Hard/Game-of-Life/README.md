# Game of Life

Time limit: *1200 ms*
Memory limit: *128 MB*



You are asked to make an implementation of the [game of life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) by John Horton Conway on a finite torus board and provide its output after ccc iterations.



## Standard input

On the first line of the input there will be three integers nnn, mmm (1≤n,m≤251 \leq n, m \leq 251≤n,m≤25) and ccc(1≤c≤1071 \leq c \leq 10^71≤c≤107). nnn and mmm give the size of the board and ccc gives the number of iterations that you must simulate.

On the following nnn lines there will be mmm characters, either `*` or `-`, each one representing the value of each cell of the board. `*` represents a *populated* cell and `-` an *unpopulated* one.

Please note that the bottom neighbours of the last line are cells in the top line, and the left neighbours of the first column are the cells of the last column.

## Standard output

On the output there should be nnn lines of mmm characters each, which represent the state of the board after ccciterations.

## Constraints and notes

- 1≤n,m≤251 \leq n, m \leq 251≤n,m≤25
- 1≤c≤1071 \leq c \leq 10^71≤c≤107 




