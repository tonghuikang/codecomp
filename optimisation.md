# Optimisation problems

This is a set of problems. Hopefully I could write a solver that solves these problems.



General problems is presented.



Please include 

Max-flow https://github.com/Errichto/contest_library/blob/master/dinic.cpp



**Convex optimisation**

(Ternary search?)

```python
import numpy as np
from scipy.optimize import minimize

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def loss_function(z):
            loss = 0
            for a, b in positions:
                loss += ((z[0] - a)**2 + 
                         (z[1] - b)**2)**0.5
            return loss
        
        res = minimize(loss_function, [0,0])
        print(res)
        return res.fun
```





##### Knapsack

There are 0–1 knapsack, bounded knapsack, and unbounded knapsack. These are actually linear/integer/mixed programming problems. 

**Binary** Knapsack problem. For every item you may or may not take, and you need to fulfil the max limit.

```python
from functools import lru_cache

def knapsack(items, maxweight):
    # items is an array of (value, weight)
    @lru_cache(maxsize=None)
    def bestvalue(i, j):
        # Return the value of the most valuable 
        # subsequence of the first i elements in 
        # items whose weights sum to no more than j.
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        value, weight, idx = items[i - 1]
        return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in reversed(range(len(items))):
        if bestvalue(i + 1, j) != bestvalue(i, j):
            result.append(items[i])
            j -= items[i][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result

arr = [(a,b,c) for a,b,c in zip([16,22,12,8,11,19],
                                [5,7,4,3,4,6],
                                range(6))]
knapsack(arr, 15)
```



**Integer** Knapsack problem
https://rosettacode.org/wiki/Knapsack_problem/Bounded#Python

You no longer build by number of items selected, you iterate from the first possible item?



**Mixed linear programming**

Use Google-OR tools for this. It seems to be a very complicated problem.



**Exact knapsack problem**

```python
def knapsack(items, maxweight):  # exact weight
    # items is an array of (value, weight)
    @lru_cache(maxsize=None)
    def bestvalue(i, j):
        # Return the value of the most valuable 
        # subsequence of the first i elements in 
        # items whose weights sum to no more than j.
        if j < 0:
            return float('-inf')
        if j == 0:
            return 0
        if i == 0:
            return float('-inf')  ## modification
        value, weight, idx = items[i - 1]
        return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in reversed(range(len(items))):
        if bestvalue(i + 1, j) != bestvalue(i, j):
            result.append(items[i])
            j -= items[i][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result
```



**scipy.optimize**

https://docs.scipy.org/doc/scipy/reference/optimize.html

```python
import numpy as np
from scipy.optimize import minimize

class Solution:
    def getMinDistSum(self, 
                      positions: List[List[int]]) -> float:
        def loss_function(z):
            loss = 0
            for a, b in positions:
                loss += ((z[0] - a)**2 + 
                         (z[1] - b)**2)**0.5
            return loss
        
        res = minimize(loss_function, [0,0])
        print(res)
        return res.fun
```



