## Which integer is closer to “hello”? 6 Question G:

## 6.1 Description

In this problem we will try to give a satisfactory answer to the question: “Which integer is closer
to a predefined string?”. To be able to answer this question, we will have to develop a custom
“String-Integer distance metric measure”. In order to accomplish this, we will “stand on the
shoulders of giants and try to see a little further... .” (Original quotation: “If I have seen further
it is by standing on the shoulders of giants” Isaac Newton).
According to the number theory, each positive integer number can be written as a sum of
other positive integers. This is known as the “Integer Partitioning” problem and has been stud-
ied by the best mathematical minds of all times, including the Indian genius S. Ramanujan
(1887-1920). Generally, in the integer partitioning problem, two sums that differ only in the or-
der of their summands are considered to be the same partition. Nevertheless, if the order of the
summands matters then the sum becomes a composition. For example, although integer 4 has
5 distinct partitions (i.e. 4: 4, 3+1, 2+2, 2+1+1, 1+1+1+1), there exist 8 compositions which can
be presented either in lexicographical or anti-lexicographical order, as presented below:


Now consider that the numbers 1-9 can be used to correspond to a set of letters as depicted
at the following table:

It now becomes clear that by replacing each summand of every composition with a letter
from the set it corresponds to, we are able to form words! For example, using the 7th composi-
tion in anti-lexicographical order of the integer 4 (i.e. the composition 1 + 1 + 2), we may form
the word “bad” (1→b, 1→a, 2→d).
Since we have found a way to create words from integers, we only need a string similarity
measure in order to decide upon the “resemblance” of the word we have formed when com-
pared to a predefined string. Towards this direction we may employ the Dice’s coefficient met-
ric. According to the Dice coefficient, the similarity between two strings can be computed
based on their number of matching bigrams. If the words under consideration share exactly
the same bigrams, then the Dice coefficient for these strings would be equal to 1.0, whilst if they
do not have any bigrams in common, the coefficient association would be equal to zero. The
mathematical formula expressing the computation of the Dice coefficient between two words
is shown at Eq. (1):

where bigrams is the function which reduces a word to a multi-set of character bigrams.
Consider for example the English words “transformation”, yielding the bigrams tr, ra, an,
ns, sf, fo, or, rm, ma, at, ti, io, on and “transportation” yielding the bigrams tr, ra, an, ns, sp,
po, or, rt, ta, at, ti, io, on. The matching bigrams between these two strings are tr, ra, an, ns,


or, at, ti, io, on. It is obvious that the set of bigrams corresponding to each word consists of
13 elements, whereas only 9 of them are shared by both strings. Therefore the overall Dice
coefficient association value would be 18/26≈0.692.
Based on the above, can you now develop a program that would be able to answer the ques-
tion: “Which integer is closer to a predefined string?”

## 6.2 Task

Please write a program that would examine and write to the standard output stream the in-
teger(s) between 1 and 10 which are “closer” to a predefined string that will be given to your
program as input in run time. More specifically:
For each integer i, 1≤i≤10, your program should be able to compute all the compositions
in anti-lexicographical order of each integer i.
a. For each derived composition, all the possible strings that can be formed using the [num-
ber – character set] correspondence presented at Table 2 should be computed.
i. For each string formed from the previous step, your program should calculate the Dice
coefficient value between the formed string and the predefined string that has been given to
your program as input in run time.
After all the aforementioned computations have been completed, your program should
print to the standard output stream the integer(s) between 1 and 10 which are “closer” to the
predefined string, according to the following format:
The integers closer to the word: [predefined input word] are the following: Integer:[integer]
(Word:[formed word] Dice Coeff.Value:[Dice value] from Composition:[composition])

## 6.3 Input

The program gets its input in the form of typical arguments in run time. It should accept only
one argument that should be of type string, and it will represent the predefined word used by
your program in order to compute the integers between 1 and 10 that are closer to this input
word.

## 6.4 Output

Your program should print to the standard output stream the integer(s) between 1 and 10 which
are “closer” to the word that has been given as input to your program, according to the following
format:
The integers closer to the word: [predefined input word] are the following: Integer:[integer]
(Word:[formed word] Dice Coeff.Value:[Dice value] from Composition:[composition]) Please
note that with regards to the Dice coefficient association value, in the output it should be rounded
and outputted using only the first 3 digits of accuracy. (e.g. if the Dice’s value is equal to 0.4 it
should be printed as 0.400. Equivalently, if it is equal to 0,6666666666 it should be outputted as
0,667).
Note: There is no new line character at the end of the result.


## 6.5 Sample Input

hello

## 6.6 Sample Output

The integers closer to the word: hello are the following: Integer:9 (Word:hel Dice Coeff.Value:0.667
from Composition:[3, 2, 4]) Integer:10 (Word:ell Dice Coeff.Value:0.667 from Composition:[2, 4,
4])