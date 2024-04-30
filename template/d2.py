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


from math import gcd

def solve_(n, m):
    # your solution here

    # res = 0
    # for a in range(1,n+1):
    #     for b in range(1,m+1):
    #         if (a+b)%(b*b) == 0:
    #             res += 1

    count = 0
    
    # we iterate through all possible gcd values
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    MAX_N = 2 * 10**6
    
    from math import gcd
    from sys import stdout
    
    # To store the results for each test case
    count = 0
    
    # Iterate over all possible values of gcd(a, b) = g
    for g in range(1, min(n, m) + 1):
        # sum (i+j) can be at least 2 (1+1) and at most max_i + max_j
        max_i = n // g
        max_j = m // g
        
        # Iterate over all possible sums (i+j)
        for s in range(2, max_i + max_j + 1):
            # Find how many values of j are there such that j*g is a multiple of s
            # and 1 <= j <= max_j and j <= s <= i + j (i = s - j)
            num_multiples = (max_j // s)  # j = s, 2s, 3s, ..., max_j
            if num_multiples > 0:
                # We need to check these j values are valid
                # i = s-j must be >= 1 and i <= max_i
                valid_js = 0
                for k in range(1, num_multiples + 1):
                    j = k * s
                    i = s - j
                    if 1 <= i <= max_i:
                        valid_js += 1
                count += valid_js
        
    return count


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
    n, m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)


