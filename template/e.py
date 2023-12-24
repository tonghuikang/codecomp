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
yes, no = "Yes", "No"
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

def check(n, k, matrix):
    # return
    # print(n,k)
    for row in matrix:
        log(row)

    assert len(matrix) == n
    for row in matrix:
        assert len(row) == n
    assert sum(sum(row) for row in matrix) == k

    rowxors = []
    for x in range(n):
        val = 0
        for y in range(n):
            if matrix[x][y] == 1:
                val += 1
        rowxors.append(val%2)
        
    colxors = []
    for y in range(n):
        val = 0
        for x in range(n):
            if matrix[x][y] == 1:
                val += 1
        colxors.append(val%2)
            
    assert len(set(rowxors)) == 1
    assert len(set(colxors)) == 1


def flip_matrix(matrix):
    return [[1-x for x in row] for row in matrix]


def solve3(n, k):
    log("solve3", n, k)

    if k%4 == 0:
        kset = k // 4
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n//2):
            for j in range(n//2):
                if kset == 0:
                    continue
                kset -= 1
                for x in range(2):
                    for y in range(2):
                        matrix[2*i + x][2*j + y] = 1
        
        return matrix
        
    if k%4 == 2:
        kset = (k - 6) // 4
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n//2):
            for j in range(n//2):
                if kset == 0:
                    continue
                kset -= 1
                for x in range(2):
                    for y in range(2):
                        matrix[2*i + x][2*j + y] = 1

        matrix[~0][~0] = 1
        matrix[~0][~1] = 1
        matrix[~1][~0] = 1
        
        matrix[~2][~2] = 1
        matrix[~2][~1] = 1
        matrix[~1][~2] = 1

    return matrix


def solve2(n, k):
    log("solve2", n, k)
    if k == 0:
        return [[0 for _ in range(n)] for _ in range(n)]

    if k == n:
        return [[1 if x == y else 0 for x in range(n)] for y in range(n)]

    if k == 2:
        return []
    
    if n%2 == 0 and k%2 == 1:
        return []

    if n%2 == 1 and k%2 == 1:
        if k < n:
            return []
        if n < k < 2*n:
            matrix = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                matrix[0][i] = 1
                matrix[i][0] = 1
            excess = k - n
            for x in range(n):
                for y in range(n):
                    if x + y < n-excess-1:
                        matrix[x][y] = 0
                    if x + y == n-excess-1:
                        matrix[x][y] = 1
            # print("check")
            return matrix

    if n%2 == 1 and k%2 == 1:
        matrix = solve3(n, n*n-k)
        matrix = flip_matrix(matrix)
    else:
        matrix = solve3(n, k)

    return matrix


def solve_(n, k):
    # your solution here

    if k > n*n // 2:
        matrix = solve2(n, n*n-k)
        matrix = flip_matrix(matrix)
    else:
        matrix = solve2(n, k)

    if matrix == []:
        return matrix

    check(n, k, matrix)

    return matrix


for n in range(1, 10):
    for k in range(0, n*n+1):
        solve(n, k)


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
    n, k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, k)  # include input here

    if res == []:
        print(no)
        continue
    print(yes)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
