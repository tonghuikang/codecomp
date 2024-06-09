#!/usr/bin/env python3
import sys
import bisect

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



def z_function(S: list) -> list:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
    # https://cp-algorithms.com/string/z-function.html
    # length of common prefix for S[i:] and S for each i
    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z


def solve_(srr):
    # your solution here

    if srr.count("a") == len(srr):
        return len(srr) - 1

    n = len(srr)

    trr = srr.lstrip("a")
    left_a = n - len(trr)

    arr = z_function(trr)
    arr = [0] * left_a + arr


    # log(srr)
    # log(arr)

    # for each possible candidate we consider the intervals
    required = [i for i,x in enumerate(srr) if x != "a"]

    # log(required)
    
    res = 0
    for core_length in range(1, n-left_a+1):
        if srr[left_a + core_length - 1] == "a":
            continue
        # log("check", srr[left_a:left_a+core_length])

        ptr = left_a
        left = left_a
        right = n   # will be overwritten
        mininterval = n
        invalid = False

        while True:
            # log(ptr, ptr+core_length)
            idx = bisect.bisect_left(required, ptr+core_length)
            if idx == len(required):
                right = n - (ptr + core_length)
                break
            new_ptr = required[idx]
            if arr[new_ptr] < core_length:
                # log("invalid")
                invalid = True
                break
            interval = new_ptr - (ptr + core_length)
            mininterval = min(mininterval, interval)
            ptr = new_ptr

        if not invalid:
            # log("--")
            left = min(left, mininterval)
            right = min(right, mininterval)
            exclude = max(0, left + right - mininterval)
            val = (left + 1) * (right + 1) - (exclude * (exclude + 1)) // 2
            # log(left, mininterval, right)
            # log(val)
            res += val

    return res

# solve("ba" * 100_000)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
