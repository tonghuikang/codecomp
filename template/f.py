#!/usr/bin/env python3
import sys # , getpass
# import math, random
# import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "hkmac"
OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
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

# ---------------------------- template ends here ----------------------------

def check(mrr):
    # matrix = 
    mrr = [[""]*len(mrr[0])] + mrr + [[""]*len(mrr[0])]
    mrr = [[""] + row + [""] for row in mrr]
    for x,row in enumerate(mrr[1:-1], start=1):
        for y,cell in enumerate(row[1:-1], start=1):
            series = ""
            for dx,dy in d4:
                series += mrr[x+dx][y+dy]
            if len(set(series)) == 3:
                log(series)
                log("ERROR")
                print(mrr)
                # assert 1 == 2
                return False
                # return []
    return True

def solve_(n,m,a,b,c):
    # print(n,m,a,b,c)
    nn = n
    mm = m
    rx = a
    gx = b
    bx = c
    # your solution here

    transposed = False
    if n > m:
        transposed = True
        n,m = m,n

    matrix = [["" for _ in range(m)] for _ in range(n)]
    # n >= m

    (a,acol),(b,bcol),(c,ccol) = sorted([(a,"R"), (b,"G"), (c,"B")])
    # print(matrix)
    # if c >= m*3 or a == 0 or n == 1 or b <= n*(n+1)//2:
    #     # you can sort by colors
    #     arr = [acol]*a + [ccol]*c + [bcol]*b
    #     for i in range(n):
    #         for j in range(m):
    #             matrix[i][j] = arr[i*m + j]
    # else:
    if True:
        # arr = [acol]*a + [ccol]*c + [bcol]*b
        # for i in range(n):
        #     for j in range(m):
        #         matrix[i][j] = arr[i*m + j]
        # if check(matrix):
        #     pass
        # else:
            # split a and c as sum of distinct numbers smaller than n
            aa = a
            arr = []
            z = n

            avail = set()
            for i in range(n):
                for j in range(m):
                    avail.add((min(n,i+j+1,(n-i-1)+(m-j-1)+1),i+j+1)) # amount, idx
                    
            avail = sorted(avail)[::-1]
            # print(avail)

            aa = a
            arr = []
            arr2 = set()
            for amount,idx in avail:
                if aa >= amount:
                    aa -= amount
                    arr.append(amount)
                    arr2.add(idx)
            # arr = set(arr)

            bb = b
            brr = []
            brr2 = set()
            for amount,idx in avail:
                if idx in arr2:
                    continue
                if bb >= amount:
                    bb -= amount
                    brr.append(amount)
                    brr2.add(idx)
            # brr = set(brr)

            # print(arr)
            # print(brr)
            # assert sum(arr) == a
            # assert sum(brr) == b
            # print(arr, brr)

            matrix = [[ccol for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if i+j+1 in arr2:
                        matrix[i][j] = acol
                    if i+j+1 in brr2:
                        matrix[i][j] = bcol

            matrix = [row[::-1] for row in matrix[::-1]]
            # print(matrix)
            # for i in range(n):
            #     for j in range(m):
            #         if i+j+1 in brr:
            #             matrix[i][j] = bcol

    if transposed:
        matrix = [list(row) for row in zip(*matrix)]
    
    matrix = [[cell for cell in row] for row in matrix]
    # print(matrix)
    assert check(matrix)

    # print("\n".join(["".join(row) for row in matrix]))

    assert len(matrix) == nn
    for row in matrix:
        assert len(row) == mm
    flat = sum(matrix, [])
    crr = Counter(flat)
    assert crr["R"] == rx
    assert crr["G"] == gx
    assert crr["B"] == bx
    # print()
    return "\n".join(["".join(row) for row in matrix])


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,m,a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(n,m,a,b,c)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)