#!/usr/bin/env python3
import sys
import collections
from collections import defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr, n):
    assert n == len(arr)
    # your solution here
    # sliding window, calculate contribution

    # arr.append(0)
    psum = defaultdict(collections.deque)

    prevsum = 0
    psum[0].append(0)
    for i,x in enumerate(arr, start=1):
        prevsum += x
        psum[prevsum].append(i)

    log(psum)

    intervals = []
    prevsum = 0
    for left,x in enumerate(arr, start=0):
        minright = n+10
        for diff in range(1, 801):
            # find the idx number that drop below prevsum-diff
            baseline = prevsum - diff
            while psum[baseline] and psum[baseline][0] <= left:
                psum[baseline].popleft()
            if psum[baseline]:
                # log(left, x, baseline, minright)
                minright = min(minright, psum[baseline][0])
        if minright == n+10:
            intervals.append((left, n-1))
        elif minright-1 > left:
            intervals.append((left, minright-2))
        prevsum += x

    log(intervals)    

    # calcluate contribution
    grad_boost = [0 for _ in range(n+1)]
    start_decr = [0 for _ in range(n+1)]
    end_decr = [0 for _ in range(n+1)]
    for a,b in intervals:
        grad_boost[a] += b-a + 1
        start_decr[a] += 1
        end_decr[b+1] += 1

    contrib = [0 for _ in range(n)]
    log(grad_boost)
    log(start_decr)
    log(end_decr)

    cur_val = 0
    cur_grad = 0
    for i in range(n):
        cur_val += grad_boost[i]
        contrib[i] += cur_val
        cur_grad -= start_decr[i]
        cur_grad += end_decr[i]
        cur_val += cur_grad

    log(contrib)

    return sum(a*b for a,b in zip(contrib, arr))


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
