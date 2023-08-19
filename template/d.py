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


def solve_(n,m,mrr):
    # your solution here
    mrr = [list(row) for row in mrr]

    rows = [[0 for _ in range(26)] for _ in range(n)]
    cols = [[0 for _ in range(26)] for _ in range(m)]

    rowset = set(range(n))
    colset = set(range(m))

    for i in range(n):
        for j in range(m):
            x = abc_map[mrr[i][j]]
            mrr[i][j] = x
            rows[i][x] += 1
            cols[j][x] += 1

    # log(rows)
    # log(cols)
    # log(mrr)

    def check(counter):
        return sum(counter) == max(counter) >= 2

    res = n*m

    flag = True
    while flag:
        flag = False
        rowset_to_remove = set()
        colset_to_remove = set()

        for i in rowset:
            c = rows[i]
            if check(c):
                flag = True
                rowset_to_remove.add(i)
        
        for j in colset:
            c = cols[j]
            if check(c):
                flag = True
                colset_to_remove.add(j)

        for i in rowset_to_remove:
            rowset.remove(i)

        for j in colset_to_remove:
            colset.remove(j)

        for i in rowset:
            for j in colset_to_remove:
                x = mrr[i][j]
                rows[i][x] -= 1

        for j in colset:
            for i in rowset_to_remove:
                x = mrr[i][j]
                cols[j][x] -= 1

        # log(rowset_to_remove, colset_to_remove)

    return len(rowset) * len(colset)


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
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
