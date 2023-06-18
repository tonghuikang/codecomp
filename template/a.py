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


def solve_(a,b,c,k):
    # your solution here

    if c < a or c < b:
        return -1

    if max(a,b) + 1 < c:
        return -1

    cntr = 0
    k -= 1

    a_min = int("1" + "0"*(a-1))
    a_max = int("9"*a)

    b_min = int("1" + "0"*(b-1))
    b_max = int("9"*b)

    c_min = int("1" + "0"*(c-1))
    c_max = int("9"*c)

    a_val = a_min

    while cntr <= k:
        b_curmin = max(b_min, c_min - a_val)
        b_curmax = min(b_max, c_max - a_val)

        if b_curmin > b_curmax:
            break

        if k - cntr < b_curmax - b_curmin + 1:
            log(a_val, b_curmin, b_curmax)
            b_curmin += k - cntr
            return a_val, b_curmin

        cntr += b_curmax - b_curmin + 1
        a_val += 1
        if a_val > a_max:
            break

    return -1


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
    a,b,c,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b,c,k)  # include input here

    if res == -1:
        print(res)
        continue

    x,y = res
    z = x+y

    log(x,y,z)

    assert len(str(x)) == a
    assert len(str(y)) == b
    assert len(str(z)) == c

    print(x,"+",y,"=",z)
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
