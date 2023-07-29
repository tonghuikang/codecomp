#!/usr/bin/env python3
import sys
import random
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
CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
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


def solve_(arr):
    # your solution here

    arr_original = [x for x in arr]
    n = len(arr)

    # build a large number and snowball

    if sorted(arr) == arr:
        return []

    res = []
    num_ops = [0]

    def op(i,j):
        arr[i] += arr[j]
        res.append([i, j])
        num_ops[0] += 1

    # make positive
    if max(arr) > 0:
        for i in range(n):
            while arr[i] != max(arr):
                idx = arr.index(max(arr))
                op(i, idx)
                # log(arr)

        if num_ops[0] <= 31:
            assert sorted(arr) == arr
            assert num_ops[0] <= 31
            return res

    res = []
    num_ops = [0]
    arr = arr_original

    assert min(arr) < 0

    # make negative
    for i in range(n-1, -1, -1):
        while arr[i] != min(arr):
            idx = arr.index(min(arr))
            op(i, idx)
            # log(arr)

    assert sorted(arr) == arr
    assert num_ops[0] <= 31
    return res


if OFFLINE_TEST:
    solve([x for x in range(20)])
    solve([x for x in range(1,20+1)])
    solve([x for x in range(20,0,-1)])
    solve([-x for x in range(20)])
    solve([-x for x in range(1,20+1)])
    solve([-x for x in range(20,0,-1)])


while OFFLINE_TEST:
    arr = [random.randint(-20,20) for _ in range(random.randint(1,20))]
    solve(arr)


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

    res = solve(arr)  # include input here

    print(len(res))
    if len(res) == 0:
        continue
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x+1) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
