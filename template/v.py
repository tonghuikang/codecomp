## for use in beginner level questions where speed is key
## and also for single test case code
## mastercopy for x,y,z

import sys
import heapq, functools, collections
import random
from collections import Counter, defaultdict

# read line as a string
# strr = input()

# read line as an integer
k = int(input())

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# arr = list(map(int,input().split()))

import operator as op
from functools import reduce

def ncr(n, r, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  p - 2, p)) % p 

if k <= 2:
    print(0)
    sys.exit()

if k == 3:
    print(1)
    sys.exit()

partitions = 1
res = 0
MOD = 10**9 + 7

while partitions*3 <= k:
    intervals = k - partitions*2
    val = ncr(intervals-1, partitions-1, MOD)
    # print(intervals-1, partitions-1, partitions, val)
    res += val
    partitions = partitions + 1

print(res%MOD)