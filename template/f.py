#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

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


modval = 999_999_893

from functools import cache

@cache
def modinv_p(base):
    # modular inverse if the modulo is a prime
    return pow(base, -1, modval)  # for Python 3.8+
    # return pow(base, p-2, p)  # if Python version is below 3.8


import math
s2 = math.sqrt(2)

def simplify(a,b,c,d):
    # a + b sqrt(2)
    # c + d sqrt(2)

    x = (a*c - 2*b*d) * modinv_p(c*c - 2*d*d)
    y = (b*c - a*d) * modinv_p(c*c - 2*d*d)
    return x, y


def solve_(n):
    # your solution here

    sets = n // 2
    p = 2 * sets * (sets + 1) // 2

    sets = (n - 1) // 2
    q = 2 * sets * (sets + 1) // 2

    x = n // 4
    y = (n - 1) // 4

    
    log(x,y)
    log()



    # p + ( q + ?)sqrt(2)
    # ---------
    # p + (q+2 + ?)sqrt(2)

    log(p,q)
    log(p,q+2)
    log()

    a = p
    b = q
    c = p
    d = q+2

    if x >= 1:
        a += 1
        c += 1 - modinv_p(pow(2, -x, modval))

    if y >= 1:
        a += 1 - modinv_p(pow(2, -x, modval))
        c += 1

    return simplify(a,b,c,d)[1]%modval

    # # aa - 2bc + (ab - ac)sqrt(2)
    # # aa - 2cc

    # log(a*a - 2*b*c, a*b - a*c)
    # log(a*a - 2*c*c)
    # log()

    # log((p + q*s2)/(p + (q+2)*s2))
    # log((a*a - 2*b*c + (a*b - a*c)*s2)/(a*a - 2*c*c))
    # log()

    # res = (a*b - a*c) * modinv_p(a*a - 2*c*c)

    # return res%modval



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
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
