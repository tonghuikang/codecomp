## for use in beginner level questions where speed is key
## and also for single test case code
## mastercopy for x,y,z

import sys
import heapq, functools, collections
import random
from collections import Counter, defaultdict

# read line as a string
strr = input()

# read line as an integer
# k = int(input())

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# arr = list(map(int,input().split()))

if "RRR" in strr:
    print(3)
elif "RR" in strr:
    print(2)
elif "R" in strr:
    print(1)
else:
    print(0)
