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


def solve_(n, m, mrr, nrr):
    # your solution here

    matrix = [[(int(a)-int(b))%3 for a,b in zip(r1, r2)] for r1,r2 in zip(mrr, nrr)]
    log(matrix)
    
    for i in range(n-1):
        for j in range(m-1):
            if matrix[i][j] == 0:
                continue
            elif matrix[i][j] == 1:

                matrix[i][j] = (matrix[i][j] + 2)%3
                matrix[i+1][j+1] = (matrix[i+1][j+1] + 2)%3

                matrix[i+1][j] = (matrix[i+1][j] + 1)%3
                matrix[i][j+1] = (matrix[i][j+1] + 1)%3

            elif matrix[i][j] == 2:

                matrix[i][j] = (matrix[i][j] + 1)%3
                matrix[i+1][j+1] = (matrix[i+1][j+1] + 1)%3

                matrix[i+1][j] = (matrix[i+1][j] + 2)%3
                matrix[i][j+1] = (matrix[i][j+1] + 2)%3

    if sum(sum(row) for row in matrix) == 0:
        return yes

    return no


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
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_strings(n)  # and return as a list of list of int
    nrr = read_strings(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr,nrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
