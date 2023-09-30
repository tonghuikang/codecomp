#!/usr/bin/env python3
import sys
import functools
import itertools

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


def parse(matrix):
    return tuple(tuple(1 if x == "#" else 0 for x in row) for row in matrix)

@functools.cache
def translate(mrr, dx, dy):
    res = [[0 for _ in range(4)] for _ in range(4)]

    for x,row in enumerate(mrr):
        for y,cell in enumerate(row):
            if cell == 1:
                xx = x+dx
                yy = y+dy
                if not (0 <= xx <= 3 and 0 <= yy <= 3):
                    return None
                res[xx][yy] = 1
    
    return res


# matrix = [col[::-1] for col in zip(*matrix)]  # once
# matrix = [col[::-1] for col in matrix][::-1]  # twice
# matrix = [col for col in zip(*matrix)][::-1]  # thirce


def solve_(arr,brr,crr):
    # your solution here

    if sum(sum(row) for row in arr) + sum(sum(row) for row in brr) + sum(sum(row) for row in crr) != 16:
        # log("wrong sum")
        return no

    # (7*7*4)**3
    # 7 million

    # assume A not need to rotate
    for a,b,c,d,e,f in itertools.product([0,-3,-2,-1,1,2,3], repeat=6):
        xrr = translate(arr, a, b)
        yrr = translate(brr, c, d)
        zrr = translate(crr, e, f)

        # log(xrr)
        # log(yrr)
        # log(zrr)

        if xrr is None or yrr is None or zrr is None:
            continue

        for _ in range(4):
            for _ in range(4):

                res = [[0 for _ in range(4)] for _ in range(4)]

                flag = True
                for qrr in [xrr, yrr, zrr]:
                    for i,row in enumerate(qrr):
                        for j,cell in enumerate(row):
                            if cell == 1:
                                if res[i][j] == 1:
                                    flag = False
                                res[i][j] = 1
                
                # log(res)

                if flag == True:
                    return yes

                # raise
                zrr = [col[::-1] for col in zip(*zrr)]
            yrr = [col[::-1] for col in zip(*yrr)]

    return no


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
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    arr = parse(read_strings(4))
    brr = parse(read_strings(4))
    crr = parse(read_strings(4))

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr,brr,crr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
