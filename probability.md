# Probability



Caculate probability from a binomial distribution (Kickstart 2020 Round B Question 4)



### Combinatorics

If you are using python 3.8

```python
import math
math.comb()
```

If scipy is allowed

```python
from scipy.special import comb
comb()
```

Otherwise (not the best)

```python
def choose(n, k):
    if k == 0:
        return 1
    return n * choose(n-1, k-1) // k
```

ncr mod p

```python
# Python3 functpion to 
# calculate nCr % p
@functools.lru_cache(maxsize=None)
def choose(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p
```



