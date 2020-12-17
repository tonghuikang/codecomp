import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(lst):
    # your solution here

    # arr = sorted(lst)
    # diff = sum(abs(x - 1) for x in lst)

    # for x in arr:
    #     diff += 


    s = sum(lst)


    mean = s//len(lst)
    mark = mean//2

    arr = [1 if x < mark else mean for x in lst]
    diff = sum(abs(x - a) for x,a in zip(lst, arr))
    log(arr)
    log(mean, diff, s)

    if diff*2 <= s:
        return arr
    

    mean = s//len(lst)
    mark = mean//2

    arr = [2**(len(bin(x))-3) for x in lst]
    diff = sum(abs(x - a) for x,a in zip(lst, arr))
    log(arr)
    log(mean, diff, s)

    if diff*2 <= s:
        return arr


    mean = max(lst)
    mark = mean//2

    arr = [1 if x < mark else mean for x in lst]
    diff = sum(abs(x - a) for x,a in zip(lst, arr))
    log(arr)
    log(mean, diff, s)

    if diff*2 <= s:
        return arr
    

    mean = int(3/2*s/len(lst))
    mark = mean//2

    arr = [1 if x < mark else mean for x in lst]
    diff = sum(abs(x - a) for x,a in zip(lst, arr))
    log(arr)
    log(mean, diff, s, "x")

    if diff*2 <= s:
        return arr


    # mean = sum(lst)

    # arr = [mean for x in lst]

    # mean = mean + 1

    # arr = [1 if x < mark else mean for x in lst]
    # diff = sum(abs(mean - a) for a in lst)

    # if diff*2 <= s:
    #     return arr
    
    return 0


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

# for case_num in [1]:  # no loop over test case
for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(lst)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    print(*res)  # if printing a list