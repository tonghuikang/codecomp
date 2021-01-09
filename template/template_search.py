#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

def binary_search(function, left, right) -> int:
    # minimize k, s.t. condition(k) is True
    # https://leetcode.com/discuss/general-discussion/786126/
    while left < right:
        mid = (left + right) // 2
        if function(mid):
            right = mid
        else:
            left = mid + 1
    return left