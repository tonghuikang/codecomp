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
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION

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


def find_peak(func_, minimize=False, left=0, right=2**31-1):
    # https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/
    # find the peak value of a function, assumes that the ends are not peaks

    def func(val):
        # negative the value of func_ if we are minimizing
        if minimize:
            return -func_(val)
        return func_(val)
        
    while left < right:
        mid = (left + right) // 2
        if func(mid) < func(mid + 1):
            left = mid + 1
        else:
            right = mid

    return left

