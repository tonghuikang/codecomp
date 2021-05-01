#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


# Python program to remove
# all adjacent duplicates from a string
 
# Recursively removes adjacent
# duplicates from str and returns
# new string. las_removed is a
# pointer to last_removed character
def removeUtil(string, last_removed):
 
    # If length of string is 1 or 0
    if len(string) == 0 or len(string) == 1:
        return string
 
    # Remove leftmost same characters
    # and recur for remaining
    # string
    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]
 
        return removeUtil(string, last_removed)
 
    # At this point, the first
    # character is definiotely different
    # from its adjacent. Ignore first
    # character and recursively
    # remove characters from remaining string
    rem_str = removeUtil(string[1:], last_removed)
 
    # Check if the first character
    # of the rem_string matches
    # with the first character of
    # the original string
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return (rem_str[1:])
 
    # If remaining string becomes
    # empty and last removed character
    # is same as first character of
    # original string. This is needed
    # for a string like "acbbcddc"
    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str
 
    # If the two first characters of
    # str and rem_str don't match,
    # append first character of str
    # before the first character of
    # rem_str.
    return ([string[0]] + rem_str)
 
def toString(x):
    return ''.join(x)

# Utility functions
def toList(string):
    return list(string)

def remove(string):
    last_removed = 0
    return toString(removeUtil(toList(string),
                                    last_removed))


def solve_(srr):
    # your solution here
    
    flag = True
    res = deque([])


    for i,x in enumerate(srr):
        if x == "R":
            flag = not flag
        else:
            if flag:
                res.append(x)
            if not flag:
                res.appendleft(x)

    res = list(res)
    if not flag:
        res = res[::-1]

    res = remove(res)
    return "".join(res)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(srr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)