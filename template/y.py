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
lst = list(map(int,input().split()))

res = 0
for i,x in enumerate(lst, start=1):
    if x%2 == 1 and i%2 == 1:
        res += 1

print(res)
