#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
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
        # log(*args)
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


class FenwickTree:
    # also known as Binary Indexed Tree
    # binarysearch.com/problems/Virtual-Array
    # https://leetcode.com/problems/create-sorted-array-through-instructions
    # may need to be implemented again to reduce constant factor

    # ALL ELEMENTS ARE TO BE POSITIVE
    def __init__(self, bits=31):
        self.c = defaultdict(int)
        self.LARGE = 2**bits

    def update(self, x, increment):
        # future query(y) to increase for all y >= x
        x += 1  # to avoid infinite loop at x > 0
        while x <= self.LARGE:
            # increase by the greatest power of two that divides x
            self.c[x] += increment
            x += x & -x

    def query(self, x):
        x += 1  # to avoid infinite loop at x > 0
        res = 0
        while x > 0:
            # decrease by the greatest power of two that divides x
            res += self.c[x]
            x -= x & -x
        return res


def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

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



def solve_(state,mrr,n,m):
    # your solution here
    # binary serach on fenwick tree

    c1 = FenwickTree()
    c2 = FenwickTree()
    c2c = [None, c1, c2, ]

    acnt = [0,0,0]

    state = nrr

    for i,val in enumerate(nrr, start=1):
        c2c[val].update(i, 1)
        acnt[val] += 1

    res = 0

    for i,new_val,z in mrr:
        prev_val = state[i-1]
        c2c[prev_val].update(i, -1)
        c2c[new_val].update(i, 1)
        acnt[prev_val] -= 1
        acnt[new_val] += 1
        state[i-1] = new_val

        m1, m2 = c1.query(z), c2.query(z)
        n1, n2 = acnt[1] - m1, acnt[2] - m2

        # log(i,new_val,z)
        # log(state)
        # log(acnt)
        
        leftsum = m1 * 1 + m2 * 2
        rightsum = n1 * 1 + n2 * 2

        val = 0

        if (leftsum + rightsum) % 2 == 1:
            # log()
            # log(leftsum, rightsum)
            # log("val", -1)
            # log()
            res -= 1
            continue
        if leftsum == rightsum:
            continue

        diff = (rightsum - leftsum) // 2
        log(state)
        log(diff)
        log()

        if diff < 0:
            # left is smaller
            if m1 < diff or n2 < diff:
                # not enough to swap
                res -= 1
                continue
            
            # get k rightmost ones on left
            # get last position where count one is less than m1-k
            def func(x):
                q = c1.query(x)
                return q <= m1 - k

            # get k leftmost twos on right
            # get first position where count one is more than m2+k
            def func(x):
                q = c2.query(x)
                return q >= m1 - k

                

            binary_search()

        



    return res


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
    n,m = list(map(int,input().split()))
    nrr = list(map(int,input().split()))

    log("qq",case_num,n,n)
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(nrr,mrr,n,m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
