# Dynamic programming

What is dynamic programming?

- In a few words - does the past matter?
- In a statement - breaking a big problem down into subproblems until the big problem can be solved



Errichto has a [short](https://www.youtube.com/watch?v=YBSt1jYwVfU) [video](https://www.youtube.com/watch?v=1mtvm2ubHCY) [series](https://www.youtube.com/watch?v=pwpOC1dph6U) on dynamic programming. The following summaries the concepts from his videos.



Objectives that could use dynamic programming

- Find out **whether is it possible** to achieve a task
- **Count the number of ways** to achieve a task
- The **minimum or maximum value** of achieving a task
- **Produce a way** (with the minimum or maximum value)

(Some solutions can be reused for other objectives, so we try to prepare code that addresses more objectives without additional costs).



### Iteration versus recursion

Take the example of the `n`-th Fibonacci number

Iterative solution

```python
def fib(n):
  arr = [0]*n
  arr[0], arr[1] = 1
  for i in range(2,n):
    arr[i] = arr[i-1]
  return arr[n]
```

Recurisve solution

```python
from functools import lru_cache

@lru_cache(maxsize=n+1)
def fib(n):
  if n == 0 or n == 1:
    return 0 
  return fib(n-1) + fib(n-2)
```







Approaches

- Greedy approach
- Iterative
- Recursive



Questions to ask yourself



States and values.



What is dynamic programming? I still don't know. I try to summarise here.

Is max sliding window (max subarray?) considered DP?





