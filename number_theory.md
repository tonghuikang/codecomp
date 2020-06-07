# Number theory

You need some basic number theory, and accompanying code.



Please translate from 

https://github.com/Errichto/contest_library/blob/master/number_theory.cpp

https://github.com/Errichto/contest_library/blob/master/fft.cpp (just use Numpy, but also provide real number calculation as well)

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
import math

def prime_factors(nr):
    i = 2
    factors = []
    while i <= nr:
      	if i > math.sqrt(nr):
            i = nr
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors
```



Geometric progression



Modular inverse

```python
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

```



Modular exponentiation

Python has an inbuilt function that does this

```python
pow(base, exponent, modulo)
```





Arithmetirc progression

