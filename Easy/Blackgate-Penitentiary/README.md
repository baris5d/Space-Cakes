# Blackgate Penitentiary
* Time limit: 1000 ms
* Memory limit: 256 MB

Vangelis the Batbear trapped all the members of Joker's Streetgang in a basement.

Your job as a police officer is to transport all gang members to Blackgate Penitentiary.

To facilitate the transport, you should form a row such that the heights of the gang members are in non-decreasing order. For each gang member you should find the minimum and the maximum position where they can be in a valid sorted row and produce a roster with this information.
<br><br>
**Standard input**<br><br>
Input will start with a line that contains only one integer nnn, the number of crew members that were arrested. On each of the following nnn lines there will be a single word sss and an integer hhh separated by a space character, where sss is the name and hhh is the height of the crew member.
<br><br>**Standard output**<br>

On the output, there will be ggg lines. Each line will contain in alphabetical order and space separated the names of the crew members that have the same height, followed by the minimum and the maximum position where any member of the specific group can be placed. The groups should be printed in increasing order of their members' heights.
<br><br>
**Constraints and notes**<br>
```
    1≤n≤10001
    1≤length(si)≤101
    120≤hi≤250120
    Names are only composed of characters of the Latin alphabet. 
```
**Input 1**	
```
6
TheJoker 180
HarleyQuin 160
MrHammer 220
Boody 220
Muggs 180
Paulie 180
```
**Output 1**	
```
HarleyQuin 1 1
Muggs Paulie TheJoker 2 4
Boody MrHammer 5 6
```

**Input 2 **
```
10
a 200
aa 200
ab 200
aba 200
aaa 200
b 200
A 200
Aa 200
AB 200
B 200
```	

**Output 1"**	
```
A AB Aa B a aa aaa ab aba b 1 10
```

[Source Link](https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/)
