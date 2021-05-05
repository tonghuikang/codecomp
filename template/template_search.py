#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------


# -------------------------- binary search template --------------------------

def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    while left < right:
        mid = (left + right) // 2
        if func(mid):
            right = mid
        else:
            left = mid + 1
    if first:  # find first True
        return left
    else:      # find last False
        return left-1
    

# -------------------------- ternay search template --------------------------


def binary_search(func_,          # condition function
                  maximize=True,  # else minimise
                  left=0, right=2**31):
    raise NotImplementedError

