#!/usr/bin/env python3
import sys
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

def mex(arr):
    for i in range(1, len(arr) + 2):
        if i not in arr:
            return i



def solve_check(n, arr, brr):
    # your solution here

    res = 0

    for i in range(n):
        for j in range(i+1,n+1):
            xrr = arr[i:j]
            yrr = brr[i:j]
            if mex(xrr) == mex(yrr):
                log(i,j,mex(xrr),xrr)
                res += 1

    return res

def cnt(x):
    return (x * (x+1)) // 2

def solve_(n, arr, brr):
    # your solution here

    aidxs = {x:i for i,x in enumerate(arr)}
    bidxs = {x:i for i,x in enumerate(brr)}

    left1 = arr.index(1)
    left2 = brr.index(1)

    a,b = min(left1, left2), max(left1, left2)
    x,y,z = a, max(0, b-a-1), n-b-1

    # log(x,y,z)

    res = cnt(x) + cnt(y) + cnt(z)

    left, right = a,b
    apool = set(arr[left:right+1])
    bpool = set(brr[left:right+1])

    for x in range(1,n):
        # log()
        # log(x)
        # log(arr[left:right+1])
        # log(brr[left:right+1])
        aidx = aidxs[x+1]
        bidx = bidxs[x+1]

        if not((left <= aidx <= right) or (left <= bidx <= right)):
            left_limit = 0
            right_limit = n-1

            if aidx <= left:
                left_limit = max(left_limit, aidx + 1)
            if bidx <= left:
                left_limit = max(left_limit, bidx + 1)

            if right <= aidx:
                right_limit = min(right_limit, aidx - 1)
            if right <= bidx:
                right_limit = min(right_limit, bidx - 1)

            left_space = left - left_limit + 1
            right_space = right_limit - right + 1

            # log(left_space, right_space)
            res += left_space * right_space

        new_left = min(left, aidx, bidx)
        new_right = max(right, aidx, bidx)

        left = new_left
        right = new_right

    return res + 1


# while OFFLINE_TEST:
#     n = random.randint(1,5)
#     arr = list(range(1,n+1))
#     brr = list(range(1,n+1))
#     import random
#     random.shuffle(arr)
#     random.shuffle(brr)
#     a = solve(n, arr, brr)
#     b = solve_check(n, arr, brr)
#     if a != b:
#         log(arr)
#         log(brr)
#         log(a,b)
#         assert False



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, arr, brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
