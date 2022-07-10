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


def remove_consecutive_duplicates(lst):
    res = []
    for x in lst:
        if res and x == res[-1]:
            continue
        res.append(x)
    return res


LARGE = 10**18
LARGE2 = 10**8

def solve_(arr, brr, n, m):
    # your solution here
    arr = remove_consecutive_duplicates(arr)

    setbrr = set(brr)

    key_to_loc = {x:[-LARGE2] for x in setbrr}

    for i,x in enumerate(brr):
        key_to_loc[x].append(i)

    for k in key_to_loc:
        key_to_loc[k].append(LARGE2)

    # log(key_to_loc)

    dp = {}
    for idx in key_to_loc[arr[0]]:
        dp[idx] = 0
    dp[-LARGE2] = LARGE
    dp[LARGE2] = LARGE

    def transition(dp, old_idxs, new_idxs):
        # assert len(old_idxs) == len(dp)
        # assert set(dp.keys()) == set(old_idxs)

        new_dp = {idx:LARGE for idx in new_idxs}
        aptr = 0
        bptr = 0
        mincost = LARGE
        while aptr < len(old_idxs) and bptr < len(new_idxs):
            if old_idxs[aptr] < new_idxs[bptr]:
                cost = dp[old_idxs[aptr]] - old_idxs[aptr]
                mincost = min(mincost, cost)
                aptr += 1
            else:
                new_dp[new_idxs[bptr]] = new_idxs[bptr] + mincost
                bptr += 1
            # log(aptr, bptr, mincost)
        return new_dp

    for a,b in zip(arr, arr[1:]):
        old_idxs = key_to_loc[a]
        new_idxs = key_to_loc[b]

        new_dp1 = transition(dp, old_idxs, new_idxs)
        new_dp2 = transition({-k:v for k,v in dp.items()}, [-x for x in old_idxs[::-1]], [-x for x in new_idxs[::-1]])

        # log()
        # log(dp)
        # log({-k:v for k,v in dp.items()})
        # log(new_dp1)
        # log(new_dp2)

        dp = {}
        for k,v in new_dp1.items():
            dp[k] = min(v, new_dp2[-k])

        # log(dp)

    return min(dp.values())


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
