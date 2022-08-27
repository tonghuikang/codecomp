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


def solve_(arr, brr, n):
    arr.sort()
    brr.sort(reverse=True)
    # your solution here

    res = []

    ranges = {0:n}

    for i in range(30,-1,-1):
        log()
        log(arr)
        log(brr)
        log(ranges)
        topmask = 2**i
        onemask = topmask - 1
    
        fail = False
        for i,j in ranges.keys():
            acount = sum(x&topmask > 0 for x in arr[i:j])
            bcount = sum(x&topmask > 0 for x in brr[i:j])
            # log(acount, bcount, len(ar))
            if acount + bcount != j-i:
                log(topmask, acount, bcount)
                fail = True
        
        if fail:
            res.append(0)

        else:
            res.append(1)
            new_ranges = []
            for i,j in ranges.keys():
                acount = sum(x&topmask > 0 for x in brr[i:j])
                # arr[i:j] = sorted(arr[i:j], key=lambda x:x&topmask)
                # brr[i:j] = sorted(brr[i:j], key=lambda x:x&topmask, reverse=True)

                ptr = j-1
                for idx in range(i,j):
                    while arr[ptr]&topmask and ptr > i:
                        ptr -= 1
                    if arr[idx]&topmask and ptr > idx:
                        arr[idx], arr[ptr] = arr[ptr], arr[idx]

                ptr = j-1
                for idx in range(i,j):
                    while not brr[ptr]&topmask and ptr > i:
                        ptr -= 1
                    if not brr[idx]&topmask and ptr > idx:
                        brr[idx], brr[ptr] = brr[ptr], brr[idx]

                # assert arr[i:j] == sorted(arr[i:j], key=lambda x:x&topmask)
                # assert brr[i:j] == sorted(brr[i:j], key=lambda x:x&topmask, reverse=True)

                new_ranges[i] = i+acount
                new_ranges[i+acount] = j
            ranges = new_ranges
        
    log()
    log(arr)
    log(brr)
    log(res)

    return int("".join(str(x) for x in res),2)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr, n)  # include input here

    # if OFFLINE_TEST:
    #     for _ in range(100):
    #         import random
    #         random.shuffle(arr)
    #         random.shuffle(brr)
            
    #         assert res == solve(arr, brr, n)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
