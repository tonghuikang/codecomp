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

# ---------------------------- template ends here ----------------------------


def solve_(n):
    # your solution here

    res = []

    pools = [(list(map(int,input().split())), list(map(int,input().split()))),]

    for i in range(29,-1,-1):
        # log(pools)
        topmask = 2**i
        onemask = topmask - 1
    
        fail = False
        for ar,br in pools:
            acount = sum(x&topmask > 0 for x in ar)
            bcount = sum(x&topmask > 0 for x in br)
            # log(acount, bcount, len(ar))
            if acount + bcount != len(ar):
                fail = True
        
        if fail:
            res.append(0)
            # pools = [
            #     ([x&onemask for x in ar], [x&onemask for x in br]) 
            #     for ar, br in pools
            # ]

        else:
            new_pools = []
            res.append(1)
            while pools:
                ar, br = pools.pop()
                ar0 = [a for a in ar if not a&topmask]
                ar = [a for a in ar if a&topmask]
                br0 = [b for b in br if not b&topmask]
                br = [b for b in br if b&topmask]
                new_pools.append((ar0, br))
                new_pools.append((ar, br0))
            pools = new_pools

    log(res)

    return int("".join(str(x) for x in res),2)


# log(solve(range(2**29,2**29+2**17), range(2**29,2**29+2**17), 2**17))

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
    # arr = list(map(int,input().split()))
    # brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
