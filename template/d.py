#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
from collections import deque
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


def solve_(arr, brr):
    # your solution here
    arr = [i+x for i,x in enumerate(arr)]
    brr = [i-x for i,x in enumerate(brr)]
    arr.append(len(arr))
    brr.append(len(brr))
    log(list(range(len(arr))))
    log(arr)
    log(brr)

    maxheight = 0
    source = 0
    queue = deque([source])  # post slip
    visited = {source: 0}
    backtrack = {}
    backtrack2 = {0:0}

    while queue:
        h = queue.popleft()
        log(h)

        # maxjump
        new_h = arr[h]

        if new_h > maxheight:
            for h_pre in range(maxheight+1, new_h+1):
                # slippage
                h_post = brr[h_pre]
                if h_post in visited:
                    continue
                queue.append(h_post)
                visited[h_post] = visited[h] + 1
                backtrack[h_post] = h
                backtrack2[h_post] = h_pre
            maxheight = new_h

    log(visited)

    if arr[-1] not in visited:
        return []

    target = arr[-1]
    res = [arr[-1]]
    while target != 0:
        target = backtrack[target]
        res.append(backtrack2[target])

    log(res)

    res = [arr[-1]-x for x in res][::-1]
    res = res[1:]
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # lst = minus_one(lst)

    arr.reverse()
    brr.reverse()

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr)  # include input here


    if len(res) == 0:
        print(-1)
        continue

    # print length if applicable
    print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
