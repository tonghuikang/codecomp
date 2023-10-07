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
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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


def solve_(n, arr):
    # your solution here

    if n == 1:
        return 1

    arr.sort()
    minres = 10**18

    target_sum = arr[0] + arr[-2]
    addn = target_sum - arr[-1]
    brr = [addn] + arr


    for a,b in zip(brr, brr[::-1]):
        if a + b != target_sum:
            break
    else:
        if addn > 0:
            minres = min(minres, addn)

    # log(addn)
    del addn

    target_sum = arr[1] + arr[-1]
    addn = target_sum - arr[0]
    brr = arr + [addn]

    for a,b in zip(brr, brr[::-1]):
        if a + b != target_sum:
            break
    else:
        if addn > 0:
            minres = min(minres, addn)

    # log(addn)
    del addn

    # from collections import Counter
    # log(Counter(arr).items())

    target_sum = arr[0] + arr[-1]
    for a,b in zip(arr[:n], arr[::-1]):
        log("-")
        log(a,b)
        if a + b != target_sum:
            break

    addn1 = target_sum - a
    addn2 = target_sum - b

    log("x")
    log(target_sum)
    log(addn1)
    log(addn2)

    brr = arr + [addn1]
    brr.sort()

    for a,b in zip(brr, brr[::-1]):
        if a + b != target_sum:
            break
    else:
        if addn1 > 0:
            minres = min(minres, addn1)

    brr = arr + [addn2]
    brr.sort()

    for a,b in zip(brr, brr[::-1]):
        if a + b != target_sum:
            break
    else:
        if addn2 > 0:
            minres = min(minres, addn2)

    if minres == 10**18:
        return -1

    return minres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
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
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
