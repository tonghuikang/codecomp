#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------

def binary_search(
    func_,  # condition function
    first=True,  # else last
    target=True,  # else False
    left=0,
    right=2**31 - 1,
) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first ^ target:
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
    else:  # find last False
        return left - 1


def calculate_median(arr):
    n = len(arr)
    arr.sort()

    if n%2 == 0:
        return arr[(n-1)//2]
    else:
        return arr[n//2]


def solve_(n, k, arr, brr):
    # your solution here

    # either you dump everything to the largest
    # or you increase the median

    if k == 0:
        # no increments allowed
        log("k=0", arr[-1], calculate_median(arr[:-1]))
        return arr[-1] + calculate_median(arr[:-1])

    xrr = [a for a,b in zip(arr, brr) if b == 1]
    yrr = [a for a,b in zip(arr, brr) if b == 0]

    xrr.sort()
    yrr.sort()

    if len(xrr) == 0:
        # no increments allowed
        log("xrr=0", yrr[-1], calculate_median(yrr[:-1]))
        return yrr[-1] + calculate_median(yrr[:-1])

    qrr = yrr + xrr[:-1]
    maxres = xrr[-1] + k + calculate_median(qrr)

    xrr.sort()
    yrr.sort()

    maxval = xrr.pop()
    
    if yrr and yrr[-1] >= maxval:
        xrr.append(maxval)
        maxval = yrr.pop()

    # log(maxval)
    # log(xrr)
    # log(yrr)

    # if yrr and xrr:

    m = len(xrr) + len(yrr)

    def func(required_median):
        xrr_violating = []
        yrr_violating = []

        allowed_violations = (m-1) // 2  # 1 -> 0, 2 -> 0, 3 -> 1, 4 -> 1, 5 -> 2

        for x in xrr:
            if x < required_median:
                xrr_violating.append(x)

        for y in yrr:
            if y < required_median:
                allowed_violations -= 1

        if allowed_violations < 0:
            return False

        fixing = xrr_violating[allowed_violations:]
        cost_to_fix = sum(required_median-x for x in fixing)
        if cost_to_fix > k:
            return False
        return True

    median = binary_search(func, first=False, target=True, left=0, right=3 * 10**9)

    res = maxval + median
    # log(res, maxval, median)

    maxres = max(maxres, res)

    return maxres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, k, arr, brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
