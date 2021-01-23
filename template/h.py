#!/usr/bin/env python3
## For the attempt to be the first to solve the easiest AtCoder questions

import heapq as hq
import math, random
import functools, itertools, collections
from collections import Counter, defaultdict, deque

# read line as an integer
# k = int(input())

# read line as a string
srr = input()
srr = list(srr)

if len(set(srr)) == 1:
    print("Won")
else:
    print("Lost")

