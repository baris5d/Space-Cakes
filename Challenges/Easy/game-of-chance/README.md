# Game of Chance
* Time limit: 1280 ms
* Memory limit: 256 MB

Alex and Ben are investors in the stock market. Initially Alex has **A** dollars and Ben has **B** dollars. Every second each of the two either *wins* or *loses* **1** dollar. Decide who has more money after **N** seconds.

#### Standard input
The first line contains three integers **N**, **A** and **B**.

The second line contains **N** integers representing the *wins* and *losses* of Alex. The integers are either **1**, in case of *win*, or **−1**, in case of a *loss*.

The third line contains **N** integers representing the *wins* and *losses* of Ben. The integers are either **1**, in case of win, or **−1**, in case of a *loss*.

#### Standard output
If Alex has more money in the end print **1**. If Ben has more money print **2**. If they have the same amount print **0**.

#### Constraints and notes
* 0 ≤ ***A***, ***B*** ≤ 1000
* 1 ≤ ***N*** ≤ 1000
* It is guaranteed neither of them will ever have a negative amount of money

| Input | Output |
| :- | :- |
| `5 3 2`<br/>`1 -1 1 1 -1`<br/>`-1 1 -1 -1 -1`| `1`<br/><br/><br/> |
| `4 1 3`<br/>`1 1 -1 -1`<br/>`1 -1 -1 -1`| `0`<br/><br/><br/> |

[Source Link](https://csacademy.com/contest/archive/task/game-of-chance/)
