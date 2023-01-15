#!/usr/bin/env python3
import sys
from collections import Counter
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 998244353
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

def modinv_p(base, p=m9):
    # modular if the modulo is a prime
    return pow(base, p-2, p)

LARGE = 1005

def solve_(n,p):
    # your solution here

    q = 10000-p
    p = (p*modinv_p(10000))%m9
    q = (q*modinv_p(10000))%m9

    dp = {}
    arr = [0 for _ in range(LARGE)]
    arr[0] = 2
    arr[1] = 1
    dp[tuple(arr)] = p

    for k in range(1,n):
        log(k, len(dp))
        new_dp = Counter()
        numpos = 2*k+1
        mpos = modinv_p(numpos)
        for arr,v in dp.items():
            v = (v%m9 * mpos)%m9
            arr = list(arr)

            for i in range(0, LARGE-2):
                if arr[i] == 0:
                    continue
                cnt = arr[i]

                arr[i+1] += 1
                arr[i] += 1
                new_dp[tuple(arr)] += cnt * v * p
                arr[i+1] -= 1
                arr[i] -= 1

            for i in range(1, LARGE-2):
                if arr[i] == 0:
                    continue
                cnt = arr[i]

                arr[i-1] += 1
                arr[i] += 1
                new_dp[tuple(arr)] += cnt * v * q
                arr[i-1] -= 1
                arr[i] -= 1

        dp = new_dp

    # log(dp)

    return sum(dp.values())%m9


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,p = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,p)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
