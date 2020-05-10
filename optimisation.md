# Optimisation problems

This is a set of problems. Hopefully I could write a solver that solves these problems.



General problems is presented.



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

This one you need to use a library. It seems to be a very complicated problem.



**Integer factorisation (brute force)**

Just in case you need it.

```python
def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors
```



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



