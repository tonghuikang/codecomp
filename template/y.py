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
# k = int(input())

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
a,b,c,d = list(map(int,input().split()))

if a <= 0 <= b:
    xx = [a,0,b] 
else:
    xx = [a,b]

if c <= 0 <= d:
    yy = [c,0,d]
else:
    yy = [c,d]

maxres = -10**18
for x in xx:
    for y in yy:
        maxres = max(maxres, x*y)

print(maxres)
