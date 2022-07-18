#!/usr/bin/env python3
import sys
import heapq
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
CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
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


def solve_(arr, n, k):
    arr = set(arr)
    # your solution here
    maxarr = max(arr)
    minarr = min(arr)
    minres = maxarr - minarr

    arr = [((x//k),k,x) for i,x in enumerate(arr)]
    arr.sort()

    minn = arr[0][0]
    maxx = arr[-1][0]
    minres = maxx - minn

    if minres == 0:
        return 0

    maxx = max(1, maxx)

    # maxx = -minarr
    # jump = max(1, min(int(maxarr // minarr) - 1, int(maxarr // k)))
    # jump = 1
    # log(jump)

    while arr[0][1] > 1:
        nx,i,x = heapq.heappop(arr)
        i = max(1, (x // maxx) + 1)
        while i > 1 and (x//i) == nx:
            i -= 1
        nx = (x//i)
        heapq.heappush(arr, (nx,i,x))

        # log((nx,i,x))

        maxx = max(maxx, nx)
        minn = arr[0][0]
        # if maxx - minn < minres:
        #     log((nx,i,x), maxx - minn)
        minres = min(minres, maxx - minn)
        if minres == 0:
            break

    return minres

# LARGE = 3000
# res = solve([1] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# res = solve([1] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# res = solve([LARGE - 100] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# arr = list(range(LARGE - 10000, LARGE))
# res = solve(arr, len(arr), LARGE)
# print("ok", LARGE, res)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
