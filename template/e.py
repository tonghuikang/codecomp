#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 998244353
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

def modinv_p(base, p=m9):
    
    # modular inverse if the modulo is a prime
    return pow(base, -1, p)  # for Python 3.8+
    # return pow(base, p-2, p)  # if Python version is below 3.8


def solve_(n, arr):
    # your solution here

    def compare(x,y):
        arr = bin(x)[2:]
        brr = bin(y)[2:]
        if len(arr) < len(brr) or x == 0:
            return 1
        if len(arr) > len(brr) or y == 0:
            return 2

        crr = []
        drr = []

        for a,b in zip(arr, brr):
            if a == b == "0":
                continue
            crr.append(a)
            drr.append(b)

        arr = crr
        brr = drr

        if len(arr) == 1:
            return 2

        res = 0
        for a,b in zip(arr, brr):
            if a == b == "1":
                res += 2
            elif b == "1":
                res += 1
                break
            elif a == "1":
                res += 0
                break
        if a == b == "1":
            res -= 1
        
        return res


    # log(compare(7,7))

    # log([(len(bin(y)) - 2) for y in arr])
    # log(sum([(bin(y).count("1")) for y in arr]))

    allres = 0
    for x in arr:
        for y in arr:
            res = compare(x,y)
            # log(x, y, bin(x)[2:], bin(x)[2:].count("1"), res)
            log(x, y, bin(x)[2:].count("1"), res)
            allres += res
            # log(allres)

    # 187
    log(allres)

    return (allres * modinv_p(n) * modinv_p(n)) % m9


# for x in range(10000):
#     if (x * modinv_p(8) * modinv_p(8)) % m9 == 77987843:
#         log(x)
#         log("nnn")


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
    arr.sort()
    # arr = [2*x for x in arr]
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
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
