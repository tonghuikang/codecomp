# Use of numba on AtCoder

AtCoder is more experimental with their platform and allows other popular Python packages.

Libraries `numba` and `numpy` allows faster computations in Python by specifying the data types in the array. This is only tested in Python 3.8.2 in AtCoder

(Why won't `numpy` alone suffice?)

Please refer to a [past question](https://atcoder.jp/contests/abc175/submissions?f.Task=abc175_e&f.Language=4006&f.Status=AC) for examples.


My implementation

- import statements

```python
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
```

- function decorator
```python
@njit((i8[:], i8, i8, i8), cache=True)
def solve(items,R,C,K):  # fix inputs here
	# your logic here
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
