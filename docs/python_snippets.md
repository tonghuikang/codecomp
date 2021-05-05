# Python snippets

[TOC]

These are some code snippets I freqently use in competitive programming.

I have pretty much memorised most of them already. I hope this snippets will help you getting up to speed.

## Without Library Imports

The following snippets do not require any import statements. The snippets are presented in descending order of frequency of usage.

##### List comprehension

Instead initialising another array and appending items to it, performing in one-line improves readability and brevity.

```python
lst = [x-1 for x in lst]
```

You can add if-else logic in the list comprehension.

```python
lst = [x-1 if x > 0 else 0 for x in lst]
```

You can apply a filter to the array as well.

```python
lst = [x-1 for x in lst if x > 0]
```



##### Copying a list or matrix

```python
arr = [1, 2, 3]
brr = arr
brr[1] = 9
arr  # [1, 9, 3], as arr is modified
```

- In the above example, `arr` and `brr` refer to the same object.
- Python does not store values in variables; it binds names to objects.

To 'clone' the list

```python
brr = [x for x in arr]
brr = list(arr)
brr = arr[:]
```

- [Stack Overflow](https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent)



To clone a matrix

```python
mrr = [row[:] for row in matrix]
mrr = [[cell for cell in row] for row in matrix]
```

- Useful when you need update a matrix while freezing the previous version of the matrix.
- [Stack Overflow](https://stackoverflow.com/questions/6532881/how-to-make-a-copy-of-a-2d-array-in-python)




##### Sorting a 2D list based on a certain index

```python
lst = sorted(list_of_lists,key=lambda e:e[1])
```

- [Stack Overflow](https://stackoverflow.com/questions/18563680/)



##### Enumerating an array

If you want both the index and element, you can use `enumerate` to make the code neater.

```python
A = [4,5,6,7]
for i,a in enumerate(arr[1:],start=10):
  print(i,a)
# [10,5], [11,6], [12,7]
```

- [Documentation](https://docs.python.org/3/library/functions.html#enumerate)




##### Enumerating an matrix

```python
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
for x,row in enumerate(matrix[1:-1], start=1):
  for y,cell in enumerate(row[1:-1], start=1):
	  for dx,dy in d4:
      matrix[x+dx][y+dy]  # do something with its neighbours
```



##### Moating a matrix

Given a 2D array, create a 'moat' of a certain value around the array.

```python
v = 0
matrix = [[v]*len(matrix[0])] + matrix + [[v]*len(matrix[0])]
matrix = [[v] + row + [v] for row in matrix]
```

- Without moats, we need to handle corner cases (for example check if `x+dx` and `y+dy` is within limits of the array)
- The code complexity is reduced.



##### Tranposing a matrix

```python
zip(*matrix)
```
- [Stack Overflow](https://stackoverflow.com/questions/10169919/python-matrix-transpose-and-zip)



##### Rotating a matrix

```python
matrix = [col[::-1] for col in zip(*matrix)]  # once
matrix = [col[::-1] for col in matrix][::-1]  # twice
matrix = [col for col in zip(*matrix)][::-1]  # thirce
```

- [Stack Overflow](https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python)



##### Flattening a list of list

```python
[cell for cell in row for row in matrix]
```

- [Stack Overflow](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)



##### Taking division and modulo at the same time

It is faster to access an array than to access the matrix. In some problems you might need such time optimisation.

This is how we would usually convert `x` and `y` indices of the matrix to `loc` index of the array flattened, and vice versa.

```python
loc = x*ncols + y
x, y = (loc // ncols, loc % ncols)
```

`divmod()` helps to make the code neater and twice faster

```python
loc = x*ncols + y
x, y = divmod(loc, ncols)
```

- [Documentation](https://docs.python.org/3/library/functions.html#divmod)



##### Sorting based on custom comparison

```python
from functools import cmp_to_key
  def compare(a,b):
    if a+b > b+a:
        return -1
    if a+b < b+a:
        return 1
    return 0
nums = sorted(nums, key=cmp_to_key(compare))
```



## Python Standard Library

The [Python Standard Library](https://docs.python.org/3.6/library/) consist of packages that installed together with Python, and is available in all competitive programming platforms. Again, these snippets presented are in decreasing freqeuncy of my usage.



##### Making a freqency dictionary

```python
from collections import Counter
c = Counter(lst)
```

- [Stack Overflow](https://stackoverflow.com/questions/722697/)



##### Building a graph

```python
from collections import defaultdict
def build_graph(edges, bidirectional=False, costs=None):
    g = defaultdict(list)
    if costs:
        for (a,b),c in zip(edges, costs):
            g[a].append((b,c))
            if bidirectional:
                g[b].append((a,c))
    else:
        for a,b in edges:
            g[a].append(b)
            if bidirectional:
                g[b].append(c)
    return g
```

- Without the library and using only `dict()`, we will need to check the whether the key is present in the dictionary. If the key is present we modify its value, otherwise we need to initialise the key value pair.
- `defaultdict` defines a default object type and value



##### Python priority queue

```python
import heapq as hq
hq.heapify(lst)
hq.heappush(lst, item)
hq.heappop(lst)
```

- The smallest element is always at `lst[0]`
- Transforming an array into a heap takes linear time $n$.
- Adding an element to the array takes $log(n)$ time. 
- Removing the smallest element from the array takes $log(n)$ time.
- [Visualisation](https://www.cs.usfca.edu/~galles/visualization/Heap.html) and [documentation](https://docs.python.org/3/library/heapq.html)



##### Python deque

If you want a list that can be popped efficiently from either side.

```python
from collections import deque
q = deque([])

q.append(v)
v = q.pop()

q.appendleft(v)
v = q.popleft()
```

- [Documentation](https://docs.python.org/3/library/collections.html#collections.deque)



##### Binary search on an array

Given a sorted array and a value, find where the value will fit into the sorted array.

```python
import bisect
bisect.bisect_left(arr, x)
# array:    [1,1,1,3,3,3,3,3,4,4]
# indexes:   0 1 2 3 4 5 6 7 8 9
# x=2:             ^bisect_left = bisect_right
# x=0:       ^bisect_left = bisect_right
# x=3:  bisect_left^         ^bisect_right
```

- The difference between `bisect_left` and `bisect_right` is  
- [Documentation](https://docs.python.org/3/library/bisect.html)



##### Binary search on a function

```python
# TBC
```

- [Writeup on LeetCode](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)



**Memoization**

To memoize (i.e. take a memo) is to record values that were previously calculated so your do not need spend time to calculate them again. However, space is required to record the values.

```python
import functools

@functools.lru_cache(maxsize=None)
def something
```

- You could use `@functools.cache` if python 3.9 is available (not true for all competitive programming platforms for now).
- [Documentation](https://docs.python.org/3/library/functools.html#functools.lru_cache)



##### Zip Longest

In default `zip` function, the iterator ends when the shortest element is finished. Instead of padding one of the arrays, you can use this. 

```python
itertools.zip_longest(arr, brr, fillvalue=0)
```

- [Documentation](https://docs.python.org/3/library/itertools.html#itertools.zip_longest)



## Other libraries

##### scipy.optimize

Tool to minimise convex functions

https://docs.scipy.org/doc/scipy/reference/optimize.html

```python
import numpy as np
from scipy.optimize import minimize

class Solution:
    def getMinDistSum(self, positions):
        
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



# Common mistakes

When I was learning Python in Year 1

- https://github.com/tonghuikang/digital-world/blob/master/digital_world_error_log.ipynb

On global variables

- https://support.leetcode.com/hc/en-us/articles/360011834174
- https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
- https://web.archive.org/web/20200221224620/http://effbot.org/zone/default-values.htm