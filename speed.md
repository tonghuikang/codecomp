# Speed optimisation

Is there really a case where the code passes on C++ but not Python?

Yes.

When you are nesting for loops but intend to run on O(n), avoid enumerate for the inner loop.

Replacing 

```python
          for z,x in enumerate(lst[i+1:], start=i+1):
```

with

```python
          for z in range(i+1, n_months+1):
```

would have made my code run within time limit. I am still trying to find a reproducible example.





# Fast reading

To read the remaining lines quickly

```python
import sys
input = sys.stdin.readline  # to read input quickly
```



https://codeforces.com/blog/entry/82989 On fast reading



# Use of numba

This is only tested in Python 3.8.2 in AtCoder



Please refer to a [past question](https://atcoder.jp/contests/abc175/submissions?f.Task=abc175_e&f.Language=4006&f.Status=AC) for examples.


My implementation

- import statements

```
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
```

- function decorator
```
@njit((i8[:], i8, i8, i8), cache=True)
def solve(items,R,C,K):  # fix inputs here
	# use
	return something
```

- ensure input format is consistent

```python
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
H, W, K = map(int, readline().split())
XYV = np.array(read().split(), np.int64)
 
print(solve(XYV, H, W, K))
```

Vectorised operations are now allowed (with numpy arrays), but not necessary for optimisation.





