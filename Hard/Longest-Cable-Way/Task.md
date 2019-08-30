
## Longest Cable Way

Historically, all cableways have been less than 100 kilometers in length and cable car speeds
have not crossed 50 kmph. However, the discovery a new ore material, available directly in the
form of long rods, in the Grand Canyon, led to the ability to create very high speed cable ways
that can extend to thousands of kilometers. The US army decided to connect most of their air
bases and navy bases using long-distance cable ways. However, there were a few constraints.

1. The cables were in the form of long and flexible rods with smooth edges that can be joined
    together using a very expensive but specialized grafting process. However, cutting the
    cables was not possible as it was not possible to retain the smoothness of the edges that
    is required to graft them.
2. The join process was not only very expensive but also inefficient as the speeds of the cable
    cars were affected by the joints and reduced by nearly 5% for every joint. Hence, there was
    a need to minimize the number of joints.
3. The cables, being naturally available rods of varying lengths, were available in specific
    sizes and there was limited inventory that was available.
4. The cable way should be connected using cable that is the exact length of the distance
    between the two locations (no higher and no lesser).

## 3.1 Task

Now your task is to help the engineer select the optimal combination of cables from the inven-
tory to build the exact requested length of cable way such that the number of joints is mini-
mized. Write a program to achieve the same. Your program must output only the minimum
number of joints possible.


## 3.2 Time Limit

Maximum five seconds for any combination of inventory and up to 5000 kilometers of cable
way.

## 3.3 Input

The first line of the input D is the distance between the two air bases to be connected in kilo-
meters. (0 < D < 5000)
Each subsequent line contains a pair of numbers Li Ni, indicating the length of the cable in
kilometers and the quantity available in the inventory. (0< _i_ <=20, 1<= _Li_ <=200, 1<= _N i_ <=
100)
The input is terminated by 0 0.

## 3.4 Output

1. The output should contain a single integer J representing the minimum number of joints
    possible to build the requested length of the cable way
2. If no solution is possible the program should print “No solution possible” in the output.

## 3.5 Note

There is no new line character at the end of the result. There may be multiple solutions for the
same number of minimum joints.
It is sufficient to identify the number of joints and not the actual list of rods to be used.
Example: (see below for input formats)
Solutions for making 444 with 10 joints are
2 ∗ 2 + 50 ∗ 7 + 45 ∗ 2 =11 rods of cables i.e., 10 Joints
16 ∗ 1 + 3 ∗ 1 + 30 ∗ 1 + 50 ∗ 7 + 45 ∗ 1 =11 rods of cables i.e., 10 Joints
However the following has 11 joints and hence not a solution
3 ∗ 2 + 30 ∗ 1 + 50 ∗ 8 + 8 ∗ 1 =12 rods of cables i.e., 11 Joints

## 3.6 Sample Input - Scenario

444

16 2

3 2

2 2

30 3

50 10

45 12

8 12

0 0


## 3.7 Sample Output - Scenario

### 10

## 3.8 Sample Input - Scenario

## Longest Cable Way

Historically, all cableways have been less than 100 kilometers in length and cable car speeds
have not crossed 50 kmph. However, the discovery a new ore material, available directly in the
form of long rods, in the Grand Canyon, led to the ability to create very high speed cable ways
that can extend to thousands of kilometers. The US army decided to connect most of their air
bases and navy bases using long-distance cable ways. However, there were a few constraints.

1. The cables were in the form of long and flexible rods with smooth edges that can be joined
    together using a very expensive but specialized grafting process. However, cutting the
    cables was not possible as it was not possible to retain the smoothness of the edges that
    is required to graft them.
2. The join process was not only very expensive but also inefficient as the speeds of the cable
    cars were affected by the joints and reduced by nearly 5% for every joint. Hence, there was
    a need to minimize the number of joints.
3. The cables, being naturally available rods of varying lengths, were available in specific
    sizes and there was limited inventory that was available.
4. The cable way should be connected using cable that is the exact length of the distance
    between the two locations (no higher and no lesser).

## 3.1 Task

Now your task is to help the engineer select the optimal combination of cables from the inven-
tory to build the exact requested length of cable way such that the number of joints is mini-
mized. Write a program to achieve the same. Your program must output only the minimum
number of joints possible.


## 3.2 Time Limit

Maximum five seconds for any combination of inventory and up to 5000 kilometers of cable
way.

## 3.3 Input

The first line of the input D is the distance between the two air bases to be connected in kilo-
meters. (0 < D < 5000)
Each subsequent line contains a pair of numbers Li Ni, indicating the length of the cable in
kilometers and the quantity available in the inventory. (0< _i_ <=20, 1<= _Li_ <=200, 1<= _N i_ <=
100)
The input is terminated by 0 0.

## 3.4 Output

1. The output should contain a single integer J representing the minimum number of joints
    possible to build the requested length of the cable way
2. If no solution is possible the program should print “No solution possible” in the output.

## 3.5 Note

There is no new line character at the end of the result. There may be multiple solutions for the
same number of minimum joints.
It is sufficient to identify the number of joints and not the actual list of rods to be used.
Example: (see below for input formats)
Solutions for making 444 with 10 joints are
2 ∗ 2 + 50 ∗ 7 + 45 ∗ 2 =11 rods of cables i.e., 10 Joints
16 ∗ 1 + 3 ∗ 1 + 30 ∗ 1 + 50 ∗ 7 + 45 ∗ 1 =11 rods of cables i.e., 10 Joints
However the following has 11 joints and hence not a solution
3 ∗ 2 + 30 ∗ 1 + 50 ∗ 8 + 8 ∗ 1 =12 rods of cables i.e., 11 Joints

## 3.6 Sample Input - Scenario

444

16 2

3 2

2 2

30 3

50 10

45 12

8 12

0 0


## 3.7 Sample Output - Scenario

10

## 3.8 Sample Input - Scenario

44

30 31

50 10

45 12

90 21

43 1

0 0

## 3.9 Sample Output - Scenario

No solution possible

## 3.9 Sample Output - Scenario

No solution possible
