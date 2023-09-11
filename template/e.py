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

def gaussian_elimination(matrix):
    n = len(matrix)
    
    # Forward Elimination
    for i in range(n):
        max_row_idx = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row_idx] = matrix[max_row_idx], matrix[i]
        
        for j in range(i+1, n):
            ratio = matrix[j][i]/matrix[i][i]
            
            for k in range(n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    # Backward Substitution
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i-1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]
    
    return x

# # Define the augmented matrix
# matrix = [[2, 3, 3, 9],
#           [1, 1, 17, 4],
#           [3, 13, 14, 12]]

# # Call the function
# solution = gaussian_elimination(matrix)
# print('The solutions are ', solution)


def query(pos):
    print("? {}".format(pos + 1), flush=True)
    response = int(input())
    return response


def alert(pos):
    res = 0
    for x in pos:
        res = res^x
    print("! {}".format(res), flush=True)



def solve_(n,k):
    # your solution here

    allres = []

    while n >= 2*k:
        val = query(n-k)
        allres.append(val)
        n -= k

    if n == k:
        val = query(0)
        allres.append(val)
        alert(allres)
        return
    
    system = []
    
    variables = list(range(n//2))

    for _ in range(n//2):
        val = query(0)
        variables[:k//2] = variables[:k//2][::-1]
        row = [0 for _ in range(n//2 + 1)]
        for idx in variables[:k//2]:
            row[idx] += 1
        row[-1] = val
        system.append(row)

        val = query(n-k)
        variables[-k//2:] = variables[-k//2:][::-1]
        row = [0 for _ in range(n//2 + 1)]
        for idx in variables[-k//2:]:
            row[idx] += 1
        row[-1] = val
        system.append(row)

    for row in system:
        log(row)
    allres.extend(int(x) for x in (gaussian_elimination(system[:n//2])))
    alert(allres)


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
    n,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)

sys.exit()
