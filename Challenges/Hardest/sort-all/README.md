# Sort All
* Time limit: 1880 ms
* Memory limit: 512 MB

Let f be a function which maps an arbitrary array of integers A to the integer value 1∗S(​1) + 2 * S(2) + 3 * S(3) + ..... + K * S(K) = ∑K,i=1 i * S(i)​​ are the distinct values of AA, sorted increasingly. 

Given an array of integer V, compute the sum of f applied to all subarrays of V, i.e. ∑​1≤i≤j≤N​​ f(V[i…j]). 

Print this value modulo 10^9 + 7.


#### Standard input
The first line contains an integer, N.

The next line contains NN values, denoting V.


#### Standard output
Print the answer modulo 10^9 + 7 on the first line.

#### Constraints and notes
* 1 <= N <= 5 * 10^4
* 1 <= V(i) <= N for 1 <= i <= N 


[Source Link](https://csacademy.com/contest/archive/task/sortall/statement/)
