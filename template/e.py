import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7

def ncr(n,k):
    if n < 0:
        return 0
    if k < 0:
        return 0
    if n < k:
        return 0
    return choose(n,k)

@functools.lru_cache(maxsize=None)
def choose(n, k):    
    if k == 0:
        return 1
    return (n * choose(n-1, k-1) // k)%M9

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(lst, m, k):  # m elements, k diff
    if m == 1:
        return len(lst)
    
    c = Counter(lst)
    crr = [(k,v) for k,v in sorted(c.items())]
    # log(crr)

    right_ptr = 0
    
    res = 0
    cursum = 0
    for x,cnt in crr:
        while right_ptr < len(crr) and crr[right_ptr][0] - k <= x:
            cursum += crr[right_ptr][1]
            right_ptr += 1
        # log(right_ptr, cursum)

        for a in range(1,cnt+1):
            # log(cnt, a, cursum-cnt, m-a)
            res += ncr(cnt, a) * ncr(cursum-cnt, m-a)
        # a = right_ptr - i - 2
        # b = m-2
        # log(a,b)
        # res += choose(a, b)

        cursum -= cnt

    return res%M9


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
    # k = int(input())
    
    # read one line and parse each word as an integer
    arr = list(map(int,input().split()))

    if len(arr) == 1:
        M9 = 10**16
        arr = [arr[0], 3, 2]
    lst = list(map(int,input().split()))
    lst.sort()

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(lst, arr[1], arr[2])  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list