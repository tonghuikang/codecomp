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



def interval_overlap(x1,x2,y1,y2):
    # given intervals [x1,x2], [y1,y2]
    # [start, end] of overlapping interval    
    # if start > end, there is no overlapping inteval
    return max(x1,y1), min(x2,y2)


def ceiling_division(numer, denom):
    return -((-numer)//denom)




def solve_(mrr):
    # your solution here

    res = []

    # inclusive
    minheight = 1
    maxheight = 5*10**18 + 10

    def calc_days(a,b,h):
        h -= a
        diff = a-b
        num_sets = max(0, ceiling_division(h, diff))  # ceiling?
        # num_sets = max(0, h // diff)  # ceiling?
        return num_sets + 1
    
    def calc_max_height_attainable(a,b,n):
        if n == 0:
            return 0
        diff = a-b
        return diff*(n-1) + a


    for arr in mrr:
        if arr[0] == 1:
            a,b,n = arr[1:]
            minheight_new = calc_max_height_attainable(a,b,n-1) + 1
            maxheight_new = calc_max_height_attainable(a,b,n)
            
            # log(minheight_new, maxheight_new)

            start,end = interval_overlap(minheight_new, maxheight_new, minheight, maxheight)

            if start > end:
                res.append(0)
            else:
                minheight = max(minheight, minheight_new)
                maxheight = min(maxheight, maxheight_new)
                res.append(1)

        if arr[0] == 2:
            a,b = arr[1:]
            upper = calc_days(a,b,minheight)
            lower = calc_days(a,b,maxheight)
            # log(minheight, maxheight)
            # log(lower, upper)
            # log()
            if upper == lower:
                res.append(upper)
            else:
                res.append(-1)


    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    q = int(input())

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
    mrr = read_matrix(q)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
