# Number theory

You need some basic number theory, and accompanying code.

Prime factorisation - there is a unique way to factorise an integer into number factors.



To find all divisors

```python
from functools import reduce

def all_divisors(n):    
    return set(reduce(list.__add__, 
    ([i, n//i] for i in 
    range(1, int(n**0.5) + 1) if n % i == 0)))
```



To obtain prime factorisation

```python
def prime_factors(nr):
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



Geometric progression



Arithmetirc progression

