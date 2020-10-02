# Partial-Sum (Troll-Coder)
You have found a huge treasure on an island, but the only access point to that island is a bridge guarded by a giant Troll! In order to cross the bridge, you have to guess a sequence of NN bits by submitting queries. For each query, the Troll will tell you how many bits you guesses correctly until you guess the correct sequence.


## Interaction
Your program must exchange information with the Troll by submitting queries and reading answers.


Note that you must flush the buffer so that the output reaches the Troll. Here we ilustrate it for several languages.


At the beginning of each test case, the Troll will give you a single integer N which will represent the length of the sequence. 


To submit a query, your program should output the letter Q followed by a space and by a binary sequence of length N with each bit separated by a space. After each query you will receive an integer denoting the number of correct bits. The last submission will be your final answer and it should start with an A followed by a space and by a binary sequence of length N with each bit separated by a space.


## Constraints and notes
1 ≤ N ≤ 100 


Your program can submit at most N + 1 queries before arriving at the correct answer. 


Time Limit : 1000ms


Memory Limit : 256 MB