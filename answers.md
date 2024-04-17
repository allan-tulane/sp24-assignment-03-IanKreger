# CMPS 2200 Assignment 3
## Answers

**Name:**______Ian Kreger___________________


Place all written answers from `assignment-03.md` here for easier grading.

1a)
To make a greedy algorithim that would produce as many coins as possible that sum up to N the first step would be find the largest denomination that does not exceed N. This means that 2^K < N. Then subtract the value of the coin from N to get a new N and then repeat until N=0. You would put all of the coin values in a list and return that list of coins. 


1b)
The algorithim satisfies the greedy choice property by selecting the largest denomination that does not exceed the remaing amount at every step. Since the denominations are in powers of 2, this is very similar to binary form. In this case it is similar to the highest order of "1" in binary. This means that the algorithim removes the highest "1" which is the most optimal because we are removing the largest section of the problem. This means that each choice is locally and globally optimal. The optimal substructure property holds because once the problem is reduced, it is the same problem with just a smaller N. The problem is equivalent at each step, which makes each subproblem still optimal. This shows that each subproblem remains optimal along with the global solution.


1c)
Work is O(logn) and span is O(logn)


2a)
A counter example would be if the D = 1, 3, 4 and N = 9. The greedy algorithm would take a four dollar coin, then a three dollar coin, then two one dollar coins. This totals to four coins, but the optimal solution would be to use three three dollar coins. This would only result in three coins which is less than four proving the greedy algorithm does not get the fewest coins. 


2b)
The optimal substructure of this problem would be to find the minimum number of coins to get to N dollars. To do this all different combinations should be tested and the optimal substructure would be the fewest number of coins to get to N. 
By solving smaller subproblems and combining their solutions, we can find the optimal solution for the original problem. This process demonstrates the optimal substructure property of the problem.This approach ensures that we consider all possible combinations of denominations and select the one that requires the fewest number of coins to make change for N dollars, which ensures optimality.


2c)
If we use the top down approach the program would account for each substructure using recursion and no repititions. This means that the work would be O(kN) where K is the number of different denominations. The span would be O(N) because each subproblem is solved sequentially.


3b) I was unable to figure out the assertion error. Is there a way to fix this? I tried to play with the test but could not figure it out.