# Leetcode Python Reference

[TOC]

Please study or include

- factorisation algorithm, and divisor counting
- knapsack of all variants
- the constraint programming solver code (use scipy for integer programming)
- binary search implementation



## Common Code snippets

These are some code snippets I freqently use in Leetcode, in descending order. I place them here so that I do not need to use the search engine everytime I want it.

##### Sorting a 2D list based on a certain index
https://stackoverflow.com/questions/18563680/ <br>

```python
lst = sorted(lst,key=lambda e:e[1])
```

##### Eumerate an array

```python
A = [4,5,6]
for i,a in enumerate(A,start=10):
  print(i,a)
  # [10,4] [11,5], [12,6]
```


##### Tranpose an array

```python
zip(*theArray)
```

##### Rotate an array

```python
rotated = [list(reversed(col)) for col in zip(*matrix)]
```

How about rotating it in another direction?

##### Flatten a list of list

```python
sum(arr, [])
```

##### Zip longest

In default, Python zip only interate until the shortest

```
itertools.zip_longest()
```

##### String range

```python
def srange(a, b):
    yield from (chr(i) for i in range(ord(a), ord(b)+1))
```

##### Making a freqency dictionary

https://stackoverflow.com/questions/722697/ <br>

```python
from collections import defaultdict
fq = defaultdict(int)
for w in words:
    fq[w] += 1
```

```python
from collections import Counter
fq = Counter(lst)
```

##### Python deque

If you want a list that can be popped efficiently from either side.

```python
from collections import deque
```

##### Deleting the first element is quite fast as well.

```python
lst = range(10000)
del lst[0]
```

##### Python heapq

https://www.cs.usfca.edu/~galles/visualization/Heap.html

The interesting property of a heap is that its smallest element is always the root, heap[0].

```python
import heapq
heapq.heapify(lst)
heapq.heappush(heap, item)
heapq.heappop(heap)
```

- Transforming an array into a heap takes linear time $n$.
- Adding a element to the array takes $log(n)$ time. 
- Removing the smallest element from the array takes $log(n)$ time.

##### Search an array efficiently in Python

Does binary search for you.

https://docs.python.org/3/library/bisect.html

```python
# examples?
```



Lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def something
```



##### List comprehension with if/else

The element is included in the array only if condition if fulfilled

```python
lst = [(i - 12*((i//12)-1)) for i in lst if i>25]
```

If you want another element to be included in the array.

```python
lst = [(i - 12*((i//12)-1)) if i>25 else i for i in lst]
```

##### Using maxint 
Because you are cool

```python
import sys
MAX = sys.maxint
```

##### Reduce excess whitespace

Replace multiple whitespace with one whitespace.

```python
' '.join(mystring.split())
```


