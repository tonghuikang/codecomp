#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import heapq, time
from collections import defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr, target):
    start_time = time.time()
    # your solution here

    psum = [0]
    for x in arr:
        psum.append(x + psum[-1])

    segments = defaultdict(list)

    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            segment_sum = psum[j] - psum[i]
            if segment_sum > target:
                continue
            segments[segment_sum].append((i,j))

    for k in segments:
        segments[k].sort(key=lambda x: x[1])

    minres = 10**18
    if target in segments:
        minres = min(j-i for i,j in segments[target])

    for x in segments:
        if time.time() - start_time > 1.5:
            break

        # log(x, target-x)
        if target-x not in segments:
            continue
        # log(segments[x])
        # log(segments[target-x])
        # log()

        right = [(j-i,i,j) for i,j in segments[target-x]]
        right.sort()

        for i,j in segments[x]:
            while right and right[0][1] < j:
                heapq.heappop(right)
            if not right:
                break
            if right[0][0] >= minres:
                break
            res = j-i + right[0][0]
            minres = min(minres, res)


    if minres == 10**18:
        return -1

    return minres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
