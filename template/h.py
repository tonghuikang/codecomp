#!/usr/bin/env python3
## For the attempt to be the first to solve the easiest AtCoder questions

import heapq as hq
import math, random
import functools, itertools, collections
from collections import Counter, defaultdict, deque

# read line as an integer
# k = int(input())

# read line as a string
# srr = input()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
v,t,s,d = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# print(v*t, d, v*s)

# include logic here
if v*t <= d <= v*s:
    print("No")
else:
    print("Yes")
